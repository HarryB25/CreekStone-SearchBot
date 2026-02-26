import os
import signal
import time
from typing import List, Tuple


def get_openai_timeout(default: float = 60.0) -> float:
    raw = os.getenv("OPENAI_REQUEST_TIMEOUT", "").strip()
    if not raw:
        return default
    try:
        value = float(raw)
        if value > 0:
            return value
    except Exception:
        pass
    return default


def is_gpt5_model(model_name: str) -> bool:
    return (model_name or "").startswith("gpt-5")


def _normalize_model_name(raw: str) -> str:
    # Guard against malformed .env lines like:
    # OPENAI_MODEL_ALTERNATE_2=gpt-4o-mini OPENAI_REQUEST_TIMEOUT=90
    token = (raw or "").strip()
    if not token:
        return ""
    token = token.split()[0].strip().strip(",;")
    return token


def get_model_candidates(default_model: str) -> List[str]:
    values = [
        os.getenv("OPENAI_MODEL", ""),
        os.getenv("OPENAI_MODEL_ALTERNATE_1", ""),
        os.getenv("OPENAI_MODEL_ALTERNATE_2", ""),
        default_model,
    ]
    out: List[str] = []
    seen = set()
    for raw in values:
        model = _normalize_model_name(raw)
        if not model or model in seen:
            continue
        seen.add(model)
        out.append(model)
    return out


def _is_retryable_error(exc: Exception) -> bool:
    msg = str(exc).lower()
    return (
        "timed out" in msg
        or "timeout" in msg
        or "rate limit" in msg
        or "too many requests" in msg
        or "429" in msg
        or "temporarily unavailable" in msg
    )


def _is_model_unavailable_error(exc: Exception) -> bool:
    msg = str(exc).lower()
    return (
        "model_not_found" in msg
        or "no available channel for model" in msg
        or "does not exist" in msg
        or "unsupported model" in msg
    )


def _call_with_hard_timeout(fn, timeout_sec: float):
    if timeout_sec <= 0:
        return fn()
    if not hasattr(signal, "setitimer") or not hasattr(signal, "SIGALRM"):
        return fn()

    def _handler(_signum, _frame):
        raise TimeoutError(f"request timed out after {timeout_sec}s")

    old = signal.getsignal(signal.SIGALRM)
    signal.signal(signal.SIGALRM, _handler)
    signal.setitimer(signal.ITIMER_REAL, timeout_sec)
    try:
        return fn()
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, old)


def _create_with_retry(client, kwargs: dict, timeout: float):
    last_exc = None
    for attempt in range(2):
        try:
            try:
                return _call_with_hard_timeout(
                    lambda: client.chat.completions.create(**kwargs),
                    timeout + 2,
                )
            except TypeError:
                # Some gateways do not support reasoning_effort.
                cleaned = dict(kwargs)
                cleaned.pop("reasoning_effort", None)
                return _call_with_hard_timeout(
                    lambda: client.chat.completions.create(**cleaned),
                    timeout + 2,
                )
        except Exception as exc:
            last_exc = exc
            if attempt == 0 and _is_retryable_error(exc):
                time.sleep(0.8)
                continue
            raise
    raise last_exc if last_exc else RuntimeError("chat completion failed")


def chat_completion_content(
    *,
    client,
    messages,
    max_tokens: int,
    temperature: float,
    json_mode: bool,
    default_model: str,
    timeout: float | None = None,
    retry_max_tokens: int | None = None,
) -> Tuple[str, str]:
    timeout = timeout if timeout is not None else get_openai_timeout()
    candidates = get_model_candidates(default_model)
    last_exc = None

    for model in candidates:
        for pass_index in range(2):
            kwargs = {
                "model": model,
                "messages": messages,
                "max_tokens": max_tokens if pass_index == 0 else (retry_max_tokens or max_tokens),
                "temperature": temperature,
                "timeout": timeout,
            }
            if is_gpt5_model(model):
                kwargs["reasoning_effort"] = "low"
            if json_mode and pass_index == 0:
                kwargs["response_format"] = {"type": "json_object"}

            try:
                resp = _create_with_retry(client, kwargs, timeout)
                content = (resp.choices[0].message.content or "").strip()
                if content:
                    return content, model
            except Exception as exc:
                last_exc = exc
                if _is_model_unavailable_error(exc) or _is_retryable_error(exc):
                    break
                raise

    if last_exc:
        raise last_exc
    raise RuntimeError("all models returned empty content")
