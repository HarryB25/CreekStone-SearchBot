import os
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import openai
import pytz
import requests

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from common.keyword_utils import (  # noqa: E402
    investor_keyword_prompt,
    investor_keyword_repair_prompt,
    extract_keywords_from_response,
    finalize_keywords,
    keyword_quality_check,
    synthesize_keywords_from_context,
)
from common.scoring import score_content  # noqa: E402
from common.storage import build_item_id, save_structured_items  # noqa: E402
from common.openai_fallback import chat_completion_content, get_openai_timeout, is_gpt5_model  # noqa: E402


AI_KEYWORDS = [
    "ai", "agent", "llm", "rag", "mcp", "workflow", "copilot",
    "autonomous", "multi-agent", "tool-use", "automation",
    "code", "infra", "sdk", "api", "vector",
]


def _get_base_url(default: str = "https://clawhub.ai") -> str:
    raw = os.getenv("CLAWHUB_API_BASE", "").strip()
    return raw or default


def _get_request_timeout(default: float = 45.0) -> float:
    raw = os.getenv("CLAWHUB_HTTP_TIMEOUT", "").strip()
    if not raw:
        return default
    try:
        value = float(raw)
        return value if value > 0 else default
    except Exception:
        return default


def _get_int_env(name: str, default: int, min_value: int = 1, max_value: Optional[int] = None) -> int:
    raw = os.getenv(name, "").strip()
    if not raw:
        return default
    try:
        value = int(raw)
    except Exception:
        return default
    if max_value is not None:
        return max(min_value, min(max_value, value))
    return max(min_value, value)


def _get_tz_name(default: str = "Asia/Singapore") -> str:
    raw = os.getenv("CLAWHUB_TIMEZONE", "").strip()
    return raw or default


def _get_model_name() -> str:
    raw = os.getenv("OPENAI_MODEL", "").strip()
    return raw or "gpt-5.2-2025-12-11"


def _get_openai_timeout() -> float:
    return get_openai_timeout(60.0)


def _chat_json_content(messages, max_tokens: int, temperature: float) -> str:
    model_name = _get_model_name()
    content, used_model = chat_completion_content(
        client=client,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
        json_mode=True,
        default_model=model_name,
        timeout=_get_openai_timeout(),
        retry_max_tokens=max(max_tokens, 1200 if is_gpt5_model(model_name) else 300),
    )
    if used_model != model_name:
        print(f"模型回退: {model_name} -> {used_model}")
    return content


def _chat_text_content(messages, max_tokens: int, temperature: float) -> str:
    model_name = _get_model_name()
    content, used_model = chat_completion_content(
        client=client,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
        json_mode=False,
        default_model=model_name,
        timeout=_get_openai_timeout(),
        retry_max_tokens=max(max_tokens, 700 if is_gpt5_model(model_name) else 260),
    )
    if used_model != model_name:
        print(f"模型回退: {model_name} -> {used_model}")
    return content


def _contains_any(text: str, keywords: List[str]) -> bool:
    lowered = text.lower()
    return any(k in lowered for k in keywords)


def _to_ms(dt: datetime) -> int:
    return int(dt.timestamp() * 1000)


def _resolve_date_range(target_date: str, tz_name: str) -> Tuple[int, int]:
    tz = pytz.timezone(tz_name)
    day = datetime.strptime(target_date, "%Y-%m-%d")
    day_local = tz.localize(day.replace(hour=0, minute=0, second=0, microsecond=0))
    start_ms = _to_ms(day_local.astimezone(timezone.utc))
    end_ms = _to_ms((day_local + timedelta(days=1)).astimezone(timezone.utc))
    return start_ms, end_ms


def _ms_to_iso(ms: int) -> str:
    try:
        return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    except Exception:
        return ""


def _request_json(url: str, params: Optional[dict] = None) -> dict:
    timeout = _get_request_timeout()
    last_exc = None
    for attempt in range(3):
        try:
            resp = requests.get(url, params=params or {}, timeout=timeout)
            resp.raise_for_status()
            data = resp.json()
            if not isinstance(data, dict):
                raise ValueError("unexpected response payload")
            return data
        except Exception as exc:
            last_exc = exc
            # 仅对临时错误重试
            msg = str(exc).lower()
            retryable = (
                "500" in msg
                or "502" in msg
                or "503" in msg
                or "504" in msg
                or "429" in msg
                or "timed out" in msg
                or "timeout" in msg
            )
            if attempt < 2 and retryable:
                time.sleep(1.0 * (attempt + 1))
                continue
            break
    raise last_exc if last_exc else RuntimeError("request failed")


