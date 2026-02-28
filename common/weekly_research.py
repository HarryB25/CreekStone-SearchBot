from __future__ import annotations

import json
import math
import os
import re
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Iterable

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

from common.openai_fallback import chat_completion_content, get_openai_timeout

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover
    from backports.zoneinfo import ZoneInfo  # type: ignore


BASE_DIR = Path(__file__).resolve().parent.parent
STRUCTURED_DIR = BASE_DIR / "data" / "structured"
INSIGHTS_WEEKLY_DIR = BASE_DIR / "data" / "insights" / "weekly"

TERM_CANONICAL_MAP = {
    "llms": "llm",
    "large language model": "llm",
    "large language models": "llm",
    "大语言模型": "llm",
    "大型语言模型": "llm",
    "rag pipeline": "rag",
    "retrieval augmented generation": "rag",
    "检索增强生成": "rag",
    "agents": "agent",
    "智能体": "agent",
    "代理": "agent",
    "autonomous agents": "agent",
    "tool use": "tool-use",
    "tool using": "tool-use",
    "multi agent": "multi-agent",
    "multi-agent": "multi-agent",
    "多智能体": "multi-agent",
    "multi agents": "multi-agent",
}

TERM_BLACKLIST = {
    "ai",
    "artificial intelligence",
    "machine learning",
    "deep learning",
    "ml",
    "tool",
    "platform",
    "product",
    "solution",
    "app",
    "agent",
    "llm",
    "rag",
    "应用",
    "产品",
    "系统",
    "模型",
    "方案",
    "工具",
    "feature",
    "features",
    "github",
    "arxiv",
    "product hunt",
    "clawhub",
    "clawhub-skill",
    "paper",
    "research",
}

EN_STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "in",
    "into",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "their",
    "this",
    "to",
    "with",
    "your",
    "you",
    "we",
    "our",
    "want",
    "all",
    "can",
}

EN_DOMAIN_CUES = {
    "agent",
    "workflow",
    "browser",
    "proxy",
    "vector",
    "retrieval",
    "memory",
    "observability",
    "monitoring",
    "security",
    "privacy",
    "debug",
    "debugging",
    "repair",
    "diff",
    "sdk",
    "api",
    "cli",
    "mcp",
    "database",
    "embedding",
    "search",
    "transcription",
    "speech",
    "voice",
    "ocr",
    "automation",
    "orchestration",
    "inference",
    "kubernetes",
    "docker",
    "gpu",
    "meeting",
    "notes",
    "coding",
    "copilot",
    "prompt",
    "planner",
    "planning",
}

CN_GENERIC = {"平台", "系统", "模型", "能力", "功能", "工具", "方案", "服务", "项目", "产品"}
EN_PHRASE_RE = re.compile(r"[A-Za-z][A-Za-z0-9+#\-/]{1,31}")
CN_PHRASE_RE = re.compile(
    r"([\u4e00-\u9fff]{2,8}(?:工作流|自动化|编排|修复|调试|分析|生成|检索|搜索|代理|智能体|数据库|引擎|框架|安全|隐私|监控|语音|图像|视频|笔记|转写|规划|协同|翻译|摘要|识别))"
)
WEEKLY_DEFAULT_LOOKBACK = 8
WEEKLY_DEFAULT_TERM_TOPK = 300
WEEKLY_DEFAULT_PROJECT_TOPK = 120


@dataclass(frozen=True)
class WeekWindow:
    week_start: date
    week_end: date
    baseline_start: date
    baseline_end: date


def _get_int_env(name: str, default: int) -> int:
    raw = os.getenv(name, "").strip()
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def _get_str_env(name: str, default: str) -> str:
    raw = os.getenv(name, "").strip()
    return raw or default


def _safe_float(value: Any, default: float = 0.0) -> float:
    try:
        if value is None:
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def _sigmoid(value: float) -> float:
    clipped = max(-12.0, min(12.0, value))
    return 1.0 / (1.0 + math.exp(-clipped))


def _ema(values: list[float], alpha: float = 0.4) -> float:
    if not values:
        return 0.0
    acc = values[0]
    for value in values[1:]:
        acc = alpha * value + (1.0 - alpha) * acc
    return acc


def _zscore(series: pd.Series) -> pd.Series:
    if series.empty:
        return pd.Series(dtype=float)
    mean = float(series.mean())
    std = float(series.std(ddof=0))
    if std <= 1e-9:
        return pd.Series([0.0] * len(series), index=series.index)
    return ((series - mean) / std).clip(-3.0, 3.0)


def load_structured_items() -> pd.DataFrame:
    files = sorted(STRUCTURED_DIR.glob("*.parquet"))
    dfs: list[pd.DataFrame] = []
    for path in files:
        try:
            dfs.append(pd.read_parquet(path))
        except Exception:
            continue
    if dfs:
        df = pd.concat(dfs, ignore_index=True)
        if "id" in df.columns:
            df = df.drop_duplicates(subset=["id"], keep="last")
        return df

    nd_path = STRUCTURED_DIR / "items.ndjson"
    if not nd_path.exists():
        return pd.DataFrame()

    rows = []
    for line in nd_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except Exception:
            continue
    return pd.DataFrame(rows)


def resolve_week_window(week_start_str: str | None = None, timezone_name: str | None = None) -> WeekWindow:
    tz_name = timezone_name or _get_str_env("WEEKLY_REPORT_TIMEZONE", "Asia/Singapore")
    tz = ZoneInfo(tz_name)
    lookback_weeks = max(1, _get_int_env("WEEKLY_REPORT_LOOKBACK_WEEKS", WEEKLY_DEFAULT_LOOKBACK))

    if week_start_str:
        target = datetime.strptime(week_start_str, "%Y-%m-%d").date()
    else:
        now_local = datetime.now(tz).date()
        current_week_start = now_local - timedelta(days=now_local.weekday())
        target = current_week_start - timedelta(days=7)

    aligned_start = target - timedelta(days=target.weekday())
    aligned_end = aligned_start + timedelta(days=6)
    baseline_end = aligned_start - timedelta(days=1)
    baseline_start = aligned_start - timedelta(days=lookback_weeks * 7)

    return WeekWindow(
        week_start=aligned_start,
        week_end=aligned_end,
        baseline_start=baseline_start,
        baseline_end=baseline_end,
    )


