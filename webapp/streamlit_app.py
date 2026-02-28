import json
import os
from html import escape
from pathlib import Path
from typing import Optional

import pandas as pd
import streamlit as st
import altair as alt
try:
    from weekly_report_view import render_weekly_report_view
except ModuleNotFoundError:
    from webapp.weekly_report_view import render_weekly_report_view
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


def _match_column(row: dict, column: str) -> bool:
    col = (column or "").strip().lower()
    if not col:
        return True
    text = " ".join(
        [
            str(row.get("title", "")),
            str(row.get("description_zh", "")),
            str(row.get("description_en", "")),
            " ".join(row.get("keywords", []) or []),
            " ".join(row.get("tags", []) or []),
        ]
    ).lower()
    if col == "openclaw":
        # Keep this column strict to avoid pulling in generic MCP projects.
        keys = ["openclaw", "clawdbot", "clawhub"]
        return any(k in text for k in keys)
    if col == "claudecode":
        keys = ["claude code", "claudecode"]
        return any(k in text for k in keys)
    return True


def filter_items(df: pd.DataFrame, source: Optional[str], q: Optional[str], column: Optional[str] = None):
    if df.empty:
        return df
    if source:
        df = df[df["source"] == source]
    if column:
        col = str(column)
        df = df[df.apply(lambda r: _match_column(r.to_dict() if hasattr(r, "to_dict") else dict(r), col), axis=1)]
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
    return "平稳", "#a6a3a0", z


def _trend_series_y_field(series_df: pd.DataFrame) -> str:
    if "share" in series_df.columns:
        return "share"
    return "count"


def _format_reason_html(score_obj: Optional[dict]) -> str:
    score = score_obj if isinstance(score_obj, dict) else {}
    reason = score.get("reason")
    text = str(reason).strip() if isinstance(reason, str) else ""
    reason_struct = score.get("reason_struct") if isinstance(score.get("reason_struct"), dict) else {}

    if reason_struct:
        summary = str(reason_struct.get("summary", "")).strip()
        plus = [str(x).strip() for x in reason_struct.get("plus", []) if str(x).strip()]
        minus = [str(x).strip() for x in reason_struct.get("minus", []) if str(x).strip()]

        if plus or minus:
            parts = []
            if summary:
                parts.append(f"<span class='reason-neutral'>{escape(summary)}</span>")
            for p in plus:
                parts.append(f"<span class='reason-plus'>加分：{escape(p)}</span>")
            for m in minus:
                parts.append(f"<span class='reason-minus'>减分：{escape(m)}</span>")
            return f"<div class='reason'>{' '.join(parts)}</div>"

    if not text:
        return ""
    return f"<div class='reason'><span class='reason-neutral'>{escape(text)}</span></div>"


def card_html(item, radar_svg: Optional[str] = None):
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
    reason_html = _format_reason_html(item.get("score"))
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
    img_html = f"<img class='thumb' src='{img}'/>" if img else ""
    radar_html = f"<div class='radar-box'>{radar_svg}</div>" if radar_svg else ""
    side_parts = [p for p in [img_html, radar_html] if p]
    side_html = f"<div class='side-col'>{''.join(side_parts)}</div>" if side_parts else ""
    row_class = "content-row has-side" if side_html else "content-row no-side"

    lines = [
        "<div class='card'>",
        f"<div class='{row_class}'>",
        "<div class='main-col'>",
        "<div class='title-row'>",
        f"<a class='title' href='{url}' target='_blank' rel='noopener'>{title}</a>",
        score_html,
        "</div>",
        f"<div class='desc'>{desc}</div>",
        reason_html,
        chips_html,
        f"<div class='meta'>{meta}</div>",
        "</div>",
        side_html,
        "</div>",
        "</div>",
    ]
    return "\n".join([l for l in lines if l])


