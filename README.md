# CreekStone SearchBot

一个面向 AI 产品/论文/开源项目的自动化数据流水线：
- 每日抓取 **Product Hunt / arXiv / GitHub Trending**
- 做 AI 相关筛选、翻译、关键词提取、投资视角评分
- 同时输出 Markdown 与结构化数据（NDJSON / Parquet）
- 提供 Streamlit 页面用于检索与浏览

## 主要功能

- 三源自动抓取与定时运行（GitHub Actions）
- AI 关键词包含/排除筛选（PH、GitHub）
- 统一评分体系（`common/scoring.py`）
- 统一结构化存储（`common/storage.py`）
- 按日期浏览的 Streamlit UI（`webapp/streamlit_app.py`）

## 目录结构

```text
.
├── common/
│   ├── scoring.py              # 评分逻辑（LLM）
│   └── storage.py              # NDJSON / Parquet 存储
├── scripts/
│   ├── product_hunt_list_to_md.py
│   ├── arxiv_papers_to_md.py
│   └── github_trending_to_md.py
├── data/
│   ├── producthunt/            # 每日 PH Markdown
│   ├── arxiv/                  # 每日 arXiv Markdown
│   ├── github/                 # 每日 GitHub Markdown
│   └── structured/             # items.ndjson + YYYY-MM-DD.parquet
├── webapp/
│   └── streamlit_app.py
├── .github/workflows/
│   ├── generate_markdown.yml
│   ├── fetch_arxiv.yml
│   └── fetch_github_trending.yml
└── app.py                      # Streamlit Cloud 入口
```

## 环境要求

- Python 3.10+
- `requirements.txt` 中依赖
- OpenAI 兼容 API（用于翻译、摘要、评分）
- Product Hunt token（仅 PH 抓取需要）

## 本地运行

### 1) 安装依赖

```bash
pip install -r requirements.txt
```

### 2) 配置环境变量

创建 `.env`（可参考 `.env.example`），常用项：

- `OPENAI_API_KEY`
- `OPENAI_BASE_URL`（可选）
- `PRODUCTHUNT_DEVELOPER_TOKEN`
- `SCORING_MODEL_NAME`（可选，默认 `gpt-4o-mini`）

### 3) 运行抓取

```bash
python scripts/product_hunt_list_to_md.py
python scripts/arxiv_papers_to_md.py
python scripts/github_trending_to_md.py
```

### 4) 快速测试

```bash
./test_all_sources.sh
```

## Streamlit 页面

本地启动：

```bash
streamlit run app.py
```

页面特性：
- 按日期切换
- 按来源筛选
- 关键词/描述搜索
- 项目卡片展示评分、关键词、图片（有图才占右侧区域）

## GitHub Actions 自动化

工作流：
- `generate_markdown.yml`（Product Hunt）
- `fetch_arxiv.yml`（arXiv）
- `fetch_github_trending.yml`（GitHub Trending）

需要在仓库设置：
- **Secrets**：`OPENAI_API_KEY`, `OPENAI_BASE_URL`, `PRODUCTHUNT_DEVELOPER_TOKEN`, `PAT`
- **Variables（可选）**：`ARXIV_*`, `GITHUB_*`

## Streamlit Community Cloud 部署

已准备好部署入口：
- 主文件：`app.py`
- 配置：`.streamlit/config.toml`

详细步骤见：`STREAMLIT_CLOUD_DEPLOY.md`

## 说明

- arXiv 默认按“前一天”日期生成（避免当天数据不完整）
- 结构化数据优先用于页面展示；Parquet 写失败时请优先检查 `pyarrow` 与日志

## License

MIT
