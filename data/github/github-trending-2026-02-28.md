# GitHub Trending 日榜 | 2026-02-28

> 共 11 个项目

## 📑 目录

- [C](#C) (2 个项目)
- [Python](#Python) (4 个项目)
- [Rust](#Rust) (1 个项目)
- [Shell](#Shell) (2 个项目)
- [TypeScript](#TypeScript) (2 个项目)

---

## C

## [1. moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine)

**语言**: C  
**Stars**: ⭐ 0 (+593 today) | **Forks**: 🔱 283

**原始描述**: Fast and accurate automatic speech recognition (ASR) for edge devices

**中文介绍（README总结）**: Moonshine Voice 是面向开发者的开源端侧语音 AI 工具包，用于在设备本地实现实时语音转写等语音应用，强调低延迟、隐私与无需账号/API Key。其关键在于为流式场景优化的 ASR 框架与从零训练的多尺寸模型（最高精度可对标并宣称优于 Whisper Large V3，亦提供约 26MB 级小模型），并提供高层 API 覆盖转写、说话人分离与语音指令识别（含语义匹配）。典型场景包括麦克风实时转写、基于自然语言变体触发的设备/家居控制等，支持多语言并可跨 Python、iOS/Android 与各类桌面/嵌入式设备集成。

**关键词**: 端侧语音识别, 低延迟推理, 离线推理, 隐私保护, 语音转写, 说话人分离, 语音指令识别, 语义匹配, 小型化模型

**评分**: 33

**项目地址**: [GitHub](https://github.com/moonshine-ai/moonshine)

---

## [2. tukaani-project/xz](https://github.com/tukaani-project/xz)

**语言**: C  
**Stars**: ⭐ 0 (+85 today) | **Forks**: 🔱 208

**原始描述**: XZ Utils

**中文介绍（README总结）**: XZ Utils 提供通用数据压缩的库（liblzma）和命令行工具，原生支持 .xz 格式并兼容旧的 .lzma。它以“过滤器”机制组织多种压缩算法，主力为 LZMA2，典型文件体积通常比 gzip 小约 30%，API 与 zlib 相近便于应用和脚本集成。面向需要高压缩比或分发场景的开发者与系统发行者，典型用在软件包发布等“压一次、解很多次”的场合：压缩可能较耗 CPU/内存，但解压相对快速。

**关键词**: 数据压缩算法, 无损压缩, xz 容器格式, 压缩过滤器链式处理, 命令行压缩工具, 软件包发布与分发压缩, 跨平台文件压缩, tukaani-project

**评分**: 15

**项目地址**: [GitHub](https://github.com/tukaani-project/xz)

---

## Python

## [3. bytedance/deer-flow](https://github.com/bytedance/deer-flow)

**语言**: Python  
**Stars**: ⭐ 0 (+696 today) | **Forks**: 🔱 2.7k

**原始描述**: An open-source SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skills and subagents, it handles different levels of tasks that could take minutes to hours.

**中文介绍（README总结）**: DeerFlow 是一个开源的“超级智能体”编排框架，用于让智能体在研究、写代码与内容创作等任务上协同工作，覆盖从几分钟到数小时的复杂度。它面向需要构建/运行自动化智能体工作流的开发者与研究者，通过子智能体编排、可扩展技能与工具、沙箱与文件系统、上下文工程及长期记忆等机制来完成任务。典型场景包括深度资料检索与分析、多步软件开发与调试、以及在受控沙箱环境中执行工具链的端到端自动化流程。

**关键词**: 智能体编排, 多智能体系统, 技能插件, 沙箱执行, 长时记忆, 上下文工程, 文件系统隔离, 模型适配层

**评分**: 41

**项目地址**: [GitHub](https://github.com/bytedance/deer-flow)

---

## [4. datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents)

**语言**: Python  
**Stars**: ⭐ 0 (+324 today) | **Forks**: 🔱 2.7k

**原始描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**中文介绍（README总结）**: Hello-Agents（《从零开始构建智能体》）是 Datawhale 发起的系统性教程，目标是带读者从智能体核心原理出发，动手构建真正 AI Native 的单体与多智能体应用，并尝试自研基于 OpenAI 原生 API 的智能体框架。它主要面向具备 Python 与基础 LLM 调用经验的 AI 开发者、软件工程师、学生与自学者，强调从框架表象深入到经典范式与核心架构的理解。内容覆盖 ReAct 等范式、上下文工程与 Memory、协议与评估、以及从 SFT 到 GRPO 的 Agentic RL 训练，并以智能旅行助手、赛博小镇等项目作为典型实践场景。

**关键词**: 智能体系统设计, 多智能体系统, 上下文工程, 智能体记忆, 智能体评估, datawhalechina, hello-agents, English

**评分**: 18

**项目地址**: [GitHub](https://github.com/datawhalechina/hello-agents)

---

## [5. D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)

**语言**: Python  
**Stars**: ⭐ 0 (+1.1k today) | **Forks**: 🔱 1.2k

**原始描述**: 🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl!

**中文介绍（README总结）**: Scrapling 是一个自适应 Web 抓取框架，既能处理单次请求也能扩展到并发的全站爬取，面向爬虫开发者和需要抓取数据的普通用户。它的解析器可从网站结构变化中“学习”并在页面更新后自动重新定位目标元素，抓取端内置对 Cloudflare Turnstile 等反爬的绕过能力，并提供类似 Scrapy 的 Spider API。典型场景包括需要稳定抽取频繁改版页面的数据采集、带代理轮换与多会话（HTTP/无头浏览器）并行的长期爬取，以及支持暂停/恢复与实时流式输出的批量抓取流水线。

**关键词**: 网页抓取框架, 分布式爬虫, 断点续爬, 代理轮换, 反爬绕过, 无头浏览器, 自适应解析器, 元素自动定位, 流式数据输出

**评分**: 39

**项目地址**: [GitHub](https://github.com/D4Vinci/Scrapling)

---

## [6. alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox)

**语言**: Python  
**Stars**: ⭐ 0 (+105 today) | **Forks**: 🔱 123

**原始描述**: OpenSandbox is a general-purpose sandbox platform for AI applications, offering multi-language SDKs, unified sandbox APIs, and Docker/Kubernetes runtimes for scenarios like Coding Agents, GUI Agents, Agent Evaluation, AI Code Execution, and RL Training.

**中文介绍（README总结）**: OpenSandbox 是面向 AI 应用的通用沙箱平台，给 Coding/GUI Agents、Agent 评测、AI 代码执行与 RL 训练等提供隔离可控的运行环境。它为不同语言提供统一的沙箱 SDK 与协议化 API，覆盖沙箱生命周期管理与执行接口，便于扩展自定义运行时。底层支持 Docker 与 Kubernetes 的本地/分布式调度，并内置命令、文件系统、代码解释器等环境能力，结合入口网关与按沙箱粒度的出网控制用于浏览器自动化、桌面环境（VNC/VS Code）等场景。

**关键词**: 安全沙箱执行, Agent 代码执行, 代码解释器, 沙箱生命周期管理, 统一沙箱 API, 多语言 SDK, 分布式调度, 网络策略控制, 浏览器自动化

**评分**: 50

**项目地址**: [GitHub](https://github.com/alibaba/OpenSandbox)

---

## Rust

## [7. ruvnet/ruvector](https://github.com/ruvnet/ruvector)

**语言**: Rust  
**Stars**: ⭐ 0 (+410 today) | **Forks**: 🔱 205

**原始描述**: RuVector is a High Performance, Real-Time, Self-Learning, Vector Graph Neural Network, and Database built in Rust.

**中文介绍（README总结）**: RuVector 是用 Rust 构建的高性能实时向量数据库/向量图神经网络系统，强调自学习与自优化：会根据使用行为自动改进检索结果并调优负载，还可在本地硬件上运行 AI 模型（不依赖云 API，GPU 可选、偏 CPU）。它面向需要长期运行大量 AI agent、并在边缘或本地低成本推理与检索的应用/平台开发者，提供向量检索结合图智能的能力。典型场景包括嵌入式/边缘设备的常驻智能体、与 PostgreSQL 集成的数据检索与推理，以及需要单文件部署或浏览器端运行的本地 AI 应用。

**关键词**: 自学习索引, 自优化调参, 实时数据处理, 图神经网络, 图向量检索, 本地推理, 分布式向量存储, 端侧智能体运行时

**评分**: 49

**项目地址**: [GitHub](https://github.com/ruvnet/ruvector)

---

## Shell

## [8. obra/superpowers](https://github.com/obra/superpowers)

**语言**: Shell  
**Stars**: ⭐ 0 (+1.5k today) | **Forks**: 🔱 5.0k

**原始描述**: An agentic skills framework & software development methodology that works.

**中文介绍（README总结）**: Superpowers 是一套面向“编码代理”的技能框架与软件开发方法论，通过可组合的技能与初始指令，让代理在写代码前先从对话中澄清目标、抽取并分段展示规格说明，待用户确认后再生成可执行的实现计划。它强调红绿 TDD、YAGNI 与 DRY，并在用户许可后进入“子代理驱动开发”流程，把任务拆分给多个代理执行、检查与复审，从而支持较长时间的半自动/自动推进。典型场景是使用 Claude Code、Cursor 等带插件的编程助手时，为从需求到设计再到实现与测试提供一套更稳定的端到端工作流。

**关键词**: 编码代理工作流, 代理式软件开发方法论, 可组合技能框架, 需求澄清与规格提炼, 设计评审流程, 实现计划生成, 子代理驱动开发, 多代理任务分解, 自主代理执行, 测试驱动开发（TDD）

**评分**: 29

**项目地址**: [GitHub](https://github.com/obra/superpowers)

---

## [9. anthropics/claude-code](https://github.com/anthropics/claude-code)

**语言**: Shell  
**Stars**: ⭐ 0 (+494 today) | **Forks**: 🔱 5.7k

**原始描述**: Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

**中文介绍（README总结）**: Claude Code 是一款运行在终端中的智能编码代理，能理解你的代码库，通过自然语言完成日常编码任务、解释复杂代码，并协助处理 Git 工作流以提升开发效率。它面向需要在命令行或 IDE 中高频编写与维护代码的开发者，也支持在 GitHub 中通过 @claude 参与协作。关键能力在于基于代码库上下文的任务执行与可扩展的插件/自定义命令机制，典型场景包括代码阅读与讲解、例行重构与自动化修改、提交与分支等版本控制操作辅助。

**关键词**: 代码智能体, 终端 CLI 编程助手, 自然语言编程, 任务自动执行, Git 工作流自动化, 插件扩展机制, anthropics, claude-code

**评分**: 81

**项目地址**: [GitHub](https://github.com/anthropics/claude-code)

---

## TypeScript

## [10. ruvnet/ruflo](https://github.com/ruvnet/ruflo)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+531 today) | **Forks**: 🔱 1.8k

**原始描述**: 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code / Codex Integration

**中文介绍（README总结）**: Ruflo v3 是面向 Claude Code 等大模型编程环境的企业级多智能体编排平台，用于部署并协调多达 60+ 专项代理，以“蜂群”方式执行自治工作流并构建对话式 AI/开发系统。它的关键技术包括分布式群体协作与共识容错、自学习/自优化的任务路由与经验复用、RAG 集成，以及以 Rust 编写的 WASM 内核驱动的策略引擎与嵌入/证明系统，并支持 Claude/Codex 等原生集成与多模型切换。典型场景是复杂软件工程任务的端到端协作（编码、评审、测试、安全审计、文档与 DevOps）以及需要高可靠与安全控制的企业自动化流程。

**关键词**: 多智能体编排, 智能体群体协作, 自治工作流, 分布式共识容错, 自学习任务路由, RAG 检索增强生成, LLM 多模型切换, 模型故障切换

**评分**: 58

**项目地址**: [GitHub](https://github.com/ruvnet/ruflo)

---

## [11. abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+1.4k today) | **Forks**: 🔱 584

**原始描述**: GitNexus: The Zero-Server Code Intelligence Engine - GitNexus is a client-side knowledge graph creator that runs entirely in your browser. Drop in a GitHub repo or ZIP file, and get an interactive knowledge graph wit a built in Graph RAG Agent. Perfect for code exploration

**中文介绍（README总结）**: GitNexus 是一个以代码知识图谱为核心的代码智能引擎，可在浏览器端导入 GitHub 仓库或 ZIP 生成交互式图谱并提供基于图谱的 RAG/对话分析，也可通过 CLI 建索引并以 MCP 服务器把图谱能力提供给 AI 编程代理。它面向需要深度理解与改动大型代码库的开发者与 AI 助手（如 Cursor、Claude Code 等），用依赖关系、调用链、聚类与执行流等关系建模来减少漏依赖、断调用链和盲改。典型场景是仓库快速探索/问答、架构与影响面分析，以及为自动化代码修改与审查提供更可靠的上下文。

**关键词**: 客户端知识图谱, 浏览器端运行, 零服务器架构, 代码智能引擎, 代码库索引, 依赖图谱, 执行流分析, MCP 服务器, CLI 工具链, 编辑器集成

**评分**: 57

**项目地址**: [GitHub](https://github.com/abhigyanpatwari/GitNexus)

---