def _normalize_keywords(value: Any) -> list[str]:
    if isinstance(value, (list, tuple, set)):
        raw = list(value)
    elif hasattr(value, "tolist"):
        try:
            raw = list(value.tolist())
        except Exception:
            raw = []
    elif isinstance(value, str):
        raw = [part.strip() for part in value.replace("，", ",").split(",") if part.strip()]
    else:
        raw = []

    out: list[str] = []
    seen = set()
    for item in raw:
        term = str(item).strip()
        if not term:
            continue
        if term.startswith("关键词：") or term.startswith("关键字："):
            term = term.split("：", 1)[1].strip()
        if not term:
            continue
        key = canonical_term(term)
        if not key or key in seen:
            continue
        seen.add(key)
        out.append(key)
    return out


def _normalize_list(value: Any) -> list[Any]:
    if isinstance(value, (list, tuple, set)):
        return list(value)
    if hasattr(value, "tolist"):
        try:
            return list(value.tolist())
        except Exception:
            return []
    if value in (None, ""):
        return []
    return [value]


def canonical_term(term: str) -> str:
    text = " ".join(str(term).strip().replace("_", " ").split())
    if not text:
        return ""
    tokens = text.split()
    if len(tokens) > 1:
        collapsed = [tokens[0]]
        for token in tokens[1:]:
            if token.lower() == collapsed[-1].lower():
                continue
            collapsed.append(token)
        text = " ".join(collapsed)
    low = text.lower()
    if low in TERM_CANONICAL_MAP:
        return TERM_CANONICAL_MAP[low]
    if low.endswith("s") and low[:-1] in TERM_CANONICAL_MAP:
        return TERM_CANONICAL_MAP[low[:-1]]
    return low


def _clean_summary(row: dict[str, Any]) -> str:
    summary = str(row.get("description_zh") or row.get("description_en") or "").strip()
    return summary


def _extra_raw_context(raw: Any) -> str:
    if not isinstance(raw, dict):
        return ""
    parts = []
    preferred_keys = ("readme_summary_zh", "translated_description")
    for key in preferred_keys:
        value = raw.get(key)
        if value:
            parts.append(str(value).strip())
    if not parts:
        value = raw.get("readme_excerpt")
        if value:
            parts.append(str(value).strip()[:900])
    ai_summary = raw.get("ai_summary")
    if isinstance(ai_summary, dict):
        for key in ("tldr", "motivation", "method", "conclusion"):
            value = ai_summary.get(key)
            if value:
                parts.append(str(value).strip())
    return "\n".join([part for part in parts if part])[:1800]


def _build_text_blob(row: dict[str, Any], summary: str, keywords: list[str]) -> str:
    tags = _normalize_list(row.get("tags"))
    tag_text = " ".join([str(tag).strip() for tag in tags if str(tag).strip()])
    kw_text = " ".join(keywords)
    extra = _extra_raw_context(row.get("raw"))
    parts = [str(row.get("title", "")).strip(), summary, kw_text, tag_text, extra]
    return "\n".join([part for part in parts if part])[:6000]


def _source_weight_base(source: str) -> float:
    return {
        "producthunt": 1.0,
        "github": 1.0,
        "arxiv": 0.9,
        "clawhub": 0.95,
    }.get(source, 1.0)


def _build_signals(row: dict[str, Any]) -> dict[str, Any]:
    source = str(row.get("source", "")).lower()
    metrics = row.get("metrics") if isinstance(row.get("metrics"), dict) else {}
    tags = _normalize_list(row.get("tags"))

    if source == "producthunt":
        featured = 1 if str(metrics.get("featured", "")).strip() == "是" else 0
        return {
            "upvotes": int(_safe_float(metrics.get("votes"), 0)),
            "rank": int(_safe_float(row.get("rank"), 0)),
            "featured": featured,
            "category": str(tags[0]).strip() if tags else "",
        }
    if source == "github":
        return {
            "stars_today": int(_safe_float(metrics.get("stars_today"), 0)),
            "stars_total": int(_safe_float(metrics.get("stars"), 0)),
            "forks": int(_safe_float(metrics.get("forks"), 0)),
            "language": str(tags[0]).strip() if tags else "",
        }
    if source == "arxiv":
        authors = metrics.get("authors") if isinstance(metrics.get("authors"), list) else []
        return {
            "rank": int(_safe_float(row.get("rank"), 0)),
            "primary_category": str(tags[0]).strip() if tags else "",
            "authors_count": len(authors),
            "pdf_link": str(row.get("detail_url", "")).strip(),
        }
    if source == "clawhub":
        return {
            "downloads": int(_safe_float(metrics.get("downloads"), 0)),
            "stars": int(_safe_float(metrics.get("stars"), 0)),
            "installs_current": int(_safe_float(metrics.get("installs_current"), 0)),
            "installs_all_time": int(_safe_float(metrics.get("installs_all_time"), 0)),
            "comments": int(_safe_float(metrics.get("comments"), 0)),
            "versions": int(_safe_float(metrics.get("versions"), 0)),
        }
    return {}