def _fetch_skill_detail(base_url: str, slug: str) -> dict:
    url = f"{base_url.rstrip('/')}/api/v1/skills/{slug}"
    try:
        return _request_json(url)
    except Exception:
        return {}


def fetch_updated_skills(target_date: str) -> List[dict]:
    base_url = _get_base_url()
    list_url = f"{base_url.rstrip('/')}/api/v1/skills"
    tz_name = _get_tz_name()
    start_ms, end_ms = _resolve_date_range(target_date, tz_name)

    page_limit = _get_int_env("CLAWHUB_PAGE_LIMIT", 100, min_value=1, max_value=200)
    max_pages = _get_int_env("CLAWHUB_MAX_PAGES", 40, min_value=1, max_value=200)
    max_results = _get_int_env("CLAWHUB_MAX_RESULTS", 25, min_value=1, max_value=200)
    sort = os.getenv("CLAWHUB_SORT", "updated").strip() or "updated"
    allow_fallback = os.getenv("CLAWHUB_ALLOW_FALLBACK", "true").strip().lower() == "true"

    cursor = None
    collected: List[dict] = []

    for page_idx in range(max_pages):
        params = {"limit": page_limit, "sort": sort}
        if cursor:
            params["cursor"] = cursor
        try:
            data = _request_json(list_url, params=params)
        except Exception as exc:
            # ClawHub 游标分页偶发 500，保留已抓取结果并结束分页。
            if cursor:
                print(f"分页请求失败，提前结束分页: {exc}")
                break
            raise
        items = data.get("items") if isinstance(data.get("items"), list) else []
        if not items:
            break
        print(f"ClawHub 第 {page_idx + 1} 页: {len(items)} 条, 已命中 {len(collected)} 条")

        min_updated = None
        for item in items:
            updated_at = item.get("updatedAt")
            if isinstance(updated_at, (int, float)):
                min_updated = updated_at if min_updated is None else min(min_updated, updated_at)
                if start_ms <= int(updated_at) < end_ms:
                    collected.append(item)

        if len(collected) >= max_results:
            break
        if sort == "updated" and min_updated is not None and int(min_updated) < start_ms:
            break

        cursor = data.get("nextCursor")
        if not cursor:
            break

    if not collected and allow_fallback:
        print(f"{target_date} 在 {tz_name} 无更新，回退到最新 skills 列表。")
        fallback_data = _request_json(list_url, params={"limit": max_results, "sort": sort})
        fallback_items = fallback_data.get("items") if isinstance(fallback_data.get("items"), list) else []
        collected = fallback_items[:max_results]

    out: List[dict] = []
    seen = set()
    for item in collected:
        slug = str(item.get("slug", "")).strip()
        if not slug or slug in seen:
            continue
        seen.add(slug)
        out.append(item)
        if len(out) >= max_results:
            break
    return out


def _build_skill_url(base_url: str, slug: str, owner: dict) -> str:
    handle = str(owner.get("handle", "")).strip() if isinstance(owner, dict) else ""
    owner_id = str(owner.get("userId", "")).strip() if isinstance(owner, dict) else ""
    if handle:
        return f"{base_url.rstrip('/')}/{handle}/{slug}"
    if owner_id:
        return f"{base_url.rstrip('/')}/{owner_id}/{slug}"
    return f"{base_url.rstrip('/')}/skills?q={slug}"


def _get_base_openai_url(default: str = "https://api.openai.com/v1") -> str:
    raw = os.getenv("OPENAI_BASE_URL", "").strip()
    return raw or default


api_key = os.getenv("OPENAI_API_KEY", "").strip()
if api_key:
    try:
        client = openai.Client(api_key=api_key, base_url=_get_base_openai_url())
        print(f"成功初始化 OpenAI 客户端 (使用API地址: {_get_base_openai_url()})")
    except Exception as e:
        print(f"初始化 OpenAI 客户端失败: {e}")
        client = None
else:
    print("警告: 未设置 OPENAI_API_KEY，将使用降级流程（无翻译、关键词与评分较弱）")
    client = None


