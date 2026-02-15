import json
import math
import os
from html import escape
from pathlib import Path
from typing import Optional

import pandas as pd
import streamlit as st
import altair as alt
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

BASE_DIR = Path(__file__).resolve().parent.parent
STRUCTURED_DIR = BASE_DIR / "data" / "structured"
INSIGHTS_DIR = BASE_DIR / "data" / "insights"

def _file_signature(paths: list[Path]) -> str:
    parts = []
    for path in paths:
        if not path.exists():
            continue
        stat = path.stat()
        parts.append(f"{path.name}:{stat.st_mtime_ns}:{stat.st_size}")
    return "|".join(parts)


def _structured_signature() -> str:
    parquet_files = sorted(STRUCTURED_DIR.glob("*.parquet"))
    ndjson_file = STRUCTURED_DIR / "items.ndjson"
    return _file_signature(parquet_files + [ndjson_file])


def _insights_signature() -> str:
    trends_file = INSIGHTS_DIR / "keyword_trends.json"
    return _file_signature([trends_file])


@st.cache_data
def load_items(_signature: str) -> pd.DataFrame:
    files = sorted(STRUCTURED_DIR.glob("*.parquet"))
    dfs = []
    for f in files:
        try:
            dfs.append(pd.read_parquet(f))
        except Exception:
            pass
    parquet_df = pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()

    nd = STRUCTURED_DIR / "items.ndjson"
    ndjson_df = pd.DataFrame()
    if nd.exists():
        try:
            ndjson_df = pd.DataFrame([json.loads(l) for l in nd.open()])
        except Exception:
            ndjson_df = pd.DataFrame()

    if not parquet_df.empty and not ndjson_df.empty:
        # Prefer latest ndjson entries and deduplicate by stable item id.
        df = pd.concat([parquet_df, ndjson_df], ignore_index=True)
        if "id" in df.columns:
            df = df.drop_duplicates(subset=["id"], keep="last")
        else:
            df = df.drop_duplicates(keep="last")
    elif not parquet_df.empty:
        df = parquet_df
    else:
        df = ndjson_df

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


@st.cache_data
def load_keyword_trends(_signature: str) -> dict:
    path = INSIGHTS_DIR / "keyword_trends.json"
    if not path.exists():
        return {"dates": [], "keywords": []}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {"dates": [], "keywords": []}