def _score_breakdown_rows(item):
    score_obj = item.get("score") if isinstance(item, dict) else None
    if not isinstance(score_obj, dict):
        return None
    breakdown = score_obj.get("breakdown")
    if not isinstance(breakdown, dict):
        return None

    dims = [
        ("AI原生", "ai_native", 30.0, False, "#bb9e55"),
        ("技术壁垒", "tech_niche", 25.0, False, "#c7ac66"),
        ("商业价值", "business", 20.0, False, "#d1b776"),
        ("团队能力", "team", 15.0, False, "#dec78e"),
        ("加分项", "bonus", 10.0, False, "#ead7a6"),
        ("减分项", "penalty", 10.0, True, "#ef4444"),
    ]

    rows = []
    for label, key, cap, is_penalty, color in dims:
        raw = _to_float(breakdown.get(key), 0.0)
        ratio = raw / cap if cap > 0 else 0.0
        rows.append(
            {
                "label": label,
                "raw": max(0.0, raw),
                "cap": cap,
                "ratio": max(0.0, min(1.0, ratio)),
                "is_penalty": is_penalty,
                "color": color,
            }
        )
    return rows


def build_score_radar_svg(item) -> Optional[str]:
    rows = _score_breakdown_rows(item)
    if rows is None:
        return None
    if not rows:
        return None

    width = 320
    height = 232
    top = 10
    row_h = 34
    label_x = 10
    bar_x = 90
    bar_w = 150
    bar_h = 13
    value_x = bar_x + bar_w + 12

    def _fmt_num(val: float) -> str:
        if abs(val - round(val)) < 1e-6:
            return str(int(round(val)))
        return f"{val:.1f}"

    def _hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
        c = hex_color.strip().lstrip("#")
        if len(c) != 6:
            return (187, 158, 85)
        return (int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16))

    defs = ["<defs>"]
    for i, row in enumerate(rows):
        r, g, b = _hex_to_rgb(str(row["color"]))
        defs.append(
            f"<linearGradient id='bargrad-{i}' x1='0%' y1='0%' x2='100%' y2='0%'>"
            f"<stop offset='0%' stop-color='rgba({r},{g},{b},0.92)'/>"
            f"<stop offset='100%' stop-color='rgba({r},{g},{b},0.72)'/>"
            f"</linearGradient>"
        )
    defs.append("</defs>")

    parts = [
        f"<svg viewBox='0 0 {width} {height}' width='100%' height='220' xmlns='http://www.w3.org/2000/svg'>",
        "".join(defs),
    ]

    for i, row in enumerate(rows):
        y = top + i * row_h
        by = y + 11
        fill_w = row["ratio"] * bar_w
        value_text = _fmt_num(row["raw"])
        cap_text = _fmt_num(row["cap"])
        if row["is_penalty"] and row["raw"] > 0:
            value_text = f"-{value_text}"
        metric_text = f"{value_text}/{cap_text}"
        text_w = max(40, len(metric_text) * 6 + 12)
        badge_x = value_x
        badge_y = y + 10

        parts.append(
            f"<text x='{label_x}' y='{y + 18}' font-size='12' fill='#5f5a50' dominant-baseline='middle'>{escape(str(row['label']))}</text>"
        )
        parts.append(
            f"<rect x='{bar_x}' y='{by}' width='{bar_w}' height='{bar_h}' rx='6' fill='#e7e1d4' />"
        )
        if fill_w > 0:
            parts.append(
                f"<rect x='{bar_x}' y='{by}' width='{fill_w:.2f}' height='{bar_h}' rx='6' fill='url(#bargrad-{i})' />"
            )
            cap_x = bar_x + fill_w
            parts.append(
                f"<circle cx='{cap_x:.2f}' cy='{by + bar_h / 2:.2f}' r='3.3' fill='#fffdf8' stroke='{row['color']}' stroke-width='1.5' />"
            )
        parts.append(
            f"<rect x='{badge_x}' y='{badge_y}' width='{text_w}' height='16' rx='8' fill='rgba(187,158,85,0.10)' />"
        )
        parts.append(
            f"<text x='{badge_x + text_w / 2:.2f}' y='{y + 18}' text-anchor='middle' font-size='11.5' fill='#2b2823' dominant-baseline='middle'>{escape(metric_text)}</text>"
        )

    parts.append("</svg>")
    svg = "".join(parts)
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
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700;800&family=Noto+Serif+SC:wght@600;700;800&display=swap');
html, body, [data-testid="stApp"] {
  background: #f4f1e8;
  font-family: "Noto Sans SC", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Source Han Sans SC", sans-serif;
}
:root { --primary-color: #bb9e55 !important; --primaryColor: #bb9e55 !important; }
.stApp {
  --bg: #f4f1e8;
  --panel: #ffffff;
  --panel-2: #fcfaf5;
  --text: #26231f;
  --muted: #6e6658;
  --accent: #bb9e55;
  --accent-hi: #d5bb78;
  --accent-line: rgba(187, 158, 85, 0.35);
  background: var(--bg);
  color: var(--text);
  font-family: "Noto Sans SC", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Source Han Sans SC", sans-serif;
}
[data-testid="stAppViewContainer"] { background: transparent; }
[data-testid="stMain"] { background: transparent; }
[data-testid="stHeader"] {
  background: transparent;
  border-bottom: none;
}
[data-testid="stToolbar"] { color: var(--muted); }
[data-testid="stStatusWidget"] { color: var(--muted); }
[data-testid="stDecoration"] { display: none; }
.block-container { padding-top: 0.2rem; max-width: 1520px; }
h1, h2, h3, h4, h5, h6 {
  color: var(--text);
  font-family: "Noto Serif SC", "Source Han Serif SC", "STSong", serif;
}
p, li, label, .stMarkdown, .stCaption { color: var(--muted); }
code, .stMarkdown code, .stCode code {
  background: rgba(187,158,85,0.14) !important;
  color: #2b2823 !important;
  border: 1px solid var(--accent-line);
  border-radius: 7px;
  padding: 1px 6px;
}
pre code, .stCodeBlock code {
  background: transparent !important;
  border: none !important;
}
div[data-baseweb="select"] > div,
.stTextInput input,
.stTextArea textarea,
.stNumberInput input {
  background: #ffffff !important;
  color: #26231f !important;
  border: 1px solid rgba(70,58,39,0.20) !important;
}
.stTextInput input:focus,
.stTextArea textarea:focus,
div[data-baseweb="select"] > div:focus-within {
  border-color: var(--accent-line) !important;
  box-shadow: 0 0 0 1px var(--accent-line) inset !important;
}
.stButton > button {
  background: #ffffff;
  color: #26231f;
  border: 1px solid rgba(70,58,39,0.18);
}
.stButton > button:hover {
  border-color: var(--accent-line);
  color: var(--accent-hi);
  transform: translateY(-1px);
}
[data-baseweb="tab-list"] {
  gap: 8px;
}
[data-baseweb="tab-highlight"] {
  background: var(--accent) !important;
}
[data-baseweb="tab"] {
  background: #ffffff;
  color: #6e6658;
  border-radius: 8px;
  border: 1px solid rgba(70,58,39,0.18);
}
[aria-selected="true"][data-baseweb="tab"] {
  color: #8e7534;
  border-color: var(--accent-line);
}
.card {
  background: linear-gradient(180deg, var(--panel), var(--panel-2));
  border: 1px solid rgba(70,58,39,0.16);
  border-radius: 16px;
  padding: 16px 18px;
  margin-bottom: 14px;
  box-shadow: 0 12px 26px rgba(42,35,25,0.08), 0 0 0 1px rgba(187,158,85,0.15) inset;
}
.content-row { display:grid; gap:16px; align-items:start; }
.content-row.has-side { grid-template-columns:minmax(0,1fr) 280px; }
.content-row.no-side { grid-template-columns:minmax(0,1fr); }
@media (max-width:1000px){ .content-row.has-side { grid-template-columns:1fr; } }
.main-col { min-width:0; }
.side-col { width:100%; display:flex; flex-direction:column; gap:12px; }
.card a.title, .card a.title:visited { display:inline-block; font-size:30px; font-weight:800; color:var(--accent) !important; text-decoration:none; line-height:1.3; font-family:"Noto Serif SC", "Source Han Serif SC", "STSong", serif; }
.card a.title:hover { color:var(--accent-hi) !important; text-decoration:underline; text-decoration-thickness: 2px; text-underline-offset: 3px; }
.stMarkdown a { color: var(--accent); }
.score { font-size:34px; font-weight:800; line-height:1; }
.score.s1 { background: linear-gradient(135deg,#bb9e55,#d5bb78); -webkit-background-clip:text; color:transparent; }
.score.s2 { background: linear-gradient(135deg,#d0b575,#e5cf9e); -webkit-background-clip:text; color:transparent; }
.score.s3 { background: linear-gradient(135deg,#ead7a6,#f3e5be); -webkit-background-clip:text; color:transparent; }
.meta { color:var(--muted); font-size:15px; margin-top:8px; line-height:1.5; }
.desc { color:var(--text); font-size:17px; line-height:1.65; margin:8px 0 8px 0; }
.reason { font-size:16px; line-height:1.72; margin:4px 0 10px 0; }
.reason-neutral { color:var(--muted); }
.reason-plus { color:#15803d; font-weight:600; }
.reason-minus { color:#dc2626; font-weight:600; }
.chips { display:flex; flex-wrap:wrap; gap:6px; margin-bottom:6px; }
    .chip { padding:7px 11px; border-radius:10px; background:rgba(187,158,85,0.12); border:1px solid var(--accent-line); color:var(--text); font-size:13px; font-weight:600; }
    .thumb { width:100%; height:150px; object-fit:cover; border-radius:12px; border:1px solid rgba(70,58,39,0.18); box-shadow:0 8px 16px rgba(42,35,25,0.10); background:#f9f6ef; }
    .radar-box { width:100%; border-radius:12px; border:1px solid rgba(70,58,39,0.18); background:#fffdf8; box-shadow:0 8px 16px rgba(42,35,25,0.08); padding:8px; }
    .radar-box svg { width:100% !important; height:220px !important; display:block; }
    .title-row { display:flex; align-items:center; gap:12px; flex-wrap:wrap; margin:8px 0 14px 0; }
    .stSlider [data-baseweb="slider"] { color:#bb9e55 !important; }
    .stSlider [data-baseweb="slider"] * { accent-color:#bb9e55 !important; }
    input[type="checkbox"], input[type="radio"] { accent-color:#bb9e55; }
/* Masthead inspired by newsroom sites */
.masthead-wrap {
  margin: 0 0 16px 0;
  border: 1px solid rgba(70,58,39,0.18);
}
.masthead-top {
  background: #f3ead5;
  color: #5a513f;
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 12px;
  align-items: center;
  padding: 10px 16px;
}
.masthead-top .mini {
  font-size: 12px;
  letter-spacing: 0.2px;
}
.masthead-top .badge {
  background: #bb9e55;
  color: #fffdf8;
  border-radius: 18px;
  padding: 6px 12px;
  font-weight: 700;
  font-size: 12px;
}
.masthead-main {
  background: linear-gradient(180deg, #efe2c2, #e8d7ae);
  color: #2b2823;
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 20px;
  align-items: end;
  padding: 18px 16px 12px 16px;
}
.masthead-brand {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 56px;
  line-height: 0.95;
  font-weight: 700;
  letter-spacing: -1px;
}
.masthead-nav {
  display: flex;
  gap: 18px;
  align-items: flex-end;
  flex-wrap: wrap;
}
.masthead-nav a {
  color: #5c5344;
  font-weight: 600;
  border-bottom: 3px solid transparent;
  padding-bottom: 8px;
  text-decoration: none;
}
.masthead-nav a.active {
  border-bottom-color: #bb9e55;
  color: #2b2823;
}
.masthead-sub {
  background: #f8f1df;
  color: #5c5344;
  border-top: 1px solid rgba(70,58,39,0.16);
  padding: 8px 16px;
  font-size: 14px;
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
}
.masthead-sub a {
  color: inherit;
  text-decoration: none;
  border-bottom: 1px solid transparent;
}
.masthead-sub a:hover {
  border-bottom-color: #bb9e55;
}
@media (max-width: 900px) {
  .masthead-main { grid-template-columns: 1fr; }
  .masthead-brand { font-size: 40px; }
}
</style>
"""

def _active_class(cond: bool) -> str:
    return "active" if cond else ""


def _qp_get_str(key: str, default: str = "") -> str:
    try:
        v = st.query_params.get(key, default)
    except Exception:
        return default
    if isinstance(v, list):
        return str(v[0]) if v else default
    return str(v)


def build_masthead_html(active_view: str = "items", active_source: str = "", active_column: str = "") -> str:
    return f"""
<div class="masthead-wrap">
  <div class="masthead-top">
    <div class="mini">Signal-driven curation for AI products, repos and research</div>
    <div class="badge">Daily Brief</div>
  </div>
  <div class="masthead-main">
    <div class="masthead-nav">
      <a href="?view=items" class="{_active_class(active_view == 'items')}">Feeds</a>
      <a href="?view=trends" class="{_active_class(active_view == 'trends')}">Trends</a>
      <a href="?view=items&sort=%E8%B6%8B%E5%8A%BF%E5%88%86" class="{_active_class(active_view == 'items')}">Scores</a>
      <a href="?view=items&source=producthunt" class="{_active_class(active_view == 'items' and active_source == 'producthunt')}">Watchlist</a>
      <a href="?view=items&column=openclaw" class="{_active_class(active_view == 'items' and active_column == 'openclaw')}">OpenClaw</a>
      <a href="?view=items&column=claudecode" class="{_active_class(active_view == 'items' and active_column == 'claudecode')}">Claude Code</a>
      <a href="?view=weekly" class="{_active_class(active_view == 'weekly')}">Weekly Research</a>
    </div>
    <div class="masthead-brand">Daily AI Feeds</div>
  </div>
  <div class="masthead-sub">
    <a href="?view=items&source=producthunt">Product Hunt</a>
    <a href="?view=items&source=github">GitHub</a>
    <a href="?view=items&source=arxiv">arXiv</a>
    <a href="?view=items&source=clawhub">ClawHub</a>
    <a href="?view=items&column=openclaw">OpenClaw / Clawdbot 专栏</a>
    <a href="?view=items&column=claudecode">Claude Code 专栏</a>
    <a href="?view=trends">Keyword Trend Intelligence</a>
    <a href="?view=weekly">Weekly Research Report</a>
  </div>
</div>
"""

st.set_page_config(page_title="Daily AI Feeds", layout="wide")
st.markdown(STYLE, unsafe_allow_html=True)
view_param = _qp_get_str("view", "items").lower().strip()
if view_param not in {"items", "trends", "weekly"}:
    view_param = "items"
source_param = _qp_get_str("source", "").strip()
column_param = _qp_get_str("column", "").strip().lower()
sort_param = _qp_get_str("sort", "").strip()
st.markdown(build_masthead_html(active_view=view_param, active_source=source_param, active_column=column_param), unsafe_allow_html=True)

df = load_items(_structured_signature())
if df.empty:
    st.warning("暂无数据，请先生成 structured 数据。")
    st.stop()
df_all = df.copy()

sort_labels = list(SORT_FIELD_OPTIONS.keys())
sort_default = sort_param if sort_param in sort_labels else "趋势分"
sort_index = sort_labels.index(sort_default) if sort_default in sort_labels else 0
if view_param != "weekly":
    sort_label = st.selectbox("关键词趋势排序", sort_labels, index=sort_index)
else:
    sort_label = sort_default
sort_field = SORT_FIELD_OPTIONS[sort_label]

if view_param == "weekly":
    tab_weekly, tab_items, tab_trends = st.tabs(["周度研究", "内容浏览", "关键词趋势"])
elif view_param == "trends":
    tab_trends, tab_items, tab_weekly = st.tabs(["关键词趋势", "内容浏览", "周度研究"])
else:
    tab_items, tab_trends, tab_weekly = st.tabs(["内容浏览", "关键词趋势", "周度研究"])

with tab_items:
    trends = load_keyword_trends(_insights_signature())
    t_keywords = (
        sort_keywords_for_display(trends.get("keywords", []), sort_field=sort_field)
        if trends
        else []
    )

    left_col, right_col = st.columns([5, 1])

    all_date_values = (
        df_all["date"]
        .dropna()
        .astype(str)
        .sort_values(ascending=False)
        .unique()
        .tolist()
    )

    with left_col:
        sources = [""] + sorted(df["source"].dropna().unique().tolist())
        source = source_param if source_param in sources else ""
        columns = ["", "openclaw", "claudecode"]
        column = column_param if column_param in columns else ""

        col1, col2, col3 = st.columns([3, 2, 1])
        with col1:
            q = st.text_input("搜索标题 / 关键词 / 描述", "")
        with col2:
            date_pool_df = df_all
            if source:
                date_pool_df = date_pool_df[date_pool_df["source"].astype(str) == str(source)]
            if column:
                date_pool_df = filter_items(date_pool_df, source=None, q=None, column=column)

            date_values = (
                date_pool_df["date"]
                .dropna()
                .astype(str)
                .sort_values(ascending=False)
                .unique()
                .tolist()
            ) if not date_pool_df.empty else []
            if not date_values:
                date_values = all_date_values

            date_state_key = f"date_choice_{source or 'all'}_{column or 'all'}"
            if date_state_key not in st.session_state or st.session_state[date_state_key] not in date_values:
                st.session_state[date_state_key] = date_values[0]

            if column in {"openclaw", "claudecode"} and len(date_values) > 1:
                nav_l, nav_c, nav_r = st.columns([1, 2, 1])
                current_date = str(st.session_state[date_state_key])
                current_idx = date_values.index(current_date) if current_date in date_values else 0

                with nav_l:
                    # Keep arrow buttons baseline-aligned with the date selectbox control.
                    st.markdown("<div style='height: 2.05rem;'></div>", unsafe_allow_html=True)
                    older_disabled = current_idx >= len(date_values) - 1
                    if st.button("←", key=f"older_{date_state_key}", use_container_width=True, disabled=older_disabled):
                        st.session_state[date_state_key] = date_values[current_idx + 1]

                # 重新读取，确保按钮点击后本次渲染生效
                current_date = str(st.session_state[date_state_key])
                current_idx = date_values.index(current_date) if current_date in date_values else 0

                with nav_c:
                    date_choice = st.selectbox("日期", date_values, key=date_state_key)

                with nav_r:
                    st.markdown("<div style='height: 2.05rem;'></div>", unsafe_allow_html=True)
                    newer_disabled = current_idx <= 0
                    if st.button("→", key=f"newer_{date_state_key}", use_container_width=True, disabled=newer_disabled):
                        st.session_state[date_state_key] = date_values[current_idx - 1]
            else:
                date_choice = st.selectbox("日期", date_values, key=date_state_key)
        with col3:
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

        df_f = filter_items(df_items, source or None, q or None, column or None)
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
        st.caption(f"共 {len(df_f)} 条")

        for _, row in df_f.iterrows():
            row_dict = row.to_dict() if hasattr(row, "to_dict") else dict(row)
            radar_svg = build_score_radar_svg(row_dict)
            st.markdown(card_html(row_dict, radar_svg=radar_svg), unsafe_allow_html=True)
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
                    f"<span style='font-weight:700;color:#2b2823;'>{idx}.</span>"
                    f"<span style='font-weight:600;color:#2b2823;'>{escape(kw)}</span>"
                    f"<span style='font-size:12px;color:{trend_color};font-weight:600;'>{trend_text}</span>"
                    f"<span style='margin-left:auto;color:{color};font-weight:700;'>"
                    f"{score:.2f}</span></div>"
                    f"<div style='font-size:11px;color:#6e6658;margin:2px 0 4px 24px;'>z={trend_z:.2f}</div>",
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
                    mini_chart = (
                        alt.layer(mini_area, mini_line, mini_points)
                        .properties(height=70)
                        .configure(background="transparent")
                        .configure_view(fill="#fffdf8", stroke="rgba(70,58,39,0.18)")
                    )
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
                chart = (
                    alt.layer(area, line, points)
                    .properties(height=160)
                    .configure(background="transparent")
                    .configure_view(fill="#fffdf8", stroke="rgba(70,58,39,0.18)")
                    .configure_axis(
                        labelColor="#6e6658",
                        titleColor="#6e6658",
                        domainColor="rgba(70,58,39,0.28)",
                        gridColor="rgba(70,58,39,0.12)",
                        tickColor="rgba(70,58,39,0.28)",
                    )
                )
                st.altair_chart(chart, use_container_width=True)

with tab_weekly:
    render_weekly_report_view(BASE_DIR)
