# GitHub Trending 日榜 | 2026-02-24

> 共 6 个项目

## 📑 目录

- [C](#C) (1 个项目)
- [Python](#Python) (2 个项目)
- [Shell](#Shell) (1 个项目)
- [TypeScript](#TypeScript) (2 个项目)

---

## C

## [1. moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine)

**语言**: C  
**Stars**: ⭐ 0 (+515 today) | **Forks**: 🔱 242

**原始描述**: Fast and accurate automatic speech recognition (ASR) for edge devices

**中文介绍（README总结）**: Moonshine Voice 是面向边缘设备的开源语音 AI 工具包，帮助开发者构建实时语音应用，在本地完成自动语音识别等处理以获得低延迟与隐私保护，无需账号或 API Key。它提供从高精度到约 26MB 级小模型的选择，并针对流式输入优化，可在用户说话过程中持续产出转写结果。典型场景包括跨平台的实时转写、说话人识别（diarization）以及基于语义匹配的语音指令识别，适用于手机、桌面、树莓派与各类 IoT/可穿戴设备的多语言语音交互。

**关键词**: 端侧语音识别, 低延迟推理, 离线语音处理, 实时转写, 说话人分离, 语音命令识别, 语义匹配, 多语言语音模型, 小型化模型

**评分**: 34

**项目地址**: [GitHub](https://github.com/moonshine-ai/moonshine)

---

## Python

## [2. huggingface/skills](https://github.com/huggingface/skills)

**语言**: Python  
**Stars**: ⭐ 0 (+711 today) | **Forks**: 🔱 397

**原始描述**: 

**中文介绍（README总结）**: Hugging Face Skills 提供一组用于数据集创建、模型训练与评估等 AI/ML 任务的“技能”定义，采用标准化的 Agent Skill 格式把说明、脚本和资源封装成自包含目录。它面向使用编程代理/代码助手的开发者与研究者，强调可在 Claude Code、OpenAI Codex、Gemini CLI、Cursor 等多种工具间互操作。典型场景是在不同代理工具中复用同一套任务流程与指令，让代理按需加载并执行特定用例的指导。

**关键词**: 代码代理, 代理技能包, 插件市场, YAML 前置元数据, 指令模板, 跨工具互操作, ML 任务自动化, 模型评估流水线

**评分**: 43

**项目地址**: [GitHub](https://github.com/huggingface/skills)

---

## [3. D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)

**语言**: Python  
**Stars**: ⭐ 0 (+2.9k today) | **Forks**: 🔱 1.1k

**原始描述**: 🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl!

**中文介绍（README总结）**: Scrapling 是一个自适应 Web 抓取框架，覆盖从单次请求到大规模并发爬取的完整流程，面向爬虫开发者及需要抓取数据的普通用户。它的解析器可从网页变化中学习并在页面更新后自动重新定位元素，抓取端内置绕过反爬机制（如 Cloudflare Turnstile），并支持代理自动轮换。框架提供类似 Scrapy 的 Spider API，支持多会话（HTTP/浏览器）、并发与限速、断点续爬与流式输出，适用于长期运行的爬虫、数据管道或需要实时统计与增量结果的采集任务。

**关键词**: Web 爬虫框架, 自适应解析, 元素自动定位, 反爬绕过, 代理轮换, 无头浏览器集成, 断点续爬, 流式输出, 阻断检测重试

**评分**: 34

**项目地址**: [GitHub](https://github.com/D4Vinci/Scrapling)

---

## Shell

## [4. obra/superpowers](https://github.com/obra/superpowers)

**语言**: Shell  
**Stars**: ⭐ 0 (+1.5k today) | **Forks**: 🔱 4.8k

**原始描述**: An agentic skills framework & software development methodology that works.

**中文介绍（README总结）**: Superpowers 是一套面向“代码智能体”的技能框架与软件开发方法论，把需求澄清、规格说明、设计评审、实现计划到执行落地串成可复用的工作流。它主要服务于使用 Claude Code/Cursor 等编程助手的开发者或团队，让智能体先从对话中提炼可读的 spec 并获得确认，再生成强调 TDD（红/绿）、YAGNI、DRY 的实施计划。随后通过“子智能体驱动开发”按任务分解执行、检查与复审，适合需要更长时间自治但仍希望按既定计划推进的开发场景。

**关键词**: 编码 Agent 工作流, Agent 技能框架, 可组合技能, 需求澄清, 规格说明生成, 设计评审, 实现计划生成, 多 Agent 编排, 子 Agent 驱动开发

**评分**: 44

**项目地址**: [GitHub](https://github.com/obra/superpowers)

---

## TypeScript

## [5. bytedance/deer-flow](https://github.com/bytedance/deer-flow)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+622 today) | **Forks**: 🔱 2.6k

**原始描述**: An open-source SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skills and subagents, it handles different levels of tasks that could take minutes to hours.

**中文介绍（README总结）**: DeerFlow 2.0 是一个开源的“超级智能体”编排框架，用来让智能体在执行研究、写代码、生成产物等分钟到小时级任务时，能协调多个子智能体、技能/工具、长期记忆与沙箱环境协同工作。它面向需要搭建可扩展 AI Agent 工作流的开发者与团队，核心技术包括子代理编排、上下文工程、沙箱与文件系统隔离、可扩展技能体系以及记忆管理。典型场景是自动化深度调研与报告生成、复杂编码与多步项目任务拆解、在受控沙箱中运行/验证工具调用与产出流程。

**关键词**: 智能体编排, 多智能体协作, 技能插件机制, 沙箱执行, 文件系统隔离, 长时记忆, 上下文工程, 深度研究代理, 代码生成代理

**评分**: 42

**项目地址**: [GitHub](https://github.com/bytedance/deer-flow)

---

## [6. ruvnet/claude-flow](https://github.com/ruvnet/claude-flow)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+210 today) | **Forks**: 🔱 1.7k

**原始描述**: 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code / Codex Integration

**中文介绍（README总结）**: Ruflo v3 是面向 Claude Code 的企业级多智能体编排平台，用于部署并协调多代理“蜂群”来完成自主工作流与对话式 AI/软件工程任务。它提供 60+ 专用代理并支持分布式协作（层级或网状通信）、自学习/自优化与容错一致性，同时可集成 RAG，并通过 MCP 与 Claude Code 原生打通。典型场景包括团队级编码、代码审查、测试、安全审计、文档与 DevOps 自动化等多环节协同。

**关键词**: 多智能体编排, 智能体集群, 自主工作流, 分布式协同, 分层与网状拓扑, 自学习任务路由, LLM 多模型切换, 故障切换, 提示注入防护

**评分**: 51

**项目地址**: [GitHub](https://github.com/ruvnet/claude-flow)

---

