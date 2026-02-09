import json
import math
import os
from collections import Counter
from pathlib import Path
from typing import Dict, List

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
STRUCTURED_DIR = BASE_DIR / "data" / "structured"
INSIGHTS_DIR = BASE_DIR / "data" / "insights"


def load_items() -> pd.DataFrame:
    files = sorted(STRUCTURED_DIR.glob("*.parquet"))
    dfs = []
    for f in files:
        try:
            dfs.append(pd.read_parquet(f))
        except Exception as e:
            print(f"读取 parquet 失败: {f.name} -> {e}")
    if dfs:
        return pd.concat(dfs, ignore_index=True)

    nd_path = STRUCTURED_DIR / "items.ndjson"
    if not nd_path.exists():
        return pd.DataFrame()

    rows = []
    with nd_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return pd.DataFrame(rows)


def normalize_keywords(value) -> List[str]:
    if isinstance(value, (list, tuple, set)):
        raw = list(value)
    elif hasattr(value, "tolist"):
        try:
            raw = list(value.tolist())
        except Exception:
            raw = []
    elif isinstance(value, str):
        text = value.strip().replace("，", ",")
        if text.startswith("关键词：") or text.startswith("关键字："):
            text = text.split("：", 1)[1].strip()
        raw = [p.strip() for p in text.split(",") if p.strip()]
    else:
        raw = []

    cleaned: List[str] = []
    for kw in raw:
        s = str(kw).strip()
        if s.startswith("关键词：") or s.startswith("关键字："):
            s = s.split("：", 1)[1].strip()
        if s:
            cleaned.append(s)
    return cleaned


def canonical_keyword(kw: str) -> str:
    return " ".join(kw.lower().strip().replace("_", " ").split())


def extract_item_score_total(value) -> float | None:
    if isinstance(value, dict):
        value = value.get("total")
    if value is None:
        return None
    try:
        score = float(value)
    except (TypeError, ValueError):
        return None
    # 统一限制在 0~100，避免异常值放大权重
    return max(0.0, min(100.0, score))


def score_to_weight(score: float | None) -> float:
    """
    将项目评分映射为关键词计数权重：
    w = score_total / 100
    - 无评分: 0.0（严格模式，不计入加权热度）
    - 0 分: 0.0
    - 100 分: 1.0
    """
    if score is None:
        return 0.0
    return score / 100.0


def _get_int_env(name: str, default: int) -> int:
    raw = os.getenv(name)
    if raw is None or str(raw).strip() == "":
        return default
    try:
        return int(raw)
    except ValueError:
        print(f"警告: {name}={raw!r} 不是整数，使用默认值 {default}")
        return default


def _get_float_env(name: str, default: float) -> float:
    raw = os.getenv(name)
    if raw is None or str(raw).strip() == "":
        return default
    try:
        return float(raw)
    except ValueError:
        print(f"警告: {name}={raw!r} 不是浮点数，使用默认值 {default}")
        return default