def build_event_frame(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()

    rows: list[dict[str, Any]] = []
    for _, item in df.iterrows():
        row = item.to_dict() if hasattr(item, "to_dict") else dict(item)
        source = str(row.get("source", "")).lower().strip()
        item_id = str(row.get("id", "")).strip()
        title = str(row.get("title", "")).strip()
        date_raw = str(row.get("date", "")).strip()
        if not source or not item_id or not title or not date_raw:
            continue
        try:
            item_date = datetime.strptime(date_raw, "%Y-%m-%d").date()
        except ValueError:
            continue

        summary = _clean_summary(row)
        keywords = _normalize_keywords(row.get("keywords"))
        signals = _build_signals(row)
        score_obj = row.get("score") if isinstance(row.get("score"), dict) else {}
        score_total = int(_safe_float(score_obj.get("total"), 0))
        rows.append(
            {
                "source": source,
                "date": item_date,
                "date_str": date_raw,
                "id": item_id,
                "stable_key": f"{source}::{title.lower()}",
                "title": title,
                "summary": summary,
                "url": str(row.get("url", "")).strip(),
                "text_blob": _build_text_blob(row, summary, keywords),
                "signals": signals,
                "keywords_norm": keywords,
                "score_total": score_total,
                "source_weight_base": _source_weight_base(source),
            }
        )

    events = pd.DataFrame(rows)
    if events.empty:
        return events
    events = events.sort_values(["date", "source", "title"], ascending=[True, True, True]).reset_index(drop=True)
    return events


def _tokenize_english_phrases(text: str) -> list[str]:
    words = [match.group(0).lower() for match in EN_PHRASE_RE.finditer(text or "")]
    cleaned = []
    for token in words:
        if token in EN_STOPWORDS or token in TERM_BLACKLIST:
            continue
        if len(token) <= 2 and token not in {"llm", "rag", "api", "sdk"}:
            continue
        cleaned.append(token)

    phrases: list[str] = []
    for idx, token in enumerate(cleaned):
        for size in (1, 2, 3):
            chunk = cleaned[idx : idx + size]
            if len(chunk) != size:
                continue
            if chunk[0] in EN_STOPWORDS or chunk[-1] in EN_STOPWORDS:
                continue
            if any(part in EN_STOPWORDS for part in chunk):
                continue
            if any(part in {"something", "anything", "everything", "together"} for part in chunk):
                continue
            if size == 1 and chunk[0] not in EN_DOMAIN_CUES:
                continue
            if size > 1 and not any(part in EN_DOMAIN_CUES for part in chunk):
                continue
            phrase = " ".join(chunk)
            if len(phrase) > 32:
                continue
            phrases.append(phrase)
    return phrases


def _tokenize_chinese_phrases(text: str) -> list[str]:
    return [match.group(1).strip() for match in CN_PHRASE_RE.finditer(text or "")]


def extract_terms_for_event(row: pd.Series) -> set[str]:
    keywords = set(row.get("keywords_norm", []) or [])
    text_blob = str(row.get("text_blob", "") or "")

    terms = set(keywords)
    for phrase in _tokenize_english_phrases(text_blob):
        canon = canonical_term(phrase)
        if not canon:
            continue
        if canon in TERM_BLACKLIST:
            continue
        if any(part in TERM_BLACKLIST for part in canon.split()):
            continue
        if len(canon.split()) == 1 and canon in {"agent", "llm", "rag"}:
            continue
        terms.add(canon)

    for phrase in _tokenize_chinese_phrases(text_blob):
        canon = canonical_term(phrase)
        if not canon:
            continue
        if canon in CN_GENERIC or canon in TERM_BLACKLIST:
            continue
        terms.add(canon)

    title_tokens = {canonical_term(token.group(0)) for token in EN_PHRASE_RE.finditer(str(row.get("title", "")))}
    out = set()
    for term in terms:
        if not term:
            continue
        if term in TERM_BLACKLIST:
            continue
        if len(term) <= 1:
            continue
        if len(term.split()) == 1 and term in title_tokens and term not in keywords:
            continue
        if term in {"agent", "llm", "rag", "api"} and term not in keywords:
            continue
        out.add(term)
    return out


def add_term_sets(events: pd.DataFrame) -> pd.DataFrame:
    if events.empty:
        return events
    frame = events.copy()
    frame["term_set"] = frame.apply(extract_terms_for_event, axis=1)
    return frame


def _category_bonus(category: str) -> float:
    return {
        "cs.ai": 0.20,
        "cs.lg": 0.18,
        "cs.cl": 0.15,
        "cs.cv": 0.15,
    }.get((category or "").lower(), 0.0)


def compute_project_scores(events: pd.DataFrame) -> pd.DataFrame:
    if events.empty:
        return events

    frame = events.copy()
    raw_hot_values: list[float] = []
    for _, row in frame.iterrows():
        signals = row["signals"] if isinstance(row["signals"], dict) else {}
        source = str(row["source"])
        if source == "producthunt":
            raw_hot = (
                math.log1p(_safe_float(signals.get("upvotes"), 0.0))
                + 0.6 * _safe_float(signals.get("featured"), 0.0)
                - 0.04 * _safe_float(signals.get("rank"), 0.0)
            )
        elif source == "github":
            raw_hot = math.log1p(
                3.0 * _safe_float(signals.get("stars_today"), 0.0)
                + 0.2 * _safe_float(signals.get("forks"), 0.0)
                + 0.02 * _safe_float(signals.get("stars_total"), 0.0)
            )
        elif source == "arxiv":
            raw_hot = 1.2 - 0.04 * _safe_float(signals.get("rank"), 0.0) + _category_bonus(
                str(signals.get("primary_category", ""))
            )
        elif source == "clawhub":
            raw_hot = math.log1p(
                _safe_float(signals.get("downloads"), 0.0)
                + 2.0 * _safe_float(signals.get("stars"), 0.0)
                + 0.5 * _safe_float(signals.get("installs_current"), 0.0)
                + 0.2 * _safe_float(signals.get("comments"), 0.0)
            )
        else:
            raw_hot = 0.0
        raw_hot_values.append(raw_hot)

    frame["raw_hot"] = raw_hot_values
    frame["hot"] = 0.0
    for source, idx in frame.groupby("source").groups.items():
        sub = frame.loc[idx, "raw_hot"]
        frame.loc[idx, "hot"] = _zscore(sub)

    hot_min = float(frame["hot"].min()) if not frame.empty else 0.0
    hot_max = float(frame["hot"].max()) if not frame.empty else 0.0
    hot_span = hot_max - hot_min if abs(hot_max - hot_min) > 1e-9 else 1.0
    frame["hot_norm"] = frame["hot"].apply(lambda x: max(0.0, min(1.0, (float(x) - hot_min) / hot_span)))
    frame["quality_weight"] = (
        0.6 * frame["hot_norm"] + 0.4 * frame["score_total"].apply(lambda x: max(0.0, min(1.0, _safe_float(x) / 100.0)))
    )
    return frame


def _iter_week_starts(window: WeekWindow) -> list[date]:
    weeks = []
    cur = window.baseline_start
    while cur <= window.week_start:
        weeks.append(cur)
        cur = cur + timedelta(days=7)
    return weeks


def _week_bucket(item_date: date) -> date:
    return item_date - timedelta(days=item_date.weekday())


def compute_project_trends(events: pd.DataFrame, window: WeekWindow) -> dict[str, Any]:
    if events.empty:
        return {
            "events": events,
            "week_events": events,
            "rising_top": [],
            "hot_top": [],
            "novel_top": [],
            "project_metrics": {},
        }

    frame = compute_project_scores(events)
    frame["week_start"] = frame["date"].apply(_week_bucket)
    week_events = frame[(frame["date"] >= window.week_start) & (frame["date"] <= window.week_end)].copy()

    rise_map: dict[str, float] = {}
    novel_map: dict[str, bool] = {}
    grouped_history = frame.groupby("stable_key")
    for stable_key, sub in grouped_history:
        sub = sub.sort_values("week_start")
        week_rows = sub[sub["week_start"] == window.week_start]
        if week_rows.empty:
            continue
        current_hot = float(week_rows["hot"].mean())
        history_rows = sub[sub["week_start"] < window.week_start]
        history_values = history_rows.groupby("week_start")["hot"].mean().tolist()
        if history_values:
            rise = current_hot - _ema(history_values, alpha=0.4)
            novel = False
        else:
            rise = current_hot * 0.8
            novel = True
        rise_map[stable_key] = rise
        novel_map[stable_key] = novel

    week_events["rise"] = week_events["stable_key"].map(rise_map).fillna(0.0)
    week_events["novel_candidate"] = week_events["stable_key"].map(novel_map).fillna(False)
    week_events["composite"] = 0.55 * week_events["hot"] + 0.45 * week_events["rise"]

    def _records(sub: pd.DataFrame, sort_col: str, limit: int = 20) -> list[dict[str, Any]]:
        data = sub.sort_values(sort_col, ascending=False).head(limit)
        rows = []
        for _, row in data.iterrows():
            rows.append(
                {
                    "id": row["id"],
                    "source": row["source"],
                    "date": row["date"].isoformat(),
                    "title": row["title"],
                    "url": row["url"],
                    "hot": round(float(row["hot"]), 4),
                    "rise": round(float(row["rise"]), 4),
                    "score_total": int(row["score_total"]),
                    "quality_weight": round(float(row["quality_weight"]), 4),
                }
            )
        return rows

    novel_cutoff: dict[str, float] = {}
    for source, sub in week_events.groupby("source"):
        novel_cutoff[source] = float(sub["hot"].median()) if not sub.empty else 0.0
    novel_rows = week_events[
        week_events.apply(
            lambda r: bool(r["novel_candidate"]) and float(r["hot"]) >= novel_cutoff.get(str(r["source"]), 0.0),
            axis=1,
        )
    ]

    project_metrics = {
        row["id"]: {
            "hot": round(float(row["hot"]), 4),
            "rise": round(float(row["rise"]), 4),
            "quality_weight": round(float(row["quality_weight"]), 4),
        }
        for _, row in week_events.iterrows()
    }

    return {
        "events": frame,
        "week_events": week_events,
        "rising_top": _records(week_events, "rise"),
        "hot_top": _records(week_events, "hot"),
        "novel_top": _records(novel_rows, "hot"),
        "project_metrics": project_metrics,
    }


def compute_term_trends(events_with_scores: pd.DataFrame, window: WeekWindow) -> dict[str, Any]:
    if events_with_scores.empty:
        return {"terms": [], "cooling_terms": [], "term_to_items": {}}

    term_rows: list[dict[str, Any]] = []
    all_weeks = _iter_week_starts(window)
    baseline_weeks = [week for week in all_weeks if week < window.week_start]

    for _, row in events_with_scores.iterrows():
        for term in row.get("term_set", set()) or set():
            term_rows.append(
                {
                    "term": term,
                    "week_start": row["week_start"],
                    "source": row["source"],
                    "item_id": row["id"],
                    "quality_weight": float(row["quality_weight"]),
                }
            )

    if not term_rows:
        return {"terms": [], "cooling_terms": [], "term_to_items": {}}

    term_df = pd.DataFrame(term_rows)
    term_to_items = (
        term_df.groupby("term")["item_id"].apply(lambda x: sorted(set(x.tolist()))).to_dict()
    )

    min_support = max(1, _get_int_env("WEEKLY_REPORT_MIN_TERM_SUPPORT", 3))
    top_k = max(20, _get_int_env("WEEKLY_REPORT_TERM_TOPK", WEEKLY_DEFAULT_TERM_TOPK))

    candidates: list[dict[str, Any]] = []
    cooling: list[dict[str, Any]] = []

    for term, sub in term_df.groupby("term"):
        week_group = sub.groupby("week_start")["item_id"].nunique().to_dict()
        freq_week = int(week_group.get(window.week_start, 0))
        if freq_week <= 0:
            continue

        support_items = sorted(set(sub[sub["week_start"] == window.week_start]["item_id"].tolist()))
        support_projects = len(support_items)
        support_sources = len(set(sub[sub["week_start"] == window.week_start]["source"].tolist()))
        if freq_week < min_support and support_projects < min_support:
            continue
        if support_sources < 1:
            continue

        baseline_values = [float(week_group.get(week, 0)) for week in baseline_weeks]
        freq_baseline = _ema(baseline_values, alpha=0.4) if baseline_values else 0.0
        burst = (freq_week + 1.0) / (freq_baseline + 1.0)
        log_burst = math.log(burst)

        weeks_with_term = len([week for week, count in week_group.items() if count > 0])
        total_weeks = max(1, len(all_weeks))
        idf_like = math.log((total_weeks + 1.0) / (weeks_with_term + 1.0)) + 1.0

        first_seen = min(week_group.keys())
        weeks_since_first = max(0, (window.week_start - first_seen).days // 7)
        novelty = 1.0 + min(0.35, 0.05 * min(7, weeks_since_first))

        week_quality = float(sub[sub["week_start"] == window.week_start]["quality_weight"].mean())
        baseline_quality = float(sub[sub["week_start"] < window.week_start]["quality_weight"].mean()) if not sub[sub["week_start"] < window.week_start].empty else week_quality

        cross_source_bonus = 1.0 + 0.15 * max(0, support_sources - 1)
        if week_quality < 0.15:
            continue

        score = max(log_burst, 0.0) * idf_like * week_quality * novelty * cross_source_bonus
        cooling_score = max(-log_burst, 0.0) * idf_like * max(0.05, baseline_quality)

        payload = {
            "term": term,
            "term_trend_score": round(float(score), 6),
            "freq_week": freq_week,
            "freq_baseline": round(float(freq_baseline), 4),
            "support_projects": support_projects,
            "support_sources": support_sources,
            "idf_like": round(float(idf_like), 4),
            "novelty": round(float(novelty), 4),
            "quality_weight": round(float(week_quality), 4),
            "support_items": support_items,
        }
        if score > 0:
            candidates.append(payload)
        if cooling_score > 0:
            cooling.append(
                {
                    **payload,
                    "cooling_score": round(float(cooling_score), 6),
                }
            )

    candidates.sort(key=lambda x: (x["term_trend_score"], x["support_projects"], x["support_sources"]), reverse=True)
    cooling.sort(key=lambda x: (x["cooling_score"], x["support_projects"]), reverse=True)
    return {
        "terms": candidates[:top_k],
        "cooling_terms": cooling[: min(60, top_k)],
        "term_to_items": term_to_items,
    }


def build_embedding_text(row: pd.Series) -> str:
    signals = row.get("signals", {}) if isinstance(row.get("signals"), dict) else {}
    signal_bits = []
    for key in ("upvotes", "stars_today", "stars_total", "downloads", "rank", "primary_category", "language"):
        value = signals.get(key)
        if value not in (None, "", 0):
            signal_bits.append(f"{key}={value}")
    keywords = " ".join((row.get("keywords_norm", []) or [])[:8])
    parts = [
        str(row.get("title", "")),
        str(row.get("summary", "")),
        keywords,
        " ".join(signal_bits),
    ]
    return "\n".join([part for part in parts if part])[:3500]


def select_candidate_projects(
    week_events: pd.DataFrame,
    term_trends: list[dict[str, Any]],
    term_to_items: dict[str, list[str]],
) -> pd.DataFrame:
    if week_events.empty:
        return week_events

    limit = max(20, _get_int_env("WEEKLY_REPORT_PROJECT_TOPK", WEEKLY_DEFAULT_PROJECT_TOPK))
    hot_ids = week_events.sort_values("hot", ascending=False)["id"].head(limit).tolist()

    selected_ids = set(hot_ids)
    for term in term_trends[:80]:
        for item_id in term_to_items.get(str(term.get("term", "")), [])[:10]:
            selected_ids.add(item_id)
            if len(selected_ids) >= limit:
                break
        if len(selected_ids) >= limit:
            break

    selected = week_events[week_events["id"].isin(selected_ids)].copy()
    return selected.sort_values(["composite", "hot"], ascending=[False, False]).head(limit)


def embed_texts(client: Any, texts: list[str], model: str) -> list[list[float]]:
    if not texts:
        return []
    try:
        response = client.embeddings.create(model=model, input=texts)
    except Exception as exc:
        raise RuntimeError(f"embedding request failed: {exc}") from exc

    data = getattr(response, "data", None)
    if not data:
        raise RuntimeError("embedding response missing data")
    vectors = [list(item.embedding) for item in data]
    if len(vectors) != len(texts):
        raise RuntimeError("embedding vector count mismatch")
    return vectors


def cluster_projects(
    candidate_projects: pd.DataFrame,
    embeddings: list[list[float]],
    term_trends: list[dict[str, Any]],
    target_theme_count: int | None = None,
) -> dict[str, Any]:
    if candidate_projects.empty:
        return {"k_selected": 0, "clusters": [], "semantic_map": [], "silhouette_score": None}
    if len(embeddings) != len(candidate_projects):
        raise RuntimeError("cluster input mismatch between projects and embeddings")

    n = len(candidate_projects)
    if n < 3:
        return {"k_selected": 1, "clusters": [], "semantic_map": [], "silhouette_score": None}

    if n < 12:
        candidate_ks = [max(2, n // 3)]
    else:
        candidate_ks = [k for k in range(4, min(10, n - 1) + 1)]

    best_k = candidate_ks[0]
    best_score = -1.0
    best_labels: list[int] | None = None

    for k in candidate_ks:
        if k >= n:
            continue
        model = KMeans(n_clusters=k, random_state=42, n_init=20)
        labels = model.fit_predict(embeddings)
        unique_labels = len(set(labels.tolist()))
        if unique_labels <= 1:
            score = -1.0
        else:
            score = float(silhouette_score(embeddings, labels))
        if score > best_score:
            best_score = score
            best_k = k
            best_labels = labels.tolist()

    if best_labels is None:
        raise RuntimeError("failed to cluster candidate projects")

    frame = candidate_projects.copy()
    frame["cluster_id"] = best_labels

    pca = PCA(n_components=2, random_state=42)
    reduced = pca.fit_transform(embeddings)
    frame["semantic_x"] = [float(point[0]) for point in reduced]
    frame["semantic_y"] = [float(point[1]) for point in reduced]
    semantic_map = []
    for _, row in frame.iterrows():
        semantic_map.append(
            {
                "id": row["id"],
                "title": row["title"],
                "source": row["source"],
                "cluster_id": int(row["cluster_id"]),
                "x": round(float(row["semantic_x"]), 6),
                "y": round(float(row["semantic_y"]), 6),
                "hot": round(float(row["hot"]), 4),
                "rise": round(float(row["rise"]), 4),
                "score_total": int(row["score_total"]),
            }
        )

    term_score_map = {str(item["term"]): float(item["term_trend_score"]) for item in term_trends}
    clusters: list[dict[str, Any]] = []
    for cluster_id, sub in frame.groupby("cluster_id"):
        if len(sub) < max(3, _get_int_env("WEEKLY_REPORT_THEME_MIN_SIZE", 3)):
            continue
        if int((sub["hot"] > 0).sum()) < 2:
            continue

        member_ids = sub["id"].tolist()
        source_mix = sorted(set(sub["source"].tolist()))
        term_counter: dict[str, float] = {}
        for _, row in sub.iterrows():
            for term in row.get("term_set", set()) or set():
                term_counter[term] = term_counter.get(term, 0.0) + term_score_map.get(term, 0.0)
        top_terms = [term for term, _ in sorted(term_counter.items(), key=lambda kv: kv[1], reverse=True)[:10]]

        top_projects = []
        for _, row in sub.sort_values(["composite", "hot"], ascending=[False, False]).head(5).iterrows():
            top_projects.append(
                {
                    "id": row["id"],
                    "title": row["title"],
                    "source": row["source"],
                    "url": row["url"],
                    "summary": row["summary"],
                    "hot": round(float(row["hot"]), 4),
                    "rise": round(float(row["rise"]), 4),
                    "score_total": int(row["score_total"]),
                }
            )

        source_diversity_bonus = 1.0 + 0.1 * max(0, len(source_mix) - 1)
        term_signal_bonus = 1.0 + min(0.4, 0.02 * len(top_terms))
        cluster_score = float(sub["composite"].mean()) * source_diversity_bonus * term_signal_bonus
        if cluster_score <= 0:
            continue

        clusters.append(
            {
                "cluster_id": int(cluster_id),
                "member_project_ids": member_ids,
                "member_count": len(member_ids),
                "top_projects": top_projects,
                "top_terms": top_terms,
                "source_mix": source_mix,
                "cluster_score": round(cluster_score, 6),
                "centroid": {
                    "x": round(float(sub["semantic_x"].mean()), 6),
                    "y": round(float(sub["semantic_y"].mean()), 6),
                },
            }
        )

    clusters.sort(key=lambda item: float(item["cluster_score"]), reverse=True)
    target_theme_count = (
        max(4, int(target_theme_count))
        if target_theme_count is not None
        else max(4, _get_int_env("WEEKLY_REPORT_THEME_TARGET", 10))
    )
    return {
        "k_selected": best_k if best_score >= 0.08 else min(best_k, 4),
        "clusters": clusters[:target_theme_count],
        "semantic_map": semantic_map,
        "silhouette_score": round(float(best_score), 6),
    }


def _theme_card_messages(cluster: dict[str, Any]) -> list[dict[str, str]]:
    project_lines = []
    for project in cluster.get("top_projects", []):
        project_lines.append(
            f"- [{project['source']}:{project['id']}] {project['title']} | hot={project['hot']} | rise={project['rise']} | score={project['score_total']}\n"
            f"  summary: {project['summary']}"
        )
    user = (
        "你是 AI 趋势研究员。请基于给定的聚类证据生成主题卡片。"
        "所有结论必须来自输入，不允许编造新数据或新项目。"
        "输出 JSON，不要 markdown。\n\n"
        f"top_terms: {cluster.get('top_terms', [])}\n"
        f"source_mix: {cluster.get('source_mix', [])}\n"
        f"cluster_score: {cluster.get('cluster_score')}\n"
        "representative_projects:\n"
        + "\n".join(project_lines)
        + "\n\n输出格式:\n"
        "{"
        '"theme_title":"",'
        '"one_sentence_summary":"",'
        '"why_now":"",'
        '"representative_projects":[{"id":"","title":"","url":"","positioning":""}],'
        '"key_terms":[""],'
        '"risks_questions":[""],'
        '"next_week_watchlist":[""]'
        "}"
    )
    return [
        {"role": "system", "content": "你是结构化趋势卡片生成器。"},
        {"role": "user", "content": user},
    ]


def _report_messages(payload: dict[str, Any], week_start: str, week_end: str, report_depth: str) -> list[dict[str, str]]:
    themes = payload.get("themes", [])
    keyword_boards = payload.get("keyword_boards", {})
    project_boards = payload.get("project_boards", {})
    depth_instruction = {
        "light": "写精炼版：每部分尽量短，控制在 600-900 字。",
        "standard": "写标准版：每部分适中，控制在 1200-1800 字。",
        "deep": "写深度版：对每个主题补充更完整的 why-now、代表项目对比、风险与下周观察，总长度可在 2200-3200 字。",
    }.get(report_depth, "写标准版。")
    summary = (
        "请根据以下结构化证据写一份中文周报。"
        "必须使用 6 个部分：本周摘要、趋势主题、项目榜单、关键词趋势、交叉来源观察、下周预测。"
        "每条结论后至少附一个 [source:id] 引用。"
        "禁止编造缺失数据。"
        f"{depth_instruction}\n\n"
        f"week: {week_start} ~ {week_end}\n"
        f"themes: {json.dumps(themes, ensure_ascii=False)}\n"
        f"project_boards: {json.dumps(project_boards, ensure_ascii=False)}\n"
        f"keyword_boards: {json.dumps(keyword_boards, ensure_ascii=False)}\n"
    )
    return [
        {"role": "system", "content": "你是周度科技趋势研究员，输出严谨、可追溯、克制的中文研究报告。"},
        {"role": "user", "content": summary},
    ]


def _critic_messages(payload: dict[str, Any], markdown: str) -> list[dict[str, str]]:
    user = (
        "请审校下面的周报，检查：重复主题、无证据断言、夸张措辞、把常识当趋势。"
        "如果通过，pass=true；若不通过，只返回需要修订的 summary bullets 或主题段落索引。"
        "输出 JSON。\n\n"
        f"themes: {json.dumps(payload.get('themes', []), ensure_ascii=False)}\n"
        f"report:\n{markdown[:12000]}"
    )
    return [
        {"role": "system", "content": "你是周报质检器。"},
        {"role": "user", "content": user},
    ]


def _extract_json_object(raw: str) -> dict[str, Any]:
    text = (raw or "").strip()
    if not text:
        raise ValueError("empty response")
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start >= 0 and end > start:
            return json.loads(text[start : end + 1])
        raise


def _chat_json(client: Any, messages: list[dict[str, str]], model: str) -> tuple[dict[str, Any], str]:
    content, used_model = chat_completion_content(
        client=client,
        messages=messages,
        max_tokens=1800,
        temperature=0.2,
        json_mode=True,
        default_model=model,
        timeout=get_openai_timeout(90.0),
        retry_max_tokens=2200,
    )
    return _extract_json_object(content), used_model


def _chat_markdown(client: Any, messages: list[dict[str, str]], model: str) -> tuple[str, str]:
    content, used_model = chat_completion_content(
        client=client,
        messages=messages,
        max_tokens=3200,
        temperature=0.3,
        json_mode=False,
        default_model=model,
        timeout=get_openai_timeout(120.0),
        retry_max_tokens=3600,
    )
    return content.strip(), used_model


def generate_theme_cards(clusters: list[dict[str, Any]], client: Any, chat_model: str) -> tuple[list[dict[str, Any]], set[str]]:
    themes: list[dict[str, Any]] = []
    models_used: set[str] = set()
    total = len(clusters)
    for idx, cluster in enumerate(clusters, start=1):
        print(f"[weekly] 生成主题卡片 {idx}/{total} (cluster={cluster.get('cluster_id')})")
        payload, used_model = _chat_json(client, _theme_card_messages(cluster), chat_model)
        models_used.add(used_model)
        theme = {
            "cluster_id": cluster["cluster_id"],
            "cluster_score": cluster["cluster_score"],
            "theme_title": str(payload.get("theme_title", "")).strip() or f"Theme {cluster['cluster_id']}",
            "one_sentence_summary": str(payload.get("one_sentence_summary", "")).strip(),
            "why_now": str(payload.get("why_now", "")).strip(),
            "representative_projects": payload.get("representative_projects") if isinstance(payload.get("representative_projects"), list) else cluster["top_projects"],
            "key_terms": payload.get("key_terms") if isinstance(payload.get("key_terms"), list) else cluster["top_terms"][:8],
            "risks_questions": payload.get("risks_questions") if isinstance(payload.get("risks_questions"), list) else [],
            "next_week_watchlist": payload.get("next_week_watchlist") if isinstance(payload.get("next_week_watchlist"), list) else [],
            "source_mix": cluster["source_mix"],
            "member_project_ids": cluster["member_project_ids"],
            "top_projects": cluster["top_projects"],
        }
        themes.append(theme)
    return themes, models_used


def build_cross_source_observations(themes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    observations = []
    for theme in themes:
        if len(theme.get("source_mix", [])) < 2:
            continue
        observations.append(
            {
                "theme_title": theme.get("theme_title", ""),
                "sources": theme.get("source_mix", []),
                "note": f"{theme.get('theme_title', '')} 同时出现在 {', '.join(theme.get('source_mix', []))}",
            }
        )
    return observations[:8]


def build_keyword_boards(term_result: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    terms = term_result.get("terms", [])
    cooling_terms = term_result.get("cooling_terms", [])
    emerging = [item for item in terms if float(item.get("novelty", 1.0)) > 1.05][:10]
    surging = terms[:10]
    cooling = cooling_terms[:10]
    return {
        "emerging": emerging,
        "surging": surging,
        "cooling": cooling,
    }


def build_citations(week_events: pd.DataFrame) -> dict[str, dict[str, Any]]:
    citations = {}
    for _, row in week_events.iterrows():
        citations[str(row["id"])] = {
            "source": row["source"],
            "date": row["date"].isoformat(),
            "title": row["title"],
            "url": row["url"],
        }
    return citations


def compile_markdown_report(
    themes: list[dict[str, Any]],
    project_boards: dict[str, list[dict[str, Any]]],
    keyword_boards: dict[str, list[dict[str, Any]]],
    cross_source_observations: list[dict[str, Any]],
    week_start: str,
    week_end: str,
    client: Any,
    chat_model: str,
    report_depth: str,
) -> tuple[str, dict[str, Any], set[str]]:
    report_payload = {
        "themes": themes,
        "project_boards": project_boards,
        "keyword_boards": keyword_boards,
        "cross_source_observations": cross_source_observations,
    }
    print("[weekly] 生成周报正文")
    markdown, used_model = _chat_markdown(
        client,
        _report_messages(report_payload, week_start, week_end, report_depth),
        chat_model,
    )
    print("[weekly] 执行周报审校")
    critic_json, critic_model = _chat_json(client, _critic_messages(report_payload, markdown), chat_model)
    models_used = {used_model, critic_model}
    if not bool(critic_json.get("pass", True)):
        revised_summary = critic_json.get("revised_summary")
        if isinstance(revised_summary, list) and revised_summary:
            summary_lines = "\n".join([f"- {str(line).strip()}" for line in revised_summary if str(line).strip()])
            markdown = f"## 本周摘要\n\n{summary_lines}\n\n{markdown}"
    return markdown, critic_json, models_used


def _slugify_week(week_start: date) -> str:
    iso = week_start.isocalendar()
    return f"{iso.year}-{iso.week:02d}"


def build_weekly_payload(
    *,
    events: pd.DataFrame,
    project_result: dict[str, Any],
    term_result: dict[str, Any],
    clustering: dict[str, Any],
    themes: list[dict[str, Any]],
    markdown: str,
    qa_result: dict[str, Any],
    window: WeekWindow,
    embedding_model: str,
    chat_models_used: Iterable[str],
    report_depth: str,
    semantic_map: list[dict[str, Any]],
) -> dict[str, Any]:
    week_events = project_result.get("week_events", pd.DataFrame())
    return {
        "meta": {
            "week_start": window.week_start.isoformat(),
            "week_end": window.week_end.isoformat(),
            "generated_at": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
            "lookback_weeks": max(1, _get_int_env("WEEKLY_REPORT_LOOKBACK_WEEKS", WEEKLY_DEFAULT_LOOKBACK)),
            "k_selected": clustering.get("k_selected", 0),
            "embedding_model": embedding_model,
            "chat_model": ", ".join(sorted(set(chat_models_used))),
            "source_counts": {
                source: int(count)
                for source, count in week_events.groupby("source")["id"].count().to_dict().items()
            } if not week_events.empty else {},
            "qa_pass": bool(qa_result.get("pass", True)),
            "qa_issues": qa_result.get("issues", []) if isinstance(qa_result.get("issues"), list) else [],
            "report_depth": report_depth,
        },
        "signals": {
            "terms": term_result.get("terms", []),
            "projects": {
                "rising_top": project_result.get("rising_top", []),
                "hot_top": project_result.get("hot_top", []),
                "novel_top": project_result.get("novel_top", []),
            },
            "clusters": clustering.get("clusters", []),
            "semantic_map": semantic_map,
            "semantic_diagnostics": {
                "silhouette_score": clustering.get("silhouette_score"),
                "project_count": len(semantic_map),
            },
        },
        "report": {
            "summary_bullets": qa_result.get("revised_summary", []) if isinstance(qa_result.get("revised_summary"), list) else [],
            "themes": themes,
            "project_boards": {
                "rising_top": project_result.get("rising_top", []),
                "hot_top": project_result.get("hot_top", []),
                "novel_top": project_result.get("novel_top", []),
            },
            "keyword_boards": build_keyword_boards(term_result),
            "cross_source_observations": build_cross_source_observations(themes),
            "watchlist": [
                {
                    "theme_title": theme.get("theme_title", ""),
                    "items": theme.get("next_week_watchlist", []),
                }
                for theme in themes
                if theme.get("next_week_watchlist")
            ],
            "markdown": markdown,
        },
        "citations": build_citations(week_events),
    }


def render_markdown_from_payload(payload: dict[str, Any]) -> str:
    meta = payload.get("meta", {})
    report = payload.get("report", {})
    lines = [
        f"# Weekly Research Report | {meta.get('week_start', '')} ~ {meta.get('week_end', '')}",
        "",
        f"> generated_at: {meta.get('generated_at', '')}",
        f"> k_selected: {meta.get('k_selected', 0)}",
        f"> embedding_model: {meta.get('embedding_model', '')}",
        f"> chat_model: {meta.get('chat_model', '')}",
        "",
        report.get("markdown", "").strip(),
        "",
        "## 引用索引",
        "",
    ]
    citations = payload.get("citations", {})
    for item_id, item in sorted(citations.items()):
        lines.append(f"- [{item.get('source')}:{item_id}] {item.get('title')} ({item.get('url')})")
    return "\n".join([line for line in lines if line is not None]).strip() + "\n"


def write_weekly_outputs(payload: dict[str, Any], markdown: str, window: WeekWindow) -> tuple[Path, Path]:
    INSIGHTS_WEEKLY_DIR.mkdir(parents=True, exist_ok=True)
    week_slug = _slugify_week(window.week_start)
    json_path = INSIGHTS_WEEKLY_DIR / f"weekly-report-{week_slug}.json"
    md_path = INSIGHTS_WEEKLY_DIR / f"weekly-report-{week_slug}.md"
    latest_json = INSIGHTS_WEEKLY_DIR / "latest.json"
    latest_md = INSIGHTS_WEEKLY_DIR / "latest.md"

    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    md_path.write_text(markdown, encoding="utf-8")

    should_update_latest = True
    if latest_json.exists():
        try:
            latest_payload = json.loads(latest_json.read_text(encoding="utf-8"))
            latest_week = str((latest_payload.get("meta") or {}).get("week_start", "")).strip()
            if latest_week:
                latest_date = datetime.strptime(latest_week, "%Y-%m-%d").date()
                if latest_date > window.week_start:
                    should_update_latest = False
        except Exception:
            should_update_latest = True

    if should_update_latest:
        latest_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        latest_md.write_text(markdown, encoding="utf-8")
    return json_path, md_path