def _load_ndjson_rows() -> list[dict]:
    nd = STRUCTURED_DIR / "items.ndjson"
    if not nd.exists():
        return []
    rows: list[dict] = []
    try:
        for line in nd.open("r", encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    except Exception:
        return []
    return rows


def _write_ndjson_rows(rows: list[dict]) -> None:
    nd = STRUCTURED_DIR / "items.ndjson"
    nd.parent.mkdir(parents=True, exist_ok=True)
    with nd.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def _rewrite_date_parquet(date_str: str, rows: list[dict]) -> None:
    path = STRUCTURED_DIR / f"{date_str}.parquet"
    date_rows = [r for r in rows if str(r.get("date", "")) == str(date_str)]
    if not date_rows:
        if path.exists():
            path.unlink()
        return
    fixed_rows = []
    for item in date_rows:
        fixed = {}
        for k, v in item.items():
            if isinstance(v, dict) and not v:
                fixed[k] = None
            else:
                fixed[k] = v
        fixed_rows.append(fixed)
    df = pd.DataFrame(fixed_rows)
    df.to_parquet(path, index=False)


def _parse_keyword_input(raw: str) -> list[str]:
    text = (raw or "").replace("，", ",")
    parts = []
    for chunk in text.splitlines():
        parts.extend(chunk.split(","))
    out: list[str] = []
    seen = set()
    for p in parts:
        s = str(p).strip()
        if not s:
            continue
        if s.startswith("关键词：") or s.startswith("关键字："):
            s = s.split("：", 1)[1].strip()
        if not s:
            continue
        key = s.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(s)
    return out


def _get_admin_password() -> str:
    pwd = os.getenv("ADMIN_PASSWORD", "").strip()
    if pwd:
        return pwd
    try:
        secret_pwd = str(st.secrets.get("ADMIN_PASSWORD", "")).strip()
        if secret_pwd:
            return secret_pwd
    except Exception:
        pass
    return ""


def _update_item_keywords(item_id: str, keywords: list[str]) -> tuple[bool, str]:
    rows = _load_ndjson_rows()
    if not rows:
        return False, "items.ndjson 为空或读取失败"
    found = False
    target_date = None
    for row in rows:
        if str(row.get("id", "")) == str(item_id):
            row["keywords"] = keywords
            found = True
            target_date = str(row.get("date", ""))
            break
    if not found:
        return False, f"未找到 id={item_id}"
    _write_ndjson_rows(rows)
    if target_date:
        _rewrite_date_parquet(target_date, rows)
    return True, f"已更新 {item_id} 的关键词（{len(keywords)} 个）"


def _delete_item_by_id(item_id: str) -> tuple[bool, str]:
    rows = _load_ndjson_rows()
    if not rows:
        return False, "items.ndjson 为空或读取失败"
    target_row = None
    kept = []
    for row in rows:
        if str(row.get("id", "")) == str(item_id):
            target_row = row
            continue
        kept.append(row)
    if target_row is None:
        return False, f"未找到 id={item_id}"
    _write_ndjson_rows(kept)
    target_date = str(target_row.get("date", ""))
    if target_date:
        _rewrite_date_parquet(target_date, kept)
    return True, f"已删除 {item_id}"


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


def _to_float(value, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


SORT_FIELD_OPTIONS = {
    "趋势分": "score",
    "占比总量（历史）": "weighted_total",
    "基础占比": "tfidf",
    "Z-Score": "z_score",
    "最近占比": "recent_freq",
    "总出现量": "total",
}


def sort_keywords_for_display(keywords: list[dict], sort_field: str = "score") -> list[dict]:
    return sorted(
        keywords,
        key=lambda x: (
            _to_float(x.get(sort_field), 0.0),
            _to_float(x.get("score"), 0.0),
            _to_float(x.get("weighted_total"), 0.0),
            _to_float(x.get("total"), 0.0),
        ),
        reverse=True,
    )


def trend_state(item: dict) -> tuple[str, str, float]:
    z = _to_float(item.get("z_score", item.get("acceleration", 0.0)), 0.0)
    if z >= 1.0:
        return "强上升", "#dc2626", z
    if z >= 0.2:
        return "上升", "#ea580c", z
    if z <= -1.0:
        return "强下降", "#15803d", z
    if z <= -0.2:
        return "下降", "#16a34a", z
    return "平稳", "#64748b", z


def _trend_series_y_field(series_df: pd.DataFrame) -> str:
    if "share" in series_df.columns:
        return "share"
    return "count"


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
    reason = (item.get("score") or {}).get("reason") if isinstance(item.get("score"), dict) else None
    reason_html = (
        f"<div class='reason'>{escape(str(reason))}</div>"
        if isinstance(reason, str) and reason.strip()
        else ""
    )
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
        reason_html,
        chips_html,
        f"<div class='meta'>{meta}</div>",
        "</div>",
        img_html,
        "</div>",
        "</div>",
    ]
    return "\n".join([l for l in lines if l])


def _score_radar_axes(item):
    score_obj = item.get("score") if isinstance(item, dict) else None
    if not isinstance(score_obj, dict):
        return None
    breakdown = score_obj.get("breakdown")
    if not isinstance(breakdown, dict):
        return None

    # Normalize each axis to [0, 1] so different sub-score ranges are comparable.
    dims = [
        ("AI Native", "ai_native", 30.0, False),
        ("Tech Niche", "tech_niche", 25.0, False),
        ("Business", "business", 20.0, False),
        ("Team", "team", 15.0, False),
        ("Bonus", "bonus", 10.0, False),
        ("Penalty(inv)", "penalty", 10.0, True),
    ]
    labels = []
    values = []
    raws = []
    for label, key, cap, invert in dims:
        raw = _to_float(breakdown.get(key), 0.0)
        value = raw / cap if cap > 0 else 0.0
        if invert:
            value = 1.0 - value
        value = max(0.0, min(1.0, value))
        labels.append(label)
        values.append(value)
        raws.append(raw)
    return labels, values, raws


def build_score_radar_svg(item) -> Optional[str]:
    axes = _score_radar_axes(item)
    if axes is None:
        return None
    labels, values, raws = axes
    n = len(labels)
    if n == 0:
        return None

    cx = 120.0
    cy = 120.0
    rmax = 78.0
    size = 240

    axis_rows = []
    for idx, label in enumerate(labels):
        angle = (2 * math.pi * idx / n) - (math.pi / 2)
        v = values[idx]
        axis_rows.append(
            {
                "dimension": label,
                "value": v,
                "raw": raws[idx],
                "x": cx + (rmax * v * math.cos(angle)),
                "y": cy + (rmax * v * math.sin(angle)),
                "axis_x": cx + (rmax * math.cos(angle)),
                "axis_y": cy + (rmax * math.sin(angle)),
                "label_x": cx + (rmax * 1.22 * math.cos(angle)),
                "label_y": cy + (rmax * 1.22 * math.sin(angle)),
            }
        )

    rings = []
    for frac in [0.25, 0.5, 0.75, 1.0]:
        rings.append(
            f"<circle cx='{cx}' cy='{cy}' r='{rmax * frac:.2f}' fill='none' stroke='#e5e7eb' stroke-width='1' />"
        )

    spokes = []
    for p in axis_rows:
        spokes.append(
            f"<line x1='{cx}' y1='{cy}' x2='{p['axis_x']:.2f}' y2='{p['axis_y']:.2f}' stroke='#d1d5db' stroke-width='1' />"
        )

    poly_points = " ".join([f"{p['x']:.2f},{p['y']:.2f}" for p in axis_rows])
    poly_fill = f"<polygon points='{poly_points}' fill='#2563eb' fill-opacity='0.16' stroke='none' />"
    poly_line = f"<polygon points='{poly_points}' fill='none' stroke='#1d4ed8' stroke-width='2' />"

    dots = []
    labels_svg = []
    for p in axis_rows:
        dots.append(f"<circle cx='{p['x']:.2f}' cy='{p['y']:.2f}' r='2.8' fill='#1d4ed8' />")
        lx = p["label_x"]
        anchor = "middle"
        if lx < cx - 8:
            anchor = "end"
        elif lx > cx + 8:
            anchor = "start"
        labels_svg.append(
            f"<text x='{lx:.2f}' y='{p['label_y']:.2f}' font-size='9' fill='#475569' text-anchor='{anchor}' dominant-baseline='middle'>{escape(str(p['dimension']))}</text>"
        )

    svg = (
        f"<svg viewBox='0 0 {size} {size}' width='100%' height='220' xmlns='http://www.w3.org/2000/svg'>"
        + "".join(rings)
        + "".join(spokes)
        + poly_fill
        + poly_line
        + "".join(dots)
        + "".join(labels_svg)
        + "</svg>"
    )
    return svg


def _score_color(norm_score: float) -> str:
    norm = max(0.0, min(1.0, norm_score))
    g = (15, 157, 88)
    r = (239, 68, 68)
    c = (
        int(g[0] + (r[0] - g[0]) * norm),
        int(g[1] + (r[1] - g[1]) * norm),
        int(g[2] + (r[2] - g[2]) * norm),
    )
    return f"#{c[0]:02x}{c[1]:02x}{c[2]:02x}"


STYLE = """
<style>
.block-container { padding-top: 1.5rem; max-width: 1300px; }
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
.reason { color:#334155; font-size:12px; line-height:1.45; margin:2px 0 8px 0; }
.chips { display:flex; flex-wrap:wrap; gap:6px; margin-bottom:6px; }
    .chip { padding:6px 10px; border-radius:10px; background:#eef2ff; border:1px solid #c7d2fe; color:#0f172a; font-size:12px; font-weight:600; }
    .thumb { width:100%; max-height:180px; object-fit:cover; border-radius:12px; border:1px solid #e5e7eb; box-shadow:0 6px 14px rgba(0,0,0,0.05); }
    .title-row { display:flex; align-items:center; gap:12px; flex-wrap:wrap; }
</style>
"""

st.set_page_config(page_title="Daily AI Feeds", layout="wide")
st.markdown(STYLE, unsafe_allow_html=True)

st.title("Daily AI Feeds")

df = load_items(_structured_signature())
if df.empty:
    st.warning("暂无数据，请先生成 structured 数据。")
    st.stop()
df_all = df.copy()

sort_label = st.selectbox("关键词趋势排序", list(SORT_FIELD_OPTIONS.keys()), index=0)
sort_field = SORT_FIELD_OPTIONS[sort_label]

tab_items, tab_trends = st.tabs(["内容浏览", "关键词趋势"])

with tab_items:
    trends = load_keyword_trends(_insights_signature())
    t_keywords = (
        sort_keywords_for_display(trends.get("keywords", []), sort_field=sort_field)
        if trends
        else []
    )

    left_col, right_col = st.columns([4, 1])

    date_values = (
        df_all["date"]
        .dropna()
        .astype(str)
        .sort_values(ascending=False)
        .unique()
        .tolist()
    )

    with left_col:
        col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
        with col1:
            q = st.text_input("搜索标题 / 关键词 / 描述", "")
        with col2:
            sources = [""] + sorted(df["source"].dropna().unique().tolist())
            source = st.selectbox("来源", sources, format_func=lambda x: "全部" if x == "" else x)
        with col3:
            limit = st.slider("显示条数", 10, 200, 50, 10)
        with col4:
            date_choice = st.selectbox("日期", date_values)
        with col5:
            manage_mode = st.toggle("管理模式", value=False, key="items_manage_mode")

        inline_authed = True
        if manage_mode:
            admin_password = _get_admin_password()
            if admin_password:
                inline_pwd = st.text_input("管理员密码", type="password", key="items_admin_password")
                inline_authed = (inline_pwd == admin_password)
                if not inline_authed:
                    st.warning("管理模式已开启，请输入正确管理员密码后操作。")
            else:
                st.caption("未设置 ADMIN_PASSWORD（.env 或 st.secrets），当前环境默认允许管理操作。")

        df_items = df_all
        if date_choice:
            df_items = df_items[df_items["date"].astype(str) == date_choice]

        df_f = filter_items(df_items, source or None, q or None)
        if not df_f.empty and "score" in df_f.columns:
            df_f = df_f.copy()
            df_f["score_total"] = df_f["score"].apply(
                lambda s: (s or {}).get("total") if isinstance(s, dict) else None
            )
            df_f = df_f.sort_values(
                by=["score_total", "rank"],
                ascending=[False, True],
                na_position="last",
            )
        st.caption(f"共 {len(df_f)} 条，显示前 {min(limit, len(df_f))} 条")

        for _, row in df_f.head(limit).iterrows():
            row_dict = row.to_dict() if hasattr(row, "to_dict") else dict(row)
            item_col, radar_col = st.columns([5, 2], gap="small")
            with item_col:
                st.markdown(card_html(row_dict), unsafe_allow_html=True)
                if manage_mode:
                    item_id = str(row_dict.get("id", ""))
                    st.caption(f"管理ID: `{item_id}`")
                    with st.expander("编辑关键词 / 删除项目", expanded=False):
                        current_kw = row_dict.get("keywords", []) if isinstance(row_dict.get("keywords"), list) else []
                        kw_text = st.text_area(
                            "关键词（每行一个，或逗号分隔）",
                            value="\n".join(current_kw),
                            height=120,
                            key=f"inline_kw_{item_id}",
                            disabled=not inline_authed,
                        )
                        parsed_kw = _parse_keyword_input(kw_text)
                        st.caption(f"解析后关键词数: {len(parsed_kw)}")
                        a1, a2, a3 = st.columns([1, 1, 2])
                        with a1:
                            if st.button("保存关键词", key=f"inline_save_kw_{item_id}", type="primary", disabled=not inline_authed):
                                ok, msg = _update_item_keywords(item_id, parsed_kw)
                                if ok:
                                    st.success(msg)
                                    st.cache_data.clear()
                                    st.rerun()
                                else:
                                    st.error(msg)
                        with a2:
                            confirm_delete = st.checkbox("确认删除", key=f"inline_confirm_delete_{item_id}", disabled=not inline_authed)
                            if st.button("删除项目", key=f"inline_delete_item_{item_id}", disabled=not inline_authed):
                                if not confirm_delete:
                                    st.warning("请先勾选“确认删除”。")
                                else:
                                    ok, msg = _delete_item_by_id(item_id)
                                    if ok:
                                        st.success(msg)
                                        st.cache_data.clear()
                                        st.rerun()
                                    else:
                                        st.error(msg)
            with radar_col:
                st.caption("评分维度")
                radar_svg = build_score_radar_svg(row_dict)
                if radar_svg is not None:
                    st.markdown(radar_svg, unsafe_allow_html=True)

    with right_col:
        if t_keywords:
            t_scores = [_to_float(k.get(sort_field), 0.0) for k in t_keywords]
            t_min = min(t_scores) if t_scores else 0.0
            t_max = max(t_scores) if t_scores else 1.0
            t_span = t_max - t_min if t_max != t_min else 1.0
            st.markdown(f"**关键词趋势排行（按{sort_label}）**")
            top_sidebar = t_keywords[:6]
            for idx, k in enumerate(top_sidebar, start=1):
                score = _to_float(k.get(sort_field), 0.0)
                ns = (score - t_min) / t_span
                color = _score_color(ns)
                kw = str(k.get("keyword", ""))
                trend_text, trend_color, trend_z = trend_state(k)
                st.markdown(
                    f"<div style='display:flex;align-items:center;gap:8px;'>"
                    f"<span style='font-weight:700;color:#0f172a;'>{idx}.</span>"
                    f"<span style='font-weight:600;color:#0f172a;'>{escape(kw)}</span>"
                    f"<span style='font-size:12px;color:{trend_color};font-weight:600;'>{trend_text}</span>"
                    f"<span style='margin-left:auto;color:{color};font-weight:700;'>"
                    f"{score:.2f}</span></div>"
                    f"<div style='font-size:11px;color:#64748b;margin:2px 0 4px 24px;'>z={trend_z:.2f}</div>",
                    unsafe_allow_html=True,
                )
                series_df = pd.DataFrame(k.get("series", []))
                if not series_df.empty:
                    series_df["norm_score"] = max(0.0, min(1.0, ns))
                    series_df["date"] = pd.to_datetime(series_df["date"])
                    series_df = series_df.sort_values("date").tail(7)
                    y_field = _trend_series_y_field(series_df)
                    mini_base = alt.Chart(series_df).encode(
                        x=alt.X("date:T", axis=alt.Axis(labels=False, ticks=False, title=None)),
                        y=alt.Y(f"{y_field}:Q", axis=alt.Axis(labels=False, ticks=False, title=None)),
                        color=alt.Color(
                            "norm_score:Q",
                            scale=alt.Scale(domain=[0, 1], range=["#0f9d58", "#ef4444"]),
                            legend=None,
                        ),
                    )
                    mini_area = mini_base.mark_area(interpolate="monotone", opacity=0.2)
                    mini_line = mini_base.mark_line(interpolate="monotone")
                    mini_points = mini_base.mark_point(filled=False, size=40, strokeWidth=1.5)
                    mini_chart = alt.layer(mini_area, mini_line, mini_points).properties(height=70)
                    st.altair_chart(mini_chart, use_container_width=True)
        else:
            st.caption("暂无趋势数据")

with tab_trends:
    trends = load_keyword_trends(_insights_signature())
    keywords = sort_keywords_for_display(trends.get("keywords", []), sort_field=sort_field)
    dates = trends.get("dates", [])
    if not keywords:
        st.warning("暂无趋势数据，请先运行：python scripts/keyword_trends.py")
    else:
        col_a, col_b = st.columns([1, 2])
        with col_a:
            top_n = st.slider("显示关键词数量", 5, 50, 20, 1, key="trend_topn")
        with col_b:
            if dates:
                st.caption(f"趋势统计区间：{dates[0]} ~ {dates[-1]}")

        scores = [float(k.get("score", 0.0)) for k in keywords]
        score_min = min(scores) if scores else 0.0
        score_max = max(scores) if scores else 1.0
        score_span = score_max - score_min if score_max != score_min else 1.0

        for i, item in enumerate(keywords[:top_n], start=1):
            trend_text, _, _ = trend_state(item)
            sort_value = _to_float(item.get(sort_field), 0.0)
            st.markdown(
                f"**{i}. {item['keyword']}**  "
                f"(排序值 `{sort_label}={sort_value:.4f}` / 趋势分 `{item['score']:.4f}` / 基础占比 `{item.get('tfidf', item['growth']):.4f}` / z-score `{item.get('z_score', item['acceleration']):.4f}` / 趋势 `{trend_text}` / total `{item['total']}`)"
            )
            series_df = pd.DataFrame(item["series"])
            if not series_df.empty:
                norm_score = (float(item.get("score", 0.0)) - score_min) / score_span
                norm_score = max(0.0, min(1.0, norm_score))
                series_df["norm_score"] = norm_score
                series_df["score"] = item["score"]
                series_df["date"] = pd.to_datetime(series_df["date"])
                series_df = series_df.sort_values("date").tail(7)
                y_field = _trend_series_y_field(series_df)
                base = alt.Chart(series_df).encode(
                    x=alt.X("date:T", title="", axis=alt.Axis(labelAngle=0, format="%m-%d")),
                    y=alt.Y(f"{y_field}:Q", title=""),
                    color=alt.Color(
                        "norm_score:Q",
                        scale=alt.Scale(domain=[0, 1], range=["#0f9d58", "#ef4444"]),
                        legend=None,
                    ),
                )
                area = base.mark_area(interpolate="monotone", opacity=0.18)
                line = base.mark_line(interpolate="monotone")
                points = base.mark_point(filled=False, size=70, strokeWidth=2)
                chart = alt.layer(area, line, points).properties(height=160)
                st.altair_chart(chart, use_container_width=True)
