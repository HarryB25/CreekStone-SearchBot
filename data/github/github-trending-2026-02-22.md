# GitHub Trending 日榜 | 2026-02-22

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

**中文介绍（README总结）**: Moonshine Voice 是面向边缘设备的本地化实时语音 AI 工具包，为开发者提供低延迟的自动语音识别，并包含转写、说话人区分（diarization）和语音命令识别等高层 API。它的模型从零训练并针对流式场景优化，宣称在高端配置下可达到或超过 Whisper Large V3 的准确率，同时也提供约 26MB 的小模型以适配受限设备。适用于需要隐私与离线能力的跨平台语音应用（Python/iOS/Android/桌面/树莓派/IoT/可穿戴等），典型场景包括边说边转写和通过语义匹配触发“开灯”等自然语言指令。

**关键词**: 端侧语音识别, 实时流式ASR, 低延迟推理, 离线语音转写, 语音接口SDK, 多平台跨端部署, 多语言语音识别, 说话人分离, 语音指令识别, 语义匹配唤醒短语, 嵌入式与物联网语音

**评分**: 35

**项目地址**: [GitHub](https://github.com/moonshine-ai/moonshine)

---

## Python

## [2. huggingface/skills](https://github.com/huggingface/skills)

**语言**: Python  
**Stars**: ⭐ 0 (+711 today) | **Forks**: 🔱 396

**原始描述**: 

**中文介绍（README总结）**: Hugging Face Skills 是一组面向 AI/ML 工作流（如数据集创建、模型训练与评估）的“技能”定义库，用标准化的 Agent Skill 格式把某个用例的指令、脚本与资源打包成可复用的自包含目录。它主要面向使用编码代理工具的开发者与研究者，可与 Claude Code、OpenAI Codex、Gemini CLI、Cursor 等互操作。典型场景是让代理在需要时自动加载特定任务的规范与步骤，或在不原生支持 skills 的工具中直接使用这些指令文件作为替代。

**关键词**: 编码智能体, 技能包封装, 指令模板, YAML 前置元数据, 工具插件集成, CLI 智能体工具, 代码生成工作流, 数据集构建, 模型训练流水线, 模型评测流程, 跨工具互操作

**评分**: 42

**项目地址**: [GitHub](https://github.com/huggingface/skills)

---

## [3. D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)

**语言**: Python  
**Stars**: ⭐ 0 (+2.9k today) | **Forks**: 🔱 1.1k

**原始描述**: 🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl!

**中文介绍（README总结）**: Scrapling 是一个自适应 Web 抓取框架，覆盖从单次请求到大规模并发爬取，面向爬虫开发者及需要采集数据的普通用户。它的解析器可在网页结构变化时自动重新定位目标元素，抓取端支持绕过常见反爬（如 Cloudflare Turnstile）并配合自动代理轮换。框架提供类似 Scrapy 的 Spider API、并发与限速控制、多会话（HTTP 与隐身无头浏览器统一）、断点续爬与流式输出，适用于长期运行的数据采集、实时统计/展示与多站点规模化抓取场景。

**关键词**: 网页抓取框架, 网络爬虫框架, 自适应解析, 元素定位修复, 反爬绕过, 代理轮换, 断点续爬, 流式数据输出

**评分**: 33

**项目地址**: [GitHub](https://github.com/D4Vinci/Scrapling)

---

## Shell

## [4. obra/superpowers](https://github.com/obra/superpowers)

**语言**: Shell  
**Stars**: ⭐ 0 (+1.5k today) | **Forks**: 🔱 4.8k

**原始描述**: An agentic skills framework & software development methodology that works.

**中文介绍（README总结）**: Superpowers 是一套面向“编码智能体”的软件开发工作流与技能框架，让智能体先通过对话澄清目标并提炼可阅读的规格说明，再在你确认设计后生成实现计划。它强调红/绿 TDD、YAGNI 和 DRY，并通过子智能体驱动的任务拆分、执行与检查来按计划推进实现。典型场景是使用 Claude Code、Cursor 等编程助手进行较长时间的半自主开发时，减少跑偏并提高从需求到落地的流程一致性。

**关键词**: 编码代理工作流, Agent 技能框架, 可组合技能, 需求澄清, 规格说明生成, 设计评审流程, 实现计划生成, 子代理协作, 任务分解执行, 测试驱动开发（TDD）

**评分**: 43

**项目地址**: [GitHub](https://github.com/obra/superpowers)

---

## TypeScript

## [5. bytedance/deer-flow](https://github.com/bytedance/deer-flow)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+622 today) | **Forks**: 🔱 2.6k

**原始描述**: An open-source SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skills and subagents, it handles different levels of tasks that could take minutes to hours.

**中文介绍（README总结）**: DeerFlow 2.0 是一个开源“超级智能体”编排框架，用于让系统在较长时间跨度内自动完成调研、写代码与内容生成等任务。它面向需要把复杂工作流交给 AI 执行的开发者与研究/产品团队，通过子智能体协作、可扩展的技能与工具、沙箱与文件系统、上下文工程和长程记忆来提升可靠性与可控性。典型场景包括深度研究与报告产出、端到端编程实现与迭代、以及在隔离沙箱中执行和验证多步骤任务。

**关键词**: 多智能体编排, 技能插件, 沙箱执行, 长时记忆, 上下文工程, 文件系统隔离, 模型路由配置, bytedance

**评分**: 38

**项目地址**: [GitHub](https://github.com/bytedance/deer-flow)

---

## [6. ruvnet/claude-flow](https://github.com/ruvnet/claude-flow)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+210 today) | **Forks**: 🔱 1.7k

**原始描述**: 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code / Codex Integration

**中文介绍（README总结）**: Ruflo v3 是面向 Claude/Claude Code 的企业级多智能体编排平台，用于部署与协调多代理“蜂群”来执行自治工作流并构建对话式 AI 系统，重点服务需要自动化软件工程流程的团队。它提供 60+ 专用代理（编码、评审、测试、安全审计、文档、DevOps 等），支持分布式协作模式与容错共识，并具备自学习/自优化能力以复用高效工作模式。平台还集成 RAG，并可通过 MCP 原生接入 Claude Code，同时支持在多种 LLM 之间切换与故障转移，适用于复杂工程任务的自动协作与生产级部署。

**关键词**: 多智能体编排, 自主工作流, 自学习路由, 分布式一致性, 容错机制, 多 LLM 路由, ruvnet, claude-flow

**评分**: 53

**项目地址**: [GitHub](https://github.com/ruvnet/claude-flow)

---

