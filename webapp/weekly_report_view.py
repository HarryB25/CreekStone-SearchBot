from __future__ import annotations

import json
from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st


def _weekly_dir(base_dir: Path) -> Path:
    return base_dir / "data" / "insights" / "weekly"


def _available_report_files(base_dir: Path) -> list[Path]:
    weekly_dir = _weekly_dir(base_dir)
    if not weekly_dir.exists():
        return []
    files = [path for path in weekly_dir.glob("weekly-report-*.json") if path.is_file()]
    return sorted(files, reverse=True)


def _load_report(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _report_options(base_dir: Path) -> tuple[list[str], dict[str, Path]]:
    files = _available_report_files(base_dir)
    mapping = {path.stem.replace("weekly-report-", ""): path for path in files}
    return list(mapping.keys()), mapping


def _safe_list(value) -> list:
    return value if isinstance(value, list) else []


def _safe_dict(value) -> dict:
    return value if isinstance(value, dict) else {}


def render_weekly_report_view(base_dir: Path) -> None:
    options, mapping = _report_options(base_dir)
    latest_path = _weekly_dir(base_dir) / "latest.json"

    if not options and not latest_path.exists():
        st.warning("暂无周报数据，请先运行：python scripts/weekly_research_report.py")
        return

    choice_options = options if options else ["latest"]
    if st.session_state.pop("weekly_report_pending_latest", False) and options:
        st.session_state["weekly_report_choice"] = options[0]
    elif (
        "weekly_report_choice" not in st.session_state
        or st.session_state["weekly_report_choice"] not in choice_options
    ):
        st.session_state["weekly_report_choice"] = choice_options[0]

    top_left, top_right = st.columns([3, 1])
    with top_left:
        selected = st.selectbox("周报周次", choice_options, key="weekly_report_choice")
    with top_right:
        st.markdown("<div style='height: 2.05rem;'></div>", unsafe_allow_html=True)
        if st.button("加载最新周", key="weekly_report_latest", use_container_width=True):
            if options:
                st.session_state["weekly_report_pending_latest"] = True
                st.rerun()

    report_path = mapping.get(selected) if selected in mapping else latest_path
    payload = _load_report(report_path)
    if not payload:
        st.error(f"读取周报失败：{report_path.name}")
        return

    meta = _safe_dict(payload.get("meta"))
    report = _safe_dict(payload.get("report"))
    signals = _safe_dict(payload.get("signals"))
    themes = _safe_list(report.get("themes"))
    project_boards = _safe_dict(report.get("project_boards"))
    keyword_boards = _safe_dict(report.get("keyword_boards"))
    cross_obs = _safe_list(report.get("cross_source_observations"))
    watchlist = _safe_list(report.get("watchlist"))
    citations = _safe_dict(payload.get("citations"))

    main_col, side_col = st.columns([5, 2])

    with side_col:
        st.markdown("**周报概览**")
        st.metric("主题数", len(themes))
        st.metric("来源数", len(_safe_dict(meta.get("source_counts"))))
        st.metric("聚类 K", int(meta.get("k_selected", 0) or 0))
        semantic_diag = _safe_dict(signals.get("semantic_diagnostics"))
        silhouette = semantic_diag.get("silhouette_score")
        if silhouette is not None:
            st.metric("聚类质量", f"{float(silhouette):.3f}")
        st.metric("QA 状态", "通过" if meta.get("qa_pass", False) else "待人工复核")
        st.caption(f"区间：{meta.get('week_start', '')} ~ {meta.get('week_end', '')}")
        st.caption(f"Embedding：{meta.get('embedding_model', '')}")
        st.caption(f"Chat：{meta.get('chat_model', '')}")
        issues = _safe_list(meta.get("qa_issues"))
        if issues:
            st.markdown("**QA 问题**")
            for issue in issues[:6]:
                if isinstance(issue, dict):
                    st.write(f"- {issue.get('type', 'issue')}: {issue.get('message', '')}")
                else:
                    st.write(f"- {issue}")

    with main_col:
        st.markdown("## 本周摘要")
        summary_bullets = _safe_list(report.get("summary_bullets"))
        if summary_bullets:
            for bullet in summary_bullets:
                st.markdown(f"- {bullet}")
        else:
            markdown_body = str(report.get("markdown", "")).strip()
            if markdown_body:
                st.caption("当前未返回结构化摘要，以下为完整周报正文。")
                st.markdown(markdown_body)
            else:
                st.caption("本周摘要暂不可用。")

        st.markdown("## 语义层聚类")
        semantic_points = _safe_list(signals.get("semantic_map"))
        if semantic_points:
            points_df = pd.DataFrame(semantic_points)
            points_df["cluster_label"] = points_df["cluster_id"].apply(lambda x: f"Cluster {x}")
            points_df["label"] = points_df.apply(
                lambda r: f"{r['source']}:{r['id']} | hot={r['hot']} | rise={r['rise']}",
                axis=1,
            )
            cluster_meta = {int(_safe_dict(theme).get("cluster_id", -1)): _safe_dict(theme) for theme in themes}
            points_df["theme_title"] = points_df["cluster_id"].apply(
                lambda cid: str(cluster_meta.get(int(cid), {}).get("theme_title", f"Cluster {cid}"))
            )
            chart = (
                alt.Chart(points_df)
                .mark_circle(size=90, opacity=0.78)
                .encode(
                    x=alt.X("x:Q", title="Semantic X"),
                    y=alt.Y("y:Q", title="Semantic Y"),
                    color=alt.Color("cluster_label:N", title="Cluster"),
                    tooltip=[
                        alt.Tooltip("theme_title:N", title="Theme"),
                        alt.Tooltip("title:N", title="Project"),
                        alt.Tooltip("source:N", title="Source"),
                        alt.Tooltip("hot:Q", title="Hot"),
                        alt.Tooltip("rise:Q", title="Rise"),
                        alt.Tooltip("score_total:Q", title="Score"),
                    ],
                )
                .properties(height=360)
                .configure_view(stroke="rgba(70,58,39,0.18)")
                .configure_axis(
                    labelColor="#6e6658",
                    titleColor="#6e6658",
                    domainColor="rgba(70,58,39,0.28)",
                    gridColor="rgba(70,58,39,0.12)",
                    tickColor="rgba(70,58,39,0.28)",
                )
            )
            st.altair_chart(chart, use_container_width=True)

            diag_cols = st.columns([1, 1])
            with diag_cols[0]:
                st.caption(
                    f"二维投影点数：{len(points_df)} | silhouette={float(silhouette):.3f}"
                    if silhouette is not None
                    else f"二维投影点数：{len(points_df)}"
                )
            with diag_cols[1]:
                st.caption("每个点是一个候选项目；颜色表示 KMeans 聚类簇。")

            st.markdown("**聚类诊断**")
            for theme in themes:
                theme = _safe_dict(theme)
                cluster_id = theme.get("cluster_id", "")
                member_count = theme.get("member_count", len(_safe_list(theme.get("member_project_ids"))))
                top_terms = " / ".join([str(term) for term in _safe_list(theme.get("key_terms"))[:6]])
                st.markdown(
                    f"- `Cluster {cluster_id}` | **{theme.get('theme_title', '')}** | 成员 {member_count} | 来源 {', '.join(_safe_list(theme.get('source_mix')))}"
                )
                if top_terms:
                    st.caption(f"核心语义锚点：{top_terms}")
        else:
            st.caption("当前周报未包含语义层投影数据。")

        st.markdown("## 趋势主题")
        for idx, theme in enumerate(themes, start=1):
            theme = _safe_dict(theme)
            title = str(theme.get("theme_title", "")).strip() or f"Theme {idx}"
            summary = str(theme.get("one_sentence_summary", "")).strip()
            why_now = str(theme.get("why_now", "")).strip()
            score = theme.get("cluster_score", "")
            source_mix = ", ".join(_safe_list(theme.get("source_mix")))

            with st.expander(f"{idx}. {title}  |  score={score}", expanded=idx <= 2):
                if summary:
                    st.markdown(f"**一句话概括**：{summary}")
                if why_now:
                    st.markdown(f"**为什么现在上升**：{why_now}")
                if source_mix:
                    st.caption(f"来源覆盖：{source_mix}")

                key_terms = _safe_list(theme.get("key_terms"))
                if key_terms:
                    st.markdown("**核心关键词**")
                    st.write(" / ".join([str(term) for term in key_terms[:10]]))

                st.markdown("**代表项目**")
                for project in _safe_list(theme.get("top_projects"))[:5]:
                    project = _safe_dict(project)
                    item_id = str(project.get("id", "")).strip()
                    cite = citations.get(item_id, {}) if item_id else {}
                    source = cite.get("source") or project.get("source", "")
                    url = cite.get("url") or project.get("url", "")
                    title_text = cite.get("title") or project.get("title", "")
                    hot = project.get("hot", "")
                    rise = project.get("rise", "")
                    score_total = project.get("score_total", "")
                    link = f"[{title_text}]({url})" if url else title_text
                    st.markdown(
                        f"- `{source}:{item_id}` {link} | hot={hot} | rise={rise} | score={score_total}"
                    )
                    summary_text = str(project.get("summary", "")).strip()
                    if summary_text:
                        st.caption(summary_text)

                risks = _safe_list(theme.get("risks_questions"))
                if risks:
                    st.markdown("**风险 / 待验证问题**")
                    for item in risks[:5]:
                        st.write(f"- {item}")

                next_watch = _safe_list(theme.get("next_week_watchlist"))
                if next_watch:
                    st.markdown("**下周观察**")
                    for item in next_watch[:5]:
                        st.write(f"- {item}")

        st.markdown("## 项目榜单")
        board_tabs = st.tabs(["Rise", "Hot", "Novel"])
        for tab, key in zip(board_tabs, ["rising_top", "hot_top", "novel_top"]):
            with tab:
                rows = _safe_list(project_boards.get(key))
                if not rows:
                    st.caption("暂无数据")
                for idx, row in enumerate(rows[:10], start=1):
                    row = _safe_dict(row)
                    item_id = str(row.get("id", "")).strip()
                    url = str(row.get("url", "")).strip()
                    title = str(row.get("title", "")).strip()
                    source = str(row.get("source", "")).strip()
                    link = f"[{title}]({url})" if url else title
                    st.markdown(
                        f"{idx}. `{source}:{item_id}` {link} | hot={row.get('hot', '')} | rise={row.get('rise', '')} | score={row.get('score_total', '')}"
                    )

        st.markdown("## 关键词趋势")
        keyword_tabs = st.tabs(["新增关键词", "爆发关键词", "退潮关键词"])
        for tab, key in zip(keyword_tabs, ["emerging", "surging", "cooling"]):
            with tab:
                rows = _safe_list(keyword_boards.get(key))
                if not rows:
                    st.caption("暂无数据")
                for idx, row in enumerate(rows[:12], start=1):
                    row = _safe_dict(row)
                    score_key = "cooling_score" if key == "cooling" else "term_trend_score"
                    st.markdown(
                        f"{idx}. **{row.get('term', '')}** | {score_key}={row.get(score_key, '')} | support={row.get('support_projects', '')} | sources={row.get('support_sources', '')}"
                    )

        st.markdown("## 交叉来源观察")
        if not cross_obs:
            st.caption("暂无跨来源观察。")
        for obs in cross_obs:
            obs = _safe_dict(obs)
            st.markdown(f"- **{obs.get('theme_title', '')}**：{obs.get('note', '')}")

        st.markdown("## 下周 Watchlist")
        if not watchlist:
            st.caption("暂无 watchlist。")
        for group in watchlist[:10]:
            group = _safe_dict(group)
            title = str(group.get("theme_title", "")).strip()
            items = _safe_list(group.get("items"))
            if title:
                st.markdown(f"**{title}**")
            for item in items[:5]:
                st.write(f"- {item}")
