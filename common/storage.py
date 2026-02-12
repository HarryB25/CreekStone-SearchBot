import os
import json
from typing import List, Dict

STRUCTURED_DIR = os.path.join("data", "structured")


def build_item_id(prefix: str, date_str: str, rank: int, extra: str = "") -> str:
    extra_part = f"-{extra}" if extra else ""
    return f"{prefix}-{date_str}-{rank}{extra_part}"


def _append_ndjson(items: List[Dict], replace_source: str = "", replace_date: str = ""):
    if not items:
        return
    os.makedirs(STRUCTURED_DIR, exist_ok=True)
    ndjson_path = os.path.join(STRUCTURED_DIR, "items.ndjson")
    existing_rows: List[Dict] = []
    existing_index_by_id = {}
    if os.path.exists(ndjson_path):
        with open(ndjson_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    continue
                existing_rows.append(row)
                row_id = row.get("id")
                if row_id:
                    existing_index_by_id[str(row_id)] = len(existing_rows) - 1

    if replace_source and replace_date:
        existing_rows = [
            row
            for row in existing_rows
            if not (
                str(row.get("source", "")).lower() == replace_source
                and str(row.get("date", "")) == replace_date
            )
        ]
        existing_index_by_id = {}
        for idx, row in enumerate(existing_rows):
            row_id = row.get("id")
            if row_id:
                existing_index_by_id[str(row_id)] = idx

    inserted = 0
    updated = 0
    for item in items:
        item_id = item.get("id")
        if item_id:
            item_key = str(item_id)
            if item_key in existing_index_by_id:
                existing_rows[existing_index_by_id[item_key]] = item
                updated += 1
            else:
                existing_index_by_id[item_key] = len(existing_rows)
                existing_rows.append(item)
                inserted += 1
        else:
            # 无 id 的记录无法稳定去重，保持追加行为
            existing_rows.append(item)
            inserted += 1

    if inserted == 0 and updated == 0:
        print("NDJSON 无新增/更新，已跳过写入。")
        return

    with open(ndjson_path, "w", encoding="utf-8") as f:
        for row in existing_rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"已写入 NDJSON 数据: {ndjson_path} ({inserted} 条新增, {updated} 条更新)")


def _write_parquet(date_str: str, items: List[Dict], replace_source: str = "", replace_date: str = ""):
    """Append items into per-day parquet; requires pandas+pyarrow."""
    if not items:
        return
    try:
        import pandas as pd  # type: ignore
    except ImportError as e:
        print(f"pandas/pyarrow 未安装，跳过 parquet 保存: {e}")
        return

    os.makedirs(STRUCTURED_DIR, exist_ok=True)
    path = os.path.join(STRUCTURED_DIR, f"{date_str}.parquet")
    # pyarrow 无法写入“空 struct”，将空 dict 统一置为 None
    sanitized = []
    for item in items:
        fixed = {}
        for k, v in item.items():
            if isinstance(v, dict) and not v:
                fixed[k] = None
            else:
                fixed[k] = v
        sanitized.append(fixed)

    df_new = pd.DataFrame(sanitized)
    if os.path.exists(path):
        try:
            df_old = pd.read_parquet(path)
            if replace_source and replace_date and {"source", "date"}.issubset(df_old.columns):
                mask = (
                    df_old["source"].astype(str).str.lower().eq(replace_source)
                    & df_old["date"].astype(str).eq(replace_date)
                )
                df_old = df_old[~mask]
            df = pd.concat([df_old, df_new], ignore_index=True)
            if "id" in df.columns:
                df.drop_duplicates(subset=["id"], keep="last", inplace=True)
        except Exception as e:  # 读取失败则覆盖
            print(f"读取现有 parquet 失败，将覆盖写入: {e}")
            df = df_new
    else:
        df = df_new

    df.to_parquet(path, index=False)
    print(f"已写入结构化数据: {path} ({len(df_new)} 条新增)")


def save_structured_items(date_str: str, items: List[Dict]):
    """同时保存到 NDJSON（追加）与按日 Parquet。"""
    if not items:
        print("无结构化数据可写入，已跳过。")
        return
    source_set = {str(item.get("source", "")).lower() for item in items if item.get("source")}
    date_set = {str(item.get("date", "")) for item in items if item.get("date")}
    replace_source = next(iter(source_set), "")
    replace_date = next(iter(date_set), "")
    if len(source_set) != 1 or len(date_set) != 1:
        replace_source = ""
        replace_date = ""
    _append_ndjson(items, replace_source=replace_source, replace_date=replace_date)
    _write_parquet(date_str, items, replace_source=replace_source, replace_date=replace_date)
