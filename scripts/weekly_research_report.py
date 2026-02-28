from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception:
    pass

import openai

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from common.weekly_research import (  # noqa: E402
    INSIGHTS_WEEKLY_DIR,
    add_term_sets,
    build_event_frame,
    build_keyword_boards,
    build_weekly_payload,
    cluster_projects,
    compile_markdown_report,
    compute_project_trends,
    compute_term_trends,
    embed_texts,
    generate_theme_cards,
    load_structured_items,
    render_markdown_from_payload,
    resolve_week_window,
    select_candidate_projects,
    build_cross_source_observations,
    build_embedding_text,
    write_weekly_outputs,
)


def _get_base_url(default: str = "https://api.openai.com/v1") -> str:
    raw = os.getenv("OPENAI_BASE_URL", "").strip()
    return raw or default


def _get_chat_model() -> str:
    return os.getenv("WEEKLY_REPORT_CHAT_MODEL", "").strip() or os.getenv("OPENAI_MODEL", "").strip() or "gpt-5.2-2025-12-11"


def _get_embedding_model() -> str:
    return os.getenv("OPENAI_EMBEDDING_MODEL", "").strip() or "text-embedding-3-large"


def _require_client() -> openai.Client:
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is required for weekly research report")
    return openai.Client(api_key=api_key, base_url=_get_base_url())


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate weekly research report")
    parser.add_argument("--week-start", dest="week_start", help="Target week start (YYYY-MM-DD, Monday preferred)")
    parser.add_argument("--force", action="store_true", help="Regenerate even if output exists")
    parser.add_argument("--depth", default="deep", choices=["light", "standard", "deep"], help="Report depth")
    return parser.parse_args()


def _week_slug(week_start_str: str) -> str:
    y, m, d = [int(part) for part in week_start_str.split("-")]
    import datetime as _dt

    iso = _dt.date(y, m, d).isocalendar()
    return f"{iso.year}-{iso.week:02d}"


def _theme_target_for_depth(depth: str) -> int:
    return {"light": 5, "standard": 8, "deep": 10}.get(depth, 10)


def main() -> int:
    args = _parse_args()
    window = resolve_week_window(args.week_start)
    week_slug = _week_slug(window.week_start.isoformat())
    target_json = INSIGHTS_WEEKLY_DIR / f"weekly-report-{week_slug}.json"
    target_md = INSIGHTS_WEEKLY_DIR / f"weekly-report-{week_slug}.md"

    if target_json.exists() and target_md.exists() and not args.force:
        print(f"已存在周报产物，跳过生成: {target_json.name}")
        return 0

    print(f"[weekly] 目标周: {window.week_start.isoformat()} ~ {window.week_end.isoformat()}")
    print(f"[weekly] 报告深度: {args.depth} | 目标主题数: {_theme_target_for_depth(args.depth)}")

    df = load_structured_items()
    if df.empty:
        raise RuntimeError("structured data is empty")

    events = build_event_frame(df)
    if events.empty:
        raise RuntimeError("no valid events after normalization")
    print(f"[weekly] 事件总数: {len(events)}")

    events = add_term_sets(events)
    project_result = compute_project_trends(events, window)
    week_events = project_result.get("week_events")
    if week_events is None or week_events.empty:
        raise RuntimeError(f"no events found for target week {window.week_start.isoformat()} ~ {window.week_end.isoformat()}")
    print(f"[weekly] 目标周项目数: {len(week_events)}")

    term_result = compute_term_trends(project_result["events"], window)
    print(f"[weekly] 候选术语数: {len(term_result.get('terms', []))}")
    candidate_projects = select_candidate_projects(week_events, term_result.get("terms", []), term_result.get("term_to_items", {}))
    if candidate_projects.empty:
        raise RuntimeError("no candidate projects selected for clustering")
    print(f"[weekly] 参与聚类项目数: {len(candidate_projects)}")

    client = _require_client()
    embedding_model = _get_embedding_model()
    chat_model = _get_chat_model()

    embed_texts_input = [build_embedding_text(row) for _, row in candidate_projects.iterrows()]
    print(f"[weekly] 请求 embeddings: {len(embed_texts_input)} 条")
    vectors = embed_texts(client, embed_texts_input, embedding_model)
    print("[weekly] 开始聚类")
    clustering = cluster_projects(
        candidate_projects,
        vectors,
        term_result.get("terms", []),
        target_theme_count=_theme_target_for_depth(args.depth),
    )
    clusters = clustering.get("clusters", [])
    if not clusters:
        raise RuntimeError("clustering produced no valid themes")
    print(f"[weekly] 有效主题簇: {len(clusters)}")

    themes, theme_models = generate_theme_cards(clusters, client, chat_model)
    cross_source_observations = build_cross_source_observations(themes)
    keyword_boards = build_keyword_boards(term_result)
    project_boards = {
        "rising_top": project_result.get("rising_top", []),
        "hot_top": project_result.get("hot_top", []),
        "novel_top": project_result.get("novel_top", []),
    }

    markdown_body, qa_result, report_models = compile_markdown_report(
        themes,
        project_boards,
        keyword_boards,
        cross_source_observations,
        window.week_start.isoformat(),
        window.week_end.isoformat(),
        client,
        chat_model,
        args.depth,
    )
    payload = build_weekly_payload(
        events=project_result["events"],
        project_result=project_result,
        term_result=term_result,
        clustering=clustering,
        themes=themes,
        markdown=markdown_body,
        qa_result=qa_result,
        window=window,
        embedding_model=embedding_model,
        chat_models_used=sorted(set(theme_models | report_models)),
        report_depth=args.depth,
        semantic_map=clustering.get("semantic_map", []),
    )
    final_markdown = render_markdown_from_payload(payload)
    json_path, md_path = write_weekly_outputs(payload, final_markdown, window)

    print(f"周报 JSON 已写入: {json_path}")
    print(f"周报 Markdown 已写入: {md_path}")
    print(f"周报主题数: {len(payload.get('report', {}).get('themes', []))}")
    print(f"周报 QA 通过: {payload.get('meta', {}).get('qa_pass')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
