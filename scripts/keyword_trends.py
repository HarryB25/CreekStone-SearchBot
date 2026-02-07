import json
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


def build_keyword_trends(df: pd.DataFrame) -> Dict:
    if df.empty or "keywords" not in df.columns or "date" not in df.columns:
        return {"dates": [], "keywords": []}

    work = df.copy()
    work["date"] = pd.to_datetime(work["date"], errors="coerce")
    work = work.dropna(subset=["date"])
    if work.empty:
        return {"dates": [], "keywords": []}

    work["keywords"] = work["keywords"].apply(normalize_keywords)

    display_counter: Dict[str, Counter] = {}
    rows = []
    for _, row in work.iterrows():
        date_str = row["date"].strftime("%Y-%m-%d")
        for kw in row["keywords"]:
            canon = canonical_keyword(kw)
            if not canon:
                continue
            rows.append((date_str, canon, kw))
            display_counter.setdefault(canon, Counter())[kw] += 1

    if not rows:
        return {"dates": [], "keywords": []}

    trend_df = pd.DataFrame(rows, columns=["date", "canonical", "display"])
    pivot = (
        trend_df.groupby(["date", "canonical"])
        .size()
        .rename("count")
        .reset_index()
        .pivot(index="date", columns="canonical", values="count")
        .fillna(0)
        .sort_index()
    )

    all_dates = pivot.index.tolist()
    results = []
    min_support = 3
    eps = 0.1

    for canon in pivot.columns:
        series = pivot[canon].astype(float)
        total = int(series.sum())
        if total < min_support:
            continue

        vals = series.values
        n = len(vals)
        recent3 = vals[max(0, n - 3): n].mean() if n > 0 else 0.0
        prev7_slice = vals[max(0, n - 10): max(0, n - 3)]
        prev7 = prev7_slice.mean() if len(prev7_slice) > 0 else 0.0
        growth = (recent3 + eps) / (prev7 + eps)

        last2 = vals[max(0, n - 2): n].mean() if n > 0 else 0.0
        prev2 = vals[max(0, n - 4): max(0, n - 2)]
        prev2_val = prev2.mean() if len(prev2) > 0 else 0.0
        prev4 = vals[max(0, n - 8): max(0, n - 4)]
        prev4_val = prev4.mean() if len(prev4) > 0 else 0.0
        acceleration = (last2 - prev2_val) - (prev2_val - prev4_val)

        nz_idx = series[series > 0].index
        first_seen = nz_idx[0] if len(nz_idx) > 0 else all_dates[0]
        days_since_first = (pd.to_datetime(all_dates[-1]) - pd.to_datetime(first_seen)).days
        novelty = max(0.0, 1.0 - min(days_since_first, 30) / 30.0)

        score = growth * 0.5 + acceleration * 0.35 + novelty * 0.15
        display = display_counter[canon].most_common(1)[0][0]

        results.append(
            {
                "keyword": display,
                "canonical": canon,
                "score": round(float(score), 4),
                "growth": round(float(growth), 4),
                "acceleration": round(float(acceleration), 4),
                "total": total,
                "recent3_avg": round(float(recent3), 4),
                "series": [
                    {"date": d, "count": int(series.loc[d])}
                    for d in all_dates
                ],
            }
        )

    results.sort(key=lambda x: x["score"], reverse=True)
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
