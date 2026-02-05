# Product Hunt 每日中文热榜

[English](README.en.md) | [中文](README.md)

![License](https://img.shields.io/github/license/ViggoZ/producthunt-daily-hot) ![Python](https://img.shields.io/badge/python-3.x-blue)

Product Hunt 每日热榜是一个基于 GitHub Action 的自动化工具，它能够每天定时生成 Product Hunt 上的热门产品榜单 Markdown 文件，并自动提交到 GitHub 仓库中。该项目旨在帮助用户快速查看每日的 Product Hunt 热门榜单，并提供更详细的产品信息。

榜单会在每天下午4点自动更新，可以在 [🌐 这里查看](https://decohack.com/category/producthunt/)。

## 预览

![Preview](./preview.gif)

## 功能概述

### Product Hunt 热榜

- **自动获取数据**：每天自动获取前一天的 Product Hunt Top 30 产品数据。
- **关键词生成**：生成简洁易懂的中文关键词，帮助用户更好地理解产品内容。
- **高质量翻译**：使用 OpenAI 的 GPT-4 模型对产品描述进行高质量翻译。
- **Markdown 文件生成**：生成包含产品数据、关键词和翻译描述的 Markdown 文件。
- **每日自动化**：通过 GitHub Actions 自动生成并提交每日的 Markdown 文件。

### arXiv AI 论文日报 🆕

- **自动爬取论文**：每天自动获取 arXiv 最新的 AI 相关论文（cs.AI, cs.LG, cs.CL, cs.CV）
- **AI 结构化总结**：使用 AI 自动生成论文的四个关键部分：
  - 📝 一句话总结（TLDR）
  - 💡 研究动机（Motivation）
  - 🔬 核心方法（Method）
  - 📊 主要结论（Conclusion）
- **智能分类**：按论文分类自动整理，生成带目录的日报
- **中文友好**：所有AI总结均为中文，便于快速理解论文要点

### GitHub Trending 热门项目 🆕

- **实时追踪**：每天自动爬取 GitHub Trending 热门项目
- **多维度筛选**：支持按语言筛选（Python、JavaScript等）
- **详细信息**：包含项目星标、Fork数、今日新增星标等
- **智能翻译**：使用 AI 将项目描述翻译成中文
- **按语言分类**：自动按编程语言分组展示

### 通用特性

- **可配置工作流**：支持手动触发或通过 GitHub Actions 定时生成内容。
- **灵活定制**：脚本易于扩展或修改，可以包括额外的产品细节或调整文件格式。

## 快速开始

### 前置条件

- Python 3.x
- GitHub 账户及仓库
- OpenAI API Key（或兼容的API服务）
- Product Hunt Developer Token (从 Product Hunt 开发者设置页面获取)
- （可选）arXiv 论文功能无需额外配置
- （可选）GitHub Trending 功能无需额外配置（免费爬取）

### 安装

1. **克隆仓库：**

```bash
git clone https://github.com/ViggoZ/producthunt-daily-hot.git
cd producthunt-daily-hot
```

2. **安装 Python 依赖：**

确保您的系统已安装 Python 3.x。然后安装所需的依赖包：

```bash
pip install -r requirements.txt
```

### 设置

#### 1. 本地开发环境配置

如果要在本地运行脚本，需要配置环境变量：

1. 复制 `.env.example` 文件并重命名为 `.env`：
   ```bash
   cp .env.example .env
   ```

2. 编辑 `.env` 文件，填入您的真实配置信息：
   
   **必需配置（Product Hunt）：**
   - `OPENAI_API_KEY`: 您的 OpenAI API 密钥
   - `OPENAI_BASE_URL`: OpenAI API地址（可选，如使用转发服务请修改，默认为官方地址）
   - `PRODUCTHUNT_DEVELOPER_TOKEN`: 您的 Product Hunt Developer Token
   
   **可选配置（arXiv论文）：**
   - `ARXIV_CATEGORIES`: arXiv论文分类，默认为 `cs.AI,cs.LG,cs.CL,cs.CV`
   - `ARXIV_MAX_RESULTS`: 每日获取的最大论文数量，默认为 `10`
   - `ARXIV_MODEL_NAME`: arXiv摘要使用的模型，默认为 `gpt-4o-mini`

**注意**：
- `.env` 文件包含敏感信息，已被 `.gitignore` 忽略，不会提交到Git仓库。
- 如果使用第三方OpenAI API转发服务，需要修改 `OPENAI_BASE_URL`（例如：`https://llmxapi.com/v1`）

#### 2. GitHub Actions 自动化配置

如果要使用 GitHub Actions 自动运行，需要在 GitHub 仓库中添加 Secrets：

1. 打开您的 GitHub 仓库
2. 点击 **Settings（设置）** → **Secrets and variables** → **Actions**
3. 点击 **New repository secret** 添加以下 Secrets：

   **必需（Product Hunt）：**
   - `OPENAI_API_KEY`: 您的 OpenAI API 密钥
   - `OPENAI_BASE_URL`: OpenAI API地址（可选，使用转发服务时需要配置）
   - `PRODUCTHUNT_DEVELOPER_TOKEN`: 您的 Product Hunt Developer Token
   - `PAT`: 用于推送更改到仓库的个人访问令牌
   
   **可选（arXiv论文）：**
   - `ARXIV_CATEGORIES`: arXiv论文分类（如 `cs.AI,cs.LG,cs.CL,cs.CV`）
   - `ARXIV_MAX_RESULTS`: 每日获取论文数量（如 `10`）
   - `ARXIV_MODEL_NAME`: 模型名称（如 `gpt-4o-mini`）
   
   **可选（GitHub Trending）：**
   - `GITHUB_LANGUAGE`: 编程语言（如 `python`、`javascript`，留空表示全部）
   - `GITHUB_SINCE`: 时间范围（`daily`、`weekly`、`monthly`）
   - `GITHUB_MAX_RESULTS`: 最大项目数量（如 `25`）
   - `GITHUB_MODEL_NAME`: 模型名称（如 `gpt-4o-mini`）

#### 3. 获取必要的API密钥和令牌

**OpenAI API Key：**
- 访问 [OpenAI API Keys](https://platform.openai.com/api-keys)
- 创建一个新的API密钥

**Product Hunt Developer Token：**
- 访问 [Product Hunt 开发者设置页面](https://www.producthunt.com/v2/oauth/applications)
- 登录您的账户
- 在开发者设置中创建一个新的应用
- 获取 Developer Token

**GitHub Personal Access Token（仅GitHub Actions需要）：**
- 访问 [GitHub Token 设置](https://github.com/settings/tokens)
- 创建一个新的token，授予 `repo` 权限

#### 4. GitHub Actions 工作流

项目包含三个自动化工作流：

1. **Product Hunt 热榜**（`generate_markdown.yml`）
   - 每天 UTC 时间 07:01（北京时间 15:01）自动运行
   - 也可以手动触发

2. **arXiv AI 论文日报**（`fetch_arxiv.yml`）
   - 每天 UTC 时间 08:01（北京时间 16:01）自动运行
   - 也可以手动触发

3. **GitHub Trending 热门项目**（`fetch_github_trending.yml`）🆕
   - 每天 UTC 时间 09:01（北京时间 17:01）自动运行
   - 也可以手动触发
   - 如不需要某功能，可删除对应的workflow文件

### 使用

设置完成后，GitHub Action 将自动运行：

- **Product Hunt 热榜**：每天生成 `data/producthunt/producthunt-daily-YYYY-MM-DD.md` 文件
- **arXiv AI 论文日报**：每天生成 `data/arxiv/arxiv-daily-YYYY-MM-DD.md` 文件
- **GitHub Trending**：每天生成 `data/github/github-trending-YYYY-MM-DD.md` 文件

文件按数据源分类存储：
```
data/
├── producthunt/    # Product Hunt 热榜文件
│   └── producthunt-daily-YYYY-MM-DD.md
├── arxiv/          # arXiv AI 论文日报文件
│   └── arxiv-daily-YYYY-MM-DD.md
└── github/         # GitHub Trending 热门项目文件
    └── github-trending-YYYY-MM-DD.md
```

### 本地运行

如需本地测试，可以直接运行脚本：

```bash
# Product Hunt 热榜
python scripts/product_hunt_list_to_md.py

# arXiv AI 论文日报
python scripts/arxiv_papers_to_md.py

# GitHub Trending 热门项目
python scripts/github_trending_to_md.py
```

### 自定义

- 修改 `scripts/product_hunt_list_to_md.py` 来自定义 Product Hunt 文件的格式
- 修改 `scripts/arxiv_papers_to_md.py` 来自定义 arXiv 论文的格式或AI总结提示词
- 修改 `scripts/github_trending_to_md.py` 来自定义 GitHub Trending 的格式
- 在 `.github/workflows/` 中调整定时任务的运行时间
- 在 `.env` 或 GitHub Variables 中调整各数据源的配置参数

### 示例输出

生成的文件按数据源分类存储：

- Product Hunt: `data/producthunt/producthunt-daily-YYYY-MM-DD.md`
- arXiv论文: `data/arxiv/arxiv-daily-YYYY-MM-DD.md`
- GitHub Trending: `data/github/github-trending-YYYY-MM-DD.md`

### 贡献

欢迎任何形式的贡献！如有任何改进或新功能的建议，请提交 issue 或 pull request。

### 许可证

本项目基于 MIT 许可证开源 - 有关详细信息，请参阅 [LICENSE](LICENSE) 文件。
