# GitHub Trending 日榜 | 2026-02-12

> 共 6 个项目

## 📑 目录

- [Go](#Go) (1 个项目)
- [Jupyter Notebook](#Jupyter-Notebook) (1 个项目)
- [Python](#Python) (2 个项目)
- [TypeScript](#TypeScript) (2 个项目)

---

## Go

## [1. github/gh-aw](https://github.com/github/gh-aw)

**语言**: Go  
**Stars**: ⭐ 0 (+390 today) | **Forks**: 🔱 132

**原始描述**: GitHub Agentic Workflows

**中文介绍（README总结）**: GitHub Agentic Workflows 让你用自然语言的 Markdown 描述 AI 代理工作流，并在 GitHub Actions 中运行以自动化仓库内的各类任务。面向使用 GitHub 的开发者与仓库维护者，帮助将常规维护与协作流程交给可控的智能代理。关键技术包括默认只读权限、经清洗的写操作、多层安全护栏（沙箱执行、输入净化、网络隔离、SHA 固定依赖、工具白名单、编译期校验）以及团队门禁与人工审批。典型场景是在受控边界内让 AI 执行代码库管理与协作相关的自动化流程，同时保持严格的安全与审核。

**关键词**: 自然语言编排, Go 语言实现, 安全护栏, 沙箱执行, 输入净化, 网络隔离, 供应链安全, 工具白名单, 编译期校验

**评分**: 52

**项目地址**: [GitHub](https://github.com/github/gh-aw)

---

## Jupyter Notebook

## [2. patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub)

**语言**: Jupyter Notebook  
**Stars**: ⭐ 0 (+154 today) | **Forks**: 🔱 4.7k

**原始描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**中文介绍（README总结）**: 一个面向AI工程的资源库，提供LLM、RAG、智能体等深入教程与可运行的示例项目，帮助快速学习与构建真实应用。适合初学者、实践者与研究者，涵盖从入门到高级的难度梯度。关键技术包括大模型、检索增强、AI代理与工作流，典型场景涉及OCR与视觉、基础RAG实现、代理式流程以及微调与生产级系统。

**关键词**: LLM, RAG, Agent, 计算机视觉, 模型微调, 本地部署, 生产级系统, 工作流编排, LaTeX 公式识别

**评分**: 15

**项目地址**: [GitHub](https://github.com/patchy631/ai-engineering-hub)

---

## Python

## [3. google/langextract](https://github.com/google/langextract)

**语言**: Python  
**Stars**: ⭐ 0 (+3.2k today) | **Forks**: 🔱 2.1k

**原始描述**: A Python library for extracting structured information from unstructured text using LLMs with precise source grounding and interactive visualization.

**中文介绍（README总结）**: LangExtract 是一个基于大语言模型的 Python 库，用于从非结构化文本中按用户定义的指令抽取结构化信息，适合需要批量处理文档的开发者、数据与临床信息团队、研究人员等。其关键技术包括精确溯源定位（将每个抽取项映射到原文位置并可交互可视化）、基于少样例的模式/架构约束输出、针对长文档的分块并行与多轮提取策略，以及对云端模型（如 Gemini）与本地模型（通过 Ollama）的灵活支持。典型场景涵盖临床笔记与放射科报告结构化、用药信息抽取，以及长篇文本（如《罗密欧与朱丽叶》）中的实体与关系提取与核验。

**关键词**: 结构化信息抽取, 来源溯源, 交互式可视化, 长文档处理, 文本分块, 少样本示例, 约束生成, google

**评分**: 27

**项目地址**: [GitHub](https://github.com/google/langextract)

---

## [4. cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources)

**语言**: Python  
**Stars**: ⭐ 0 (+440 today) | **Forks**: 🔱 948

**原始描述**: A list of free LLM inference resources accessible via API.

**中文介绍（README总结）**: 这是一个汇总可通过 API 免费调用或带试用额度的合法大模型推理资源的目录，涵盖 OpenRouter、Google AI Studio、NVIDIA NIM、Mistral、HuggingFace 等提供方。面向希望低成本做原型开发、评测对比与集成的开发者与研究者，可直接访问多种模型如 Llama、Gemma、Qwen、DeepSeek 等；部分服务有速率与配额限制（如 OpenRouter 的日请求上限）或试用额度。典型场景包括快速搭建应用、模型路由与性能基准、在不自建推理的前提下做多模型实验与对比。

**关键词**: 推理网关, 多模型路由, 模型目录, 模型托管, 云推理服务, 速率限制, cheahjs, free-llm-api-resources

**评分**: 5

**项目地址**: [GitHub](https://github.com/cheahjs/free-llm-api-resources)

---

## TypeScript

## [5. ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+120 today) | **Forks**: 🔱 1.4k

**原始描述**: Chrome DevTools for coding agents

**中文介绍（README总结）**: Chrome DevTools MCP 是面向 AI 编码助手和开发者的 MCP 服务器，让 Gemini、Claude、Cursor、Copilot 等代理可操控并检查真实的 Chrome 浏览器，用于可靠自动化、深度调试与性能分析。它基于 Chrome DevTools 与 Puppeteer，支持记录性能追踪并生成洞察、分析网络请求、抓取截图、查看源映射控制台信息，并自动等待操作结果。典型场景包括端到端网页自动化、前端问题定位、性能基准与对比评估；使用时需注意浏览器内容会暴露给代理，且性能工具可能访问 CrUX 以获取真实用户体验数据。

**关键词**: MCP 服务器, 浏览器自动化, 浏览器调试, 性能追踪, 性能分析, 网络请求分析, 截图采集, 控制台日志与源映射, CrUX 数据集成

**评分**: 46

**项目地址**: [GitHub](https://github.com/ChromeDevTools/chrome-devtools-mcp)

---

## [6. EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+272 today) | **Forks**: 🔱 673

**原始描述**: Official Claude Code compound engineering plugin

**中文介绍（README总结）**: 这是一套面向使用多款 AI 编码工具的工程团队与开发者的 Claude Code 插件与市场，核心提供 Compound Engineering Plugin，并配套一个 Bun/TypeScript CLI 将 Claude Code 插件转换为 OpenCode、Codex、Factory Droid、Cursor、Pi 与 Gemini 的可用格式。关键技术包括跨平台的技能/命令/代理映射、统一的 SKILL.md 标准传递、MCP 互操作以及通过符号链接同步个人技能与 MCP 服务器配置，使多工具间配置即时生效。典型场景是将现有 Claude Code 工作流迁移到不同 IDE/CLI、在团队内复用和分发插件与技能，并在多供应商实验性格式演进中保持兼容与同步。

**关键词**: 插件市场, 跨平台插件转换, 多供应商适配, Agent-技能-命令映射, 命名空间前缀去除, 配置同步, 符号链接, MCP 服务器

**评分**: 48

**项目地址**: [GitHub](https://github.com/EveryInc/compound-engineering-plugin)

---

