import json
from html import escape
from pathlib import Path
from typing import Optional

import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent.parent
STRUCTURED_DIR = BASE_DIR / "data" / "structured"

@st.cache_data
def load_items() -> pd.DataFrame:
    files = sorted(STRUCTURED_DIR.glob("*.parquet"))
    dfs = []
    for f in files:
        try:
            dfs.append(pd.read_parquet(f))
        except Exception:
            pass
    if dfs:
        df = pd.concat(dfs, ignore_index=True)
    else:
        nd = STRUCTURED_DIR / "items.ndjson"
        if nd.exists():
            df = pd.DataFrame([json.loads(l) for l in nd.open()])
        else:
            df = pd.DataFrame()

    if not df.empty and "keywords" in df.columns:
        def norm_kw(x):
            if isinstance(x, (list, tuple, set)):
                return list(x)
            if hasattr(x, "tolist"):
                try:
                    return list(x.tolist())
                except Exception:
                    pass
            if isinstance(x, str):
                if x.startswith("关键词：") or x.startswith("关键字："):
                    x = x.split("：", 1)[1]
                return [p.strip() for p in x.replace("，", ",").split(",") if p.strip()]
            return []
        df["keywords"] = df["keywords"].apply(norm_kw)
        df["date_dt"] = pd.to_datetime(df["date"], errors="coerce")
        df = df.sort_values(by=["date_dt", "rank"], ascending=[False, True])
    return df


def filter_items(df: pd.DataFrame, source: Optional[str], q: Optional[str]):
    if df.empty:
        return df
    if source:
        df = df[df["source"] == source]
    if q:
        ql = q.lower()
        def m(row):
            text = " ".join([
                str(row.get("title", "")),
                str(row.get("description_zh", "")),
                str(row.get("description_en", "")),
                " ".join(row.get("keywords", [])),
            ]).lower()
            return ql in text
        df = df[df.apply(m, axis=1)]
    return df


def card_html(item):
    title = escape(item.get("title", ""))
    url = item.get("url", "#")
    desc = escape(item.get("description_zh") or item.get("description_en") or "")
    kws = item.get("keywords") or []

    cleaned = []
    for k in kws:
        s = str(k).strip()
        if s.startswith("关键词：") or s.startswith("关键字："):
            s = s.split("：", 1)[1].strip()
        if s:
            cleaned.append(s)

    chips_html = "".join([f"<span class='chip'>{escape(k)}</span>" for k in cleaned[:12]])
    if chips_html:
        chips_html = f"<div class='chips'>{chips_html}</div>"

    score = (item.get("score") or {}).get("total")
    score_class = "s1" if score is not None and score < 74 else "s2" if score is not None and score < 78 else "s3"
    score_html = f"<span class='score {score_class}'>{score}</span>" if score is not None else ""

    meta_bits = []
    metrics = item.get("metrics") or {}
    if item.get("source"):
        meta_bits.append(str(item.get("source")))
    if item.get("date"):
        meta_bits.append(str(item.get("date")))
    if item.get("rank"):
        meta_bits.append(f"#{item.get('rank')}")
    if metrics.get("votes"):
        meta_bits.append(f"票 {metrics['votes']}")
    if metrics.get("stars"):
        meta_bits.append(f"⭐ {metrics['stars']}")
    meta = " · ".join(meta_bits)

    media = item.get("media") or {}
    img = media.get("image")
    has_img = bool(img)
    img_html = f"<img class='thumb' src='{img}'/>" if has_img else ""
    row_class = "row" if has_img else "row no-media"

    lines = [
        "<div class='card'>",
        f"<div class='{row_class}'>",
        "<div>",
        "<div class='title-row'>",
        f"<a class='title' href='{url}' target='_blank' rel='noopener'>{title}</a>",
        score_html,
        "</div>",
        f"<div class='desc'>{desc}</div>",
        chips_html,
        f"<div class='meta'>{meta}</div>",
        "</div>",
        img_html,
        "</div>",
        "</div>",
    ]
    return "\n".join([l for l in lines if l])


STYLE = """
<style>
.block-container { padding-top: 1.5rem; max-width: 1100px; }
.card { background:#fff; border:1px solid #e5e7eb; border-radius:16px; padding:16px 18px; margin-bottom:14px; box-shadow:0 10px 30px rgba(0,0,0,0.06); }
.row { display:grid; grid-template-columns:1fr 230px; gap:14px; align-items:start; }
.row.no-media { grid-template-columns:1fr; }
@media (max-width:900px){ .row { grid-template-columns:1fr; } }
.title { font-size:22px; font-weight:750; color:#0f172a; text-decoration:none; line-height:1.3; }
.title:hover { color:#007aff; }
.score { font-size:24px; font-weight:800; }
.score.s1 { background: linear-gradient(135deg,#f97316,#facc15); -webkit-background-clip:text; color:transparent; }
.score.s2 { background: linear-gradient(135deg,#22c55e,#a3e635); -webkit-background-clip:text; color:transparent; }
.score.s3 { background: linear-gradient(135deg,#2563eb,#38bdf8); -webkit-background-clip:text; color:transparent; }
.meta { color:#6b7280; font-size:12px; margin-top:6px; }
.desc { color:#1f2937; font-size:14px; line-height:1.5; margin:6px 0 8px 0; }
.chips { display:flex; flex-wrap:wrap; gap:6px; margin-bottom:6px; }
.chip { padding:6px 10px; border-radius:10px; background:#eef2ff; border:1px solid #c7d2fe; color:#0f172a; font-size:12px; font-weight:600; }
.thumb { width:100%; max-height:180px; object-fit:cover; border-radius:12px; border:1px solid #e5e7eb; box-shadow:0 6px 14px rgba(0,0,0,0.05); }
.title-row { display:flex; align-items:center; gap:12px; flex-wrap:wrap; }
</style>
"""

st.set_page_config(page_title="Daily AI Feeds", layout="wide")
st.markdown(STYLE, unsafe_allow_html=True)

st.title("Daily AI Feeds")

df = load_items()
if df.empty:
    st.warning("暂无数据，请先生成 structured 数据。")
    st.stop()

date_values = (
    df["date"]
    .dropna()
    .astype(str)
    .sort_values(ascending=False)
    .unique()
    .tolist()
)

col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
with col1:
    q = st.text_input("搜索标题 / 关键词 / 描述", "")
with col2:
    sources = [""] + sorted(df["source"].dropna().unique().tolist())
    source = st.selectbox("来源", sources, format_func=lambda x: "全部" if x == "" else x)
with col3:
    limit = st.slider("显示条数", 10, 200, 50, 10)
with col4:
    date_choice = st.selectbox("日期", date_values)

if date_choice:
    df = df[df["date"].astype(str) == date_choice]

df_f = filter_items(df, source or None, q or None)
st.caption(f"共 {len(df_f)} 条，显示前 {min(limit, len(df_f))} 条")

for _, row in df_f.head(limit).iterrows():
    st.markdown(card_html(row), unsafe_allow_html=True)