class ClawHubSkill:
    def __init__(self, base_url: str, data: dict):
        self.base_url = base_url.rstrip("/")
        self.slug = str(data.get("slug", "")).strip()
        self.display_name = str(data.get("displayName", "")).strip() or self.slug
        self.summary_en = str(data.get("summary", "")).strip()
        self.created_at_ms = int(data.get("createdAt") or 0)
        self.updated_at_ms = int(data.get("updatedAt") or 0)
        self.stats = data.get("stats") if isinstance(data.get("stats"), dict) else {}
        self.tags = data.get("tags") if isinstance(data.get("tags"), dict) else {}
        self.latest_version = data.get("latestVersion") if isinstance(data.get("latestVersion"), dict) else {}
        self.owner = data.get("owner") if isinstance(data.get("owner"), dict) else {}
        self.moderation = data.get("moderation")

        self.url = _build_skill_url(self.base_url, self.slug, self.owner)
        self.detail_url = f"{self.base_url}/api/v1/skills/{self.slug}"

        self.changelog = str(self.latest_version.get("changelog", "")).strip()
        self.description_en = self._compose_description_en()
        self.description_zh = self._translate_description()
        self.keywords = self._generate_keywords()
        self.score = score_content(
            (
                f"来源: ClawHub skill\n"
                f"名称: {self.display_name}\n"
                f"简介: {self.summary_en}\n"
                f"版本更新: {self.changelog[:1400]}\n"
                f"关键词: {self.keywords}\n"
                f"中文介绍: {self.description_zh}\n"
            ),
            client,
            kind="clawhub",
        )

    def _compose_description_en(self) -> str:
        summary = self.summary_en
        changelog = self.changelog
        if changelog:
            snippet = changelog[:1200]
            return f"{summary}\n\nLatest changelog:\n{snippet}".strip()
        return summary

    def _translate_description(self) -> str:
        if client is None:
            return self.description_en
        source_text = self.description_en[:2600]
        try:
            content = _chat_text_content(
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "你是技术产品分析助手。请将输入整理成中文简介，"
                            "重点说明：能力边界、典型场景、关键技术形态。"
                            "忽略安装命令、模板化说明。"
                        ),
                    },
                    {
                        "role": "user",
                        "content": (
                            "请用 2-4 句中文输出，不要分点，不要标题。\n"
                            f"{source_text}"
                        ),
                    },
                ],
                max_tokens=700 if is_gpt5_model(_get_model_name()) else 260,
                temperature=0.3,
            )
            text = (content or "").strip()
            return text or self.description_en
        except Exception as e:
            print(f"翻译失败 {self.slug}: {e}")
            return self.description_en

    def _generate_keywords(self) -> str:
        base_text = f"{self.display_name}\n{self.description_en}"
        if client is None:
            fallback = finalize_keywords(
                [self.display_name, self.summary_en, self.changelog],
                base_text,
                source="github",
            )
            ok, _ = keyword_quality_check(fallback, base_text, source="github")
            if not ok:
                fallback = synthesize_keywords_from_context(base_text, source="github", max_items=10)
            return ", ".join(fallback)

        try:
            raw = _chat_json_content(
                messages=investor_keyword_prompt(
                    subject="Open Source Repository",
                    title=self.display_name,
                    subtitle="ClawHub Skill",
                    description=self.description_en[:2600],
                ),
                max_tokens=1200 if is_gpt5_model(_get_model_name()) else 240,
                temperature=0.3,
            )
            items = extract_keywords_from_response(raw)
            items = finalize_keywords(items, base_text, source="github")
            ok, reason = keyword_quality_check(items, base_text, source="github")
            if not ok:
                repaired_raw = _chat_json_content(
                    messages=investor_keyword_repair_prompt(
                        subject="Open Source Repository",
                        title=self.display_name,
                        subtitle="ClawHub Skill",
                        description=self.description_en[:2600],
                        bad_keywords=items,
                        reason=reason,
                    ),
                    max_tokens=1000 if is_gpt5_model(_get_model_name()) else 220,
                    temperature=0.2,
                )
                repaired = extract_keywords_from_response(repaired_raw)
                repaired = finalize_keywords(repaired, base_text, source="github")
                repaired_ok, _ = keyword_quality_check(repaired, base_text, source="github")
                if repaired_ok:
                    items = repaired
                else:
                    items = synthesize_keywords_from_context(base_text, source="github", max_items=10)
            if not items:
                items = synthesize_keywords_from_context(base_text, source="github", max_items=10)
            return ", ".join(dict.fromkeys(items))
        except Exception as e:
            print(f"关键词生成失败 {self.slug}: {e}")
            fallback = synthesize_keywords_from_context(base_text, source="github", max_items=10)
            return ", ".join(fallback)

    def to_content_item(self, rank: int, date_str: str) -> dict:
        merged = f"{self.display_name} {self.description_en} {self.keywords}".lower()
        hit_keywords = [kw for kw in AI_KEYWORDS if kw in merged]

        latest_version = str(self.latest_version.get("version", "")).strip()
        tag_list = ["clawhub-skill"]
        if latest_version:
            tag_list.append(f"v{latest_version}")

        return {
            "id": build_item_id("ch", date_str, rank),
            "source": "clawhub",
            "date": date_str,
            "rank": rank,
            "title": self.display_name,
            "url": self.url,
            "detail_url": self.detail_url,
            "description_en": self.description_en,
            "description_zh": self.description_zh,
            "keywords": [k.strip() for k in self.keywords.split(",") if k.strip()],
            "tags": tag_list,
            "metrics": {
                "stars": int(self.stats.get("stars") or 0),
                "downloads": int(self.stats.get("downloads") or 0),
                "installs_all_time": int(self.stats.get("installsAllTime") or 0),
                "installs_current": int(self.stats.get("installsCurrent") or 0),
                "comments": int(self.stats.get("comments") or 0),
                "versions": int(self.stats.get("versions") or 0),
                "owner_handle": str(self.owner.get("handle", "")).strip(),
                "owner_name": str(self.owner.get("displayName", "")).strip(),
            },
            "media": {"image": None},
            "ai_flags": {"is_ai": True, "hit_keywords": hit_keywords, "hit_excludes": []},
            "score": self.score,
            "raw": {
                "slug": self.slug,
                "created_at": _ms_to_iso(self.created_at_ms),
                "updated_at": _ms_to_iso(self.updated_at_ms),
                "latest_version": self.latest_version,
                "owner": self.owner,
                "moderation": self.moderation,
            },
        }

    def to_markdown(self, rank: int) -> str:
        latest_version = str(self.latest_version.get("version", "")).strip() or "-"
        return f"""## [{rank}. {self.display_name}]({self.url})

**Slug**: `{self.slug}`  
**Version**: {latest_version}  
**Stats**: ⭐ {int(self.stats.get('stars') or 0)} | ⬇️ {int(self.stats.get('downloads') or 0)} | 🧩 {int(self.stats.get('versions') or 0)}

**原始简介**: {self.summary_en}

**中文介绍**: {self.description_zh}

**关键词**: {self.keywords}

**评分**: {self.score.get('total', 0)}

**详情地址**: [ClawHub API]({self.detail_url})

---

"""


