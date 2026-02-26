"""Generate special topic columns from structured items.

Outputs Markdown files under data/columns/<column>/<column>-YYYY-MM-DD.md.

Columns:
- openclaw: items mentioning OpenClaw/Clawdbot/MCP
- claudecode: items mentioning Claude Code / ClaudeCode

This is intentionally lightweight and does not require credentials.

Usage:
  python scripts/generate_columns.py
  COLUMN_TARGET_DATE=2026-02-24 python scripts/generate_columns.py

Env:
  COLUMN_TARGET_DATE: only generate for one date
  COLUMN_FORCE: if true, overwrite existing files
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

BASE_DIR = Path(__file__).resolve().parent.parent
STRUCTURED_DIR = BASE_DIR / "data" / "structured"
OUT_DIR = BASE_DIR / "data" / "columns"


@dataclass(frozen=True)
class ColumnSpec:
    key: str
    title: str
    keywords: tuple[str, ...]


COLUMNS: list[ColumnSpec] = [
    ColumnSpec(
        key="openclaw",
        title="OpenClaw / Clawdbot 专栏",
        # Keep strict to avoid pulling in generic MCP projects.
        keywords=("openclaw", "clawdbot", "clawhub"),
    ),
    ColumnSpec(
        key="claudecode",
        title="Claude Code 专栏",
        keywords=("claude code", "claudecode"),
    ),
]


def _iter_ndjson_rows() -> Iterable[dict]:
    nd = STRUCTURED_DIR / "items.ndjson"
    if not nd.exists():
        return []
    rows: list[dict] = []
    with nd.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except Exception:
                continue
    return rows


def _norm_text(x) -> str:
    if x is None:
        return ""
    if isinstance(x, (list, tuple, set)):
        return " ".join([str(i) for i in x])
    return str(x)


def _item_text(item: dict) -> str:
    parts = [
        _norm_text(item.get("title")),
        _norm_text(item.get("description_en")),
        _norm_text(item.get("description_zh")),
        _norm_text(item.get("keywords")),
        _norm_text(item.get("tags")),
    ]
    return "\n".join([p for p in parts if p]).lower()


def _match(item: dict, spec: ColumnSpec) -> bool:
    text = _item_text(item)
    return any(k in text for k in spec.keywords)


def _safe_filename(s: str) -> str:
    return "".join(ch for ch in s if ch.isalnum() or ch in "-_.").strip(".")


def _write_column_md(spec: ColumnSpec, date_str: str, items: list[dict], force: bool) -> Path | None:
    if not items:
        return None
    out_sub = OUT_DIR / spec.key
    out_sub.mkdir(parents=True, exist_ok=True)
    out_path = out_sub / f"{_safe_filename(spec.key)}-{date_str}.md"
    if out_path.exists() and not force:
        return out_path

    lines: list[str] = []
    lines.append(f"# {spec.title} | {date_str}")
    lines.append("")
    lines.append(f"> 共 {len(items)} 条（来自 Product Hunt / GitHub / arXiv 的聚合数据）")
    lines.append("")

    for idx, it in enumerate(items, start=1):
        title = str(it.get("title", "")).strip() or "(untitled)"
        url = str(it.get("url", "")).strip() or "#"
        source = str(it.get("source", "")).strip()
        desc = (it.get("description_zh") or it.get("description_en") or "").strip()
        score = None
        sc = it.get("score")
        if isinstance(sc, dict):
            score = sc.get("total")

        meta_bits = [b for b in [source, f"score={score}" if score is not None else ""] if b]
        meta = " · ".join(meta_bits)

        lines.append(f"## {idx}. [{title}]({url})")
        if meta:
            lines.append(f"**{meta}**")
        if desc:
            lines.append("")
            lines.append(desc)
        lines.append("\n---\n")

    out_path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    return out_path


def main() -> None:
    target_date = os.getenv("COLUMN_TARGET_DATE", "").strip()
    force = os.getenv("COLUMN_FORCE", "").strip().lower() in {"1", "true", "yes"}

    rows = list(_iter_ndjson_rows())
    if not rows:
        print("No structured items found (data/structured/items.ndjson missing or empty).")
        return

    # group by date
    by_date: dict[str, list[dict]] = {}
    for r in rows:
        d = str(r.get("date", "")).strip()
        if not d:
            continue
        if target_date and d != target_date:
            continue
        by_date.setdefault(d, []).append(r)

    if not by_date:
        print("No rows matched target date.")
        return

    for date_str, items in sorted(by_date.items(), reverse=True):
        for spec in COLUMNS:
            matched = [it for it in items if _match(it, spec)]
            path = _write_column_md(spec, date_str, matched, force=force)
            if path and matched:
                print(f"[{spec.key}] {date_str}: {len(matched)} items -> {path}")


if __name__ == "__main__":
    main()
