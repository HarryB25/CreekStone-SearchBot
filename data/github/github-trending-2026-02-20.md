# GitHub Trending 日榜 | 2026-02-20

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
**Stars**: ⭐ 0 (+515 today) | **Forks**: 🔱 240

**原始描述**: Fast and accurate automatic speech recognition (ASR) for edge devices

**中文介绍（README总结）**: Moonshine Voice 是面向边缘设备的开源语音 AI 工具包，帮助开发者构建实时语音应用，提供本地端自动语音识别并强调低延迟与隐私无需云端账号或 API Key。其框架与模型针对流式输入优化，支持从高精度到约 26MB 的小模型，并提供转写、说话人分离（diarization）和语音指令识别等高层接口。典型场景包括麦克风实时字幕/转写、在设备上识别“打开灯”等自定义指令（语义匹配容忍自然表达变化），可跨 Python、iOS/Android 与桌面/IoT/可穿戴等平台集成。

**关键词**: 端侧语音识别, 低延迟推理, 离线语音转写, 语音指令识别, 语义匹配, 说话人分离, 小型化模型, 隐私保护

**评分**: 40

**项目地址**: [GitHub](https://github.com/moonshine-ai/moonshine)

---

## Python

## [2. huggingface/skills](https://github.com/huggingface/skills)

**语言**: Python  
**Stars**: ⭐ 0 (+711 today) | **Forks**: 🔱 396

**原始描述**: 

**中文介绍（README总结）**: Hugging Face Skills 是一套面向 AI/ML 任务（如数据集创建、模型训练与评估）的“技能”定义与打包规范，把指令、脚本和资源封装成自包含目录供编码代理调用。它主要面向使用自动化编程/智能体工具的开发者与研究者，并采用标准化的 Agent Skill 格式（含带 YAML 前置字段的说明文件）。典型场景是让 Claude Code、OpenAI Codex、Gemini CLI、Cursor 等工具以统一方式加载并执行特定工作流指引，在不同代理生态间复用同一套任务能力。

**关键词**: 代理技能规范, 编码代理集成, 跨代理互操作, 目录式技能包, YAML 前置元数据, 插件市场机制, CLI 扩展指令, 数据集构建任务, 模型训练任务, 模型评测任务

**评分**: 45

**项目地址**: [GitHub](https://github.com/huggingface/skills)

---

## [3. D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)

**语言**: Python  
**Stars**: ⭐ 0 (+2.9k today) | **Forks**: 🔱 1.1k

**原始描述**: 🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl!

**中文介绍（README总结）**: Scrapling 是一个自适应的 Web 抓取框架，覆盖从单次请求到大规模并发爬取的需求，面向爬虫开发者与需要抓取数据的普通用户。它的解析器可随网页结构变化自动重新定位元素，抓取端内置绕过反爬（如 Cloudflare Turnstile）的能力，并提供类似 Scrapy 的 Spider API 支持并发、多会话（HTTP 与无头浏览器统一）、暂停/恢复、流式输出与实时统计。典型场景包括长期运行的数据采集任务、需要断点续爬的全站抓取，以及在高封禁风险站点上结合代理轮换进行稳定抓取。

**关键词**: 网页爬虫框架, 自适应解析, 元素自动定位, 反爬绕过, 代理轮换, 无头浏览器, 断点续爬, 流式数据输出

**评分**: 31

**项目地址**: [GitHub](https://github.com/D4Vinci/Scrapling)

---

## Shell

## [4. obra/superpowers](https://github.com/obra/superpowers)

**语言**: Shell  
**Stars**: ⭐ 0 (+1.5k today) | **Forks**: 🔱 4.8k

**原始描述**: An agentic skills framework & software development methodology that works.

**中文介绍（README总结）**: Superpowers 是一套面向“编码代理”的软件开发工作流与技能框架，通过可组合的 skills 和初始指令，让代理先澄清目标并从对话中提炼可审阅的规格说明，再在你确认设计后生成可执行的实现计划。它强调红/绿 TDD、YAGNI 和 DRY，并以“子代理驱动开发”把任务拆分给多个代理执行、检查与复核，支持在既定计划下较长时间的半/全自动推进。典型场景是使用 Claude/Cursor/Codex 等 coding agent 进行项目从需求到实现的端到端协作开发与质量约束。

**关键词**: 编码代理工作流, Agent 技能框架, 可组合技能, 需求澄清, 规格说明生成, 设计评审流程, 实现计划生成, 测试驱动开发（TDD）, 子代理驱动开发, 多智能体协作, IDE/编辑器插件集成

**评分**: 30

**项目地址**: [GitHub](https://github.com/obra/superpowers)

---

## TypeScript

## [5. bytedance/deer-flow](https://github.com/bytedance/deer-flow)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+622 today) | **Forks**: 🔱 2.6k

**原始描述**: An open-source SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skills and subagents, it handles different levels of tasks that could take minutes to hours.

**中文介绍（README总结）**: DeerFlow 2.0 是一个开源的“超级智能体编排框架”，用于把子智能体、可扩展技能/工具、长短期记忆与沙箱环境组织起来，自动完成从调研到编码与内容生成等可能持续数分钟到数小时的任务。它面向希望搭建多智能体自动化工作流的开发者与研究者，强调上下文工程、文件系统/沙箱隔离执行与记忆管理等能力。典型场景包括深度资料检索与总结、跨步骤的软件开发与验证、以及需要多工具协作的复杂项目自动化。

**关键词**: 超级智能体框架, 多智能体编排, 子智能体协作, 沙箱执行环境, 技能插件机制, 长时记忆, 上下文工程, 代码生成, 深度研究工作流

**评分**: 34

**项目地址**: [GitHub](https://github.com/bytedance/deer-flow)

---

## [6. ruvnet/claude-flow](https://github.com/ruvnet/claude-flow)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+210 today) | **Forks**: 🔱 1.7k

**原始描述**: 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code / Codex Integration

**中文介绍（README总结）**: Ruflo v3 是面向 Claude Code 的企业级多智能体编排平台，用于部署并协调大规模 agent 群体，驱动自动化工作流与对话式 AI 系统。它提供 60+ 专项 agent（编码、评审、测试、安全审计、文档与 DevOps 等），支持分布式群体协作与自学习/自优化路由，并具备容错共识与企业安全能力。平台可与 RAG 集成，并通过 MCP 原生接入 Claude Code，同时支持在 Claude/GPT/Gemini 等多种模型间切换与故障转移，典型用于复杂软件工程任务的自动化协同开发与运维。

**关键词**: 多智能体编排, 智能体群体（swarm）, 自主工作流, 层级式智能体协作, 点对点智能体协作, 自学习任务路由, 分布式共识, RAG检索增强生成, 提示注入防护

**评分**: 51

**项目地址**: [GitHub](https://github.com/ruvnet/claude-flow)

---