def _enrich_skills(base_url: str, rows: List[dict]) -> List[ClawHubSkill]:
    skills: List[ClawHubSkill] = []
    total = len(rows)
    for idx, row in enumerate(rows, start=1):
        slug = str(row.get("slug", "")).strip()
        if not slug:
            continue
        print(f"处理 skill [{idx}/{total}]: {slug}")
        detail = _fetch_skill_detail(base_url, slug)
        merged = dict(row)
        if isinstance(detail.get("latestVersion"), dict):
            merged["latestVersion"] = detail["latestVersion"]
        if isinstance(detail.get("owner"), dict):
            merged["owner"] = detail["owner"]
        if "moderation" in detail:
            merged["moderation"] = detail.get("moderation")
        if isinstance(detail.get("skill"), dict):
            # Use skill-level fields as source of truth when available.
            skill_obj = detail["skill"]
            for key in ("slug", "displayName", "summary", "tags", "stats", "createdAt", "updatedAt"):
                if key in skill_obj:
                    merged[key] = skill_obj[key]
        try:
            skills.append(ClawHubSkill(base_url=base_url, data=merged))
        except Exception as e:
            print(f"构建 skill 失败 {slug}: {e}")
            continue
    return skills


def generate_markdown(skills: List[ClawHubSkill], date_str: str):
    markdown_content = f"# ClawHub Skills Daily | {date_str}\n\n"
    markdown_content += f"> 共 {len(skills)} 个 skills\n\n"

    structured_items: List[dict] = []
    rank = 1
    for skill in skills:
        markdown_content += skill.to_markdown(rank)
        structured_items.append(skill.to_content_item(rank, date_str))
        rank += 1

    os.makedirs("data/clawhub", exist_ok=True)
    file_name = f"data/clawhub/clawhub-daily-{date_str}.md"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    print(f"文件 {file_name} 生成成功。")

    save_structured_items(date_str, structured_items)


def main():
    tz_name = _get_tz_name()
    tz = pytz.timezone(tz_name)
    target_date = os.getenv("CLAWHUB_TARGET_DATE", "").strip()
    output_date = os.getenv("CLAWHUB_OUTPUT_DATE", "").strip()

    if not target_date:
        target_date = datetime.now(tz).strftime("%Y-%m-%d")
    if not output_date:
        output_date = target_date

    print("=== ClawHub 抓取开始 ===")
    print(f"API Base: {_get_base_url()}")
    print(f"抓取日期: {target_date} ({tz_name})")
    print(f"写入日期: {output_date}")

    rows = fetch_updated_skills(target_date=target_date)
    print(f"拉取到 {len(rows)} 条 skills")

    skills = _enrich_skills(_get_base_url(), rows)
    print(f"处理完成 {len(skills)} 条 skills")

    generate_markdown(skills, output_date)
    print("=== ClawHub 抓取完成 ===")


if __name__ == "__main__":
    main()