def build_keyword_trends(df: pd.DataFrame) -> Dict:
    if df.empty or "keywords" not in df.columns or "date" not in df.columns:
        return {"dates": [], "keywords": []}

    work = df.copy()
    work["date"] = pd.to_datetime(work["date"], errors="coerce")
    work = work.dropna(subset=["date"])
    if work.empty:
        return {"dates": [], "keywords": []}

    work["keywords"] = work["keywords"].apply(normalize_keywords)
    work["score_total"] = work.get("score", pd.Series([None] * len(work))).apply(
        extract_item_score_total
    )
    work["score_weight"] = work["score_total"].apply(score_to_weight)

    recent_days = max(1, _get_int_env("KEYWORD_TREND_RECENT_DAYS", 3))
    min_total_support = max(1, _get_int_env("KEYWORD_TREND_MIN_TOTAL", 3))
    min_recent_freq = max(0.0, _get_float_env("KEYWORD_TREND_MIN_RECENT_FREQ", 1.0))

    display_counter: Dict[str, Counter] = {}
    rows = []
    doc_rows: List[str] = []
    for _, row in work.iterrows():
        date_str = row["date"].strftime("%Y-%m-%d")
        weight = float(row["score_weight"])
        item_keywords: Dict[str, str] = {}
        for kw in row["keywords"]:
            canon = canonical_keyword(kw)
            if not canon:
                continue
            item_keywords.setdefault(canon, kw)
            display_counter.setdefault(canon, Counter())[kw] += 1

        # 单个项目同一关键词只计一次，避免单条重复文本放大频次
        for canon in item_keywords:
            rows.append((date_str, canon, 1.0, weight))
            doc_rows.append(canon)

    if not rows:
        return {"dates": [], "keywords": []}

    trend_df = pd.DataFrame(rows, columns=["date", "canonical", "count", "weighted_count"])
    grouped = (
        trend_df.groupby(["date", "canonical"], as_index=False)[["count", "weighted_count"]]
        .sum()
    )
    raw_pivot = (
        grouped.pivot(index="date", columns="canonical", values="count")
        .fillna(0.0)
        .sort_index()
    )
    weighted_pivot = (
        grouped.pivot(index="date", columns="canonical", values="weighted_count")
        .fillna(0.0)
        .sort_index()
    )

    all_dates = raw_pivot.index.tolist()
    results = []
    history_total_docs = max(len(work), 1)
    doc_freq = pd.Series(doc_rows, dtype="string").value_counts()

    for canon in raw_pivot.columns:
        raw_series = raw_pivot[canon].astype(float)
        weighted_series = weighted_pivot[canon].astype(float)
        total = int(raw_series.sum())
        weighted_total = float(weighted_series.sum())
        if total < min_total_support:
            continue

        recent_slice = weighted_series.tail(recent_days)
        recent_freq = float(recent_slice.sum())
        if recent_freq < min_recent_freq:
            continue

        kw_doc_freq = float(doc_freq.get(canon, 0.0))
        # TF-IDF: 最近频次 * log(历史总量 / 历史含该词量)
        idf = math.log((history_total_docs + 1.0) / (kw_doc_freq + 1.0))
        tfidf_score = recent_freq * idf

        baseline = weighted_series.iloc[:-recent_days]
        if len(baseline) >= 2:
            base_mean = float(baseline.mean())
            base_std = float(baseline.std(ddof=0))
            recent_mean = float(recent_slice.mean())
            z_score = (recent_mean - base_mean) / base_std if base_std > 1e-9 else 0.0
        else:
            z_score = 0.0

        # 用 z-score 抓突增趋势：只增强上行趋势，避免噪声放大
        trend_boost = 1.0 + max(0.0, z_score)
        score = tfidf_score * trend_boost
        display = display_counter[canon].most_common(1)[0][0]

        results.append(
            {
                "keyword": display,
                "canonical": canon,
                "score": round(float(score), 4),
                # 保留字段兼容旧前端：growth 对应 tfidf，acceleration 对应 z-score
                "growth": round(float(tfidf_score), 4),
                "acceleration": round(float(z_score), 4),
                "tfidf": round(float(tfidf_score), 4),
                "z_score": round(float(z_score), 4),
                "idf": round(float(idf), 4),
                "recent_freq": round(float(recent_freq), 4),
                "total": total,
                "weighted_total": round(weighted_total, 4),
                "history_total": int(history_total_docs),
                "doc_freq": int(kw_doc_freq),
                "recent_days": int(recent_days),
                "series": [
                    {
                        "date": d,
                        "count": int(raw_series.loc[d]),
                        "weighted_count": round(float(weighted_series.loc[d]), 4),
                    }
                    for d in all_dates
                ],
            }
        )

    results.sort(key=lambda x: float(x.get("score", 0.0)), reverse=True)
    return {"dates": all_dates, "keywords": results}


def save_outputs(payload: Dict) -> None:
    INSIGHTS_DIR.mkdir(parents=True, exist_ok=True)

    json_path = INSIGHTS_DIR / "keyword_trends.json"
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"已写入趋势 JSON: {json_path}")

    # MD 输出已弃用，仅保留 JSON


def main():
    df = load_items()
    payload = build_keyword_trends(df)
    save_outputs(payload)
    print(f"候选关键词数: {len(payload.get('keywords', []))}")


if __name__ == "__main__":
    main()
