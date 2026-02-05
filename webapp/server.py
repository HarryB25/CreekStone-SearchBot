import os
import glob
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Optional

import pandas as pd
from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent.parent
STRUCTURED_DIR = BASE_DIR / "data" / "structured"

# 确保项目根在 sys.path，避免 uvicorn reload 子进程找不到 webapp 包
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

app = FastAPI(title="Daily AI Feeds")
templates = Jinja2Templates(directory=str(BASE_DIR / "webapp" / "templates"))


def load_items() -> pd.DataFrame:
    """Load all parquet files under data/structured; fallback to ndjson."""
    files = sorted(STRUCTURED_DIR.glob("*.parquet"))
    dfs = []
    for f in files:
        try:
            dfs.append(pd.read_parquet(f))
        except Exception as e:
            print(f"Failed to read {f}: {e}")
    if dfs:
        df = pd.concat(dfs, ignore_index=True)
    else:
        ndjson_path = STRUCTURED_DIR / "items.ndjson"
        if ndjson_path.exists():
            records = [json.loads(line) for line in ndjson_path.open()]
            df = pd.DataFrame(records)
        else:
            df = pd.DataFrame()
    if not df.empty:
        # ensure keywords as list
        if "keywords" in df.columns:
            df["keywords"] = df["keywords"].apply(lambda x: x if isinstance(x, list) else [])
        # convert date string to datetime for sort
        if "date" in df.columns:
            df["date_dt"] = pd.to_datetime(df["date"], errors="coerce")
            df = df.sort_values(by=["date_dt", "rank"], ascending=[False, True])
    return df


def filter_items(df: pd.DataFrame, source: Optional[str], q: Optional[str]) -> pd.DataFrame:
    if df.empty:
        return df
    if source:
        df = df[df["source"] == source]
    if q:
        q_lower = q.lower()
        def match(row):
            haystack = " ".join([
                str(row.get("title", "")),
                str(row.get("description_zh", "")),
                str(row.get("description_en", "")),
                " ".join(row.get("keywords", []))
            ]).lower()
            return q_lower in haystack
        df = df[df.apply(match, axis=1)]
    return df


@app.get("/", response_class=HTMLResponse)
def index(request: Request,
          source: Optional[str] = Query(default=None),
          q: Optional[str] = Query(default=None),
          limit: int = Query(default=50, le=200)):
    df = load_items()
    df = filter_items(df, source, q)
    items = df.head(limit).to_dict(orient="records") if not df.empty else []
    sources = sorted(df["source"].unique().tolist()) if not df.empty else []
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "items": items,
            "sources": sources,
            "current_source": source,
            "q": q or "",
            "count": len(items),
            "limit": limit,
        }
    )


@app.get("/api/items", response_class=JSONResponse)
def api_items(source: Optional[str] = None,
              q: Optional[str] = None,
              limit: int = 200):
    df = load_items()
    df = filter_items(df, source, q)
    items = df.head(limit).to_dict(orient="records") if not df.empty else []
    return {"items": items, "total": len(df)}


if __name__ == "__main__":
    import uvicorn
    # 使用模块字符串，reload 不再警告；sys.path 已加入项目根保证可导入
    uvicorn.run(
        "webapp.server:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        reload=True,
    )
