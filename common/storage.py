import os
import json
from typing import List, Dict

STRUCTURED_DIR = os.path.join("data", "structured")


def build_item_id(prefix: str, date_str: str, rank: int, extra: str = "") -> str:
    extra_part = f"-{extra}" if extra else ""
    return f"{prefix}-{date_str}-{rank}{extra_part}"


def _append_ndjson(items: List[Dict]):
    if not items:
        return
    os.makedirs(STRUCTURED_DIR, exist_ok=True)
    ndjson_path = os.path.join(STRUCTURED_DIR, "items.ndjson")
    with open(ndjson_path, "a", encoding="utf-8") as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")


def _write_parquet(date_str: str, items: List[Dict]):
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
            df = pd.concat([df_old, df_new], ignore_index=True)
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
    _append_ndjson(items)
    _write_parquet(date_str, items)
