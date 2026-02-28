# GitHub Trending 日榜 | 2026-02-25

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

**中文介绍（README总结）**: Moonshine Voice 是面向边缘设备的本地自动语音识别工具包，帮助开发者构建实时语音应用，强调低延迟、隐私与无需云端账号/密钥。它提供从 26MB 小模型到高精度模型的选择，并针对流式输入做了优化，可用于边说边转写。框架提供转写、说话人分离与语音指令/命令识别等高层能力，适配 Python、iOS、Android 及多种桌面与 IoT 平台，支持多语言场景如语音助手、设备控制与可穿戴/物联网交互。

**关键词**: 端侧语音识别, 流式转写, 低延迟推理, 语音交互, 说话人分离, 语音指令识别, 语义匹配, 多语言语音识别, 嵌入式与IoT部署, 跨平台客户端集成

**评分**: 36

**项目地址**: [GitHub](https://github.com/moonshine-ai/moonshine)

---

## [2. tukaani-project/xz](https://github.com/tukaani-project/xz)

**语言**: C  
**Stars**: ⭐ 0 (+85 today) | **Forks**: 🔱 208

**原始描述**: XZ Utils

**中文介绍（README总结）**: XZ Utils 提供通用数据压缩库 liblzma 和配套命令行工具，主要面向需要在应用与脚本中读写 .xz（并兼容旧 .lzma）格式的开发者与系统/发行版维护者。它以“过滤器”机制支持多种压缩算法，主力为 LZMA2，通常比 gzip 生成更小的文件但压缩可能更耗 CPU 与内存。典型场景是软件包分发与归档：压缩可慢一些但解压相对快，适合同一文件被大量重复解压的环境，并且其 API 与 zlib 类似便于集成迁移。

**关键词**: 数据压缩, 压缩工具链, 压缩库, 命令行工具, xz 格式, 压缩过滤器, gzip 命令行兼容, tukaani-project

**评分**: 19

**项目地址**: [GitHub](https://github.com/tukaani-project/xz)

---

## Python

## [3. bytedance/deer-flow](https://github.com/bytedance/deer-flow)

**语言**: Python  
**Stars**: ⭐ 0 (+696 today) | **Forks**: 🔱 2.7k

**原始描述**: An open-source SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skills and subagents, it handles different levels of tasks that could take minutes to hours.

**中文介绍（README总结）**: DeerFlow 是一个开源的“超级智能体”编排框架，用来让智能体在研究、写代码与内容生成等任务中协同工作，覆盖从几分钟到数小时的复杂流程。它面向希望构建/运行多智能体自动化的开发者与研究人员，通过子智能体编排、可扩展的技能与工具、沙箱与文件系统、上下文工程和长期记忆等机制来提升可靠性与任务完成度。典型场景包括自动化深度调研、跨步骤的软件原型开发与迭代、以及需要安全隔离执行与持久化记忆的长链路工作流。

**关键词**: 多智能体编排, 技能插件, 沙箱执行, 代码生成, 深度研究工作流, 长程记忆, 上下文工程, 文件系统沙箱, LLM 模型配置

**评分**: 37

**项目地址**: [GitHub](https://github.com/bytedance/deer-flow)

---

## [4. datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents)

**语言**: Python  
**Stars**: ⭐ 0 (+324 today) | **Forks**: 🔱 2.7k

**原始描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**中文介绍（README总结）**: Hello-Agents《从零开始构建智能体》是一套面向智能体构建的系统性教程，目标是让学习者从理解核心原理出发，亲手实现并搭建 AI Native 的单体到多智能体系统与应用。它主要面向具备一定 Python 与 LLM API 调用基础的 AI 开发者、软件工程师、学生和自学者。内容覆盖 ReAct 等经典范式、上下文工程与记忆（Memory）、协议与评估、以及基于 OpenAI 原生 API 从零自研智能体框架，并延伸到 Agentic RL 等训练实践。典型场景包括开发智能旅行助手、模拟“赛博小镇”等综合多智能体应用，并辅助求职面试准备。

**关键词**: 多智能体系统, LLM, 上下文工程, 记忆模块, 智能体协议, 智能体评测, datawhalechina, hello-agents

**评分**: 27

**项目地址**: [GitHub](https://github.com/datawhalechina/hello-agents)

---

## [5. D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)

**语言**: Python  
**Stars**: ⭐ 0 (+1.1k today) | **Forks**: 🔱 1.2k

**原始描述**: 🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl!

**中文介绍（README总结）**: Scrapling 是一个自适应的 Python Web 抓取与爬虫框架，既能处理单次请求也能扩展到并发的大规模爬取。它面向爬虫开发者和普通数据采集用户，核心技术包括可随页面变化自动重新定位元素的学习型解析器、内置可绕过常见反爬（如 Cloudflare Turnstile）的抓取器，以及支持多会话、暂停/续爬、代理轮换与实时流式输出的 Spider 框架。典型场景是站点结构频繁变动、需要稳定抗封与高并发抓取，并将结果实时送入 UI 或数据管道的长期任务。

**关键词**: 自适应网页抓取, 网页爬虫框架, 选择器自愈, 元素定位迁移, 反爬绕过, 代理池轮换, 无头浏览器集成, 断点续爬, 流式数据输出

**评分**: 33

**项目地址**: [GitHub](https://github.com/D4Vinci/Scrapling)

---

## [6. alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox)

**语言**: Python  
**Stars**: ⭐ 0 (+105 today) | **Forks**: 🔱 124

**原始描述**: OpenSandbox is a general-purpose sandbox platform for AI applications, offering multi-language SDKs, unified sandbox APIs, and Docker/Kubernetes runtimes for scenarios like Coding Agents, GUI Agents, Agent Evaluation, AI Code Execution, and RL Training.

**中文介绍（README总结）**: OpenSandbox 是面向 AI 应用的通用沙箱平台，为开发者提供多语言 SDK 与统一沙箱 API，用于在隔离环境中安全执行代码与工具调用。它基于沙箱协议管理生命周期与执行接口，并以 Docker/Kubernetes 作为运行时，支持本地运行到大规模分布式调度。典型场景包括 Coding/GUI Agent 的命令与文件系统操作、浏览器/桌面自动化环境、Agent 评测、AI 代码执行与强化学习训练等。

**关键词**: 沙箱执行环境, 统一沙箱 API, 多语言 SDK, 生命周期管理, 代码解释器, 强化学习训练, 网络策略（入站/出站）, 浏览器自动化

**评分**: 43

**项目地址**: [GitHub](https://github.com/alibaba/OpenSandbox)

---

## Rust

## [7. ruvnet/ruvector](https://github.com/ruvnet/ruvector)

**语言**: Rust  
**Stars**: ⭐ 0 (+410 today) | **Forks**: 🔱 205

**原始描述**: RuVector is a High Performance, Real-Time, Self-Learning, Vector Graph Neural Network, and Database built in Rust.

**中文介绍（README总结）**: RuVector 是用 Rust 构建的高性能实时向量数据库/图神经网络系统，强调“自学习、自优化”，能根据使用反馈自动改进检索与调度，并在本地硬件上运行 AI 模型（偏 CPU、可选 GPU），还可作为 PostgreSQL 扩展集成。它面向需要大规模、持续运行 AI 代理与向量检索的开发者与团队，目标是在无需云端 API 的情况下提供近实时检索、图智能与本地推理的一体化栈。典型场景包括长久在线代理、边缘/本地信号（传感器、网络、机器）旁的在线学习与检索，以及与 PostgreSQL 深度集成的向量+图应用。

**关键词**: 自学习检索, 自优化调度, 实时向量搜索, 图神经网络, 边缘端推理, 分布式系统, 智能体操作系统, 容器化模型格式

**评分**: 56

**项目地址**: [GitHub](https://github.com/ruvnet/ruvector)

---

## Shell

## [8. obra/superpowers](https://github.com/obra/superpowers)

**语言**: Shell  
**Stars**: ⭐ 0 (+1.5k today) | **Forks**: 🔱 5.0k

**原始描述**: An agentic skills framework & software development methodology that works.

**中文介绍（README总结）**: Superpowers 是一套面向编程智能体的“技能框架+开发方法论”，让代码代理先通过对话澄清目标并提炼可阅读的需求规格，再在你确认设计后生成可执行的实现计划。它强调红/绿 TDD、YAGNI 与 DRY，并通过子代理驱动的分工执行与检查评审，让代理按计划持续推进。适用于使用 Claude/Cursor/Codex 等代码代理进行较长时间半自治的软件开发与迭代场景。

**关键词**: 技能框架（skills）, 可组合技能, 需求澄清, 规格说明生成, 设计评审, 实现计划生成, 子代理协作开发, 测试驱动开发（TDD）, 代码审查自动化, IDE 插件集成

**评分**: 50

**项目地址**: [GitHub](https://github.com/obra/superpowers)

---

## [9. anthropics/claude-code](https://github.com/anthropics/claude-code)

**语言**: Shell  
**Stars**: ⭐ 0 (+494 today) | **Forks**: 🔱 5.7k

**原始描述**: Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

**中文介绍（README总结）**: Claude Code 是一个运行在终端的智能编程代理，能够理解你的代码库，通过自然语言帮你执行日常编码任务、解释复杂代码，并协助完成 git 工作流以提升开发效率。它面向需要在本地项目中高频编写与维护代码的开发者，可在终端、IDE 或通过在 GitHub 上 @claude 的方式使用。项目还提供可扩展的插件机制，用自定义命令和代理覆盖更多自动化协作场景。它会收集一定的使用与对话反馈数据，并声明有访问控制与有限保留等隐私保护措施。

**关键词**: 终端编程助手, 自然语言命令, Git 工作流自动化, 命令行工具（CLI）, 插件系统, 隐私与数据留存, anthropics, claude-code

**评分**: 76

**项目地址**: [GitHub](https://github.com/anthropics/claude-code)

---

## TypeScript

## [10. ruvnet/ruflo](https://github.com/ruvnet/ruflo)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+531 today) | **Forks**: 🔱 1.8k

**原始描述**: 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code / Codex Integration

**中文介绍（README总结）**: Ruflo 是面向 Claude（并可切换到 GPT/Gemini 等多模型）的企业级智能体编排平台，用来把 Claude Code 扩展为可部署与协调的多智能体“蜂群”，共同完成复杂的软件工程与对话式 AI 工作流。它提供 60+ 专用智能体并支持层级/网状协作、上下文共享与自动拆分任务，结合 RAG，并通过自学习/自优化把成功模式沉淀为可复用的路由策略。底层强调分布式群体智能、容错共识与安全架构，典型场景包括编码/评审/测试/安全审计/文档/DevOps 等自动化协作以及企业级自主工作流编排。

**关键词**: 多智能体编排, 智能体集群（swarm）, 自主工作流, 层级/网状协作, 自学习任务路由, RAG, 分布式共识容错, 企业级安全, 多 LLM 切换与故障转移

**评分**: 53

**项目地址**: [GitHub](https://github.com/ruvnet/ruflo)

---

## [11. abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+1.4k today) | **Forks**: 🔱 585

**原始描述**: GitNexus: The Zero-Server Code Intelligence Engine - GitNexus is a client-side knowledge graph creator that runs entirely in your browser. Drop in a GitHub repo or ZIP file, and get an interactive knowledge graph wit a built in Graph RAG Agent. Perfect for code exploration

**中文介绍（README总结）**: GitNexus 是一个面向代码库的“零服务器”代码智能引擎，可在浏览器端将 GitHub 仓库或 ZIP 索引为知识图谱，并提供交互式图谱与内置的 Graph RAG Agent 用于对仓库聊天与探索。它主要面向需要深度理解与分析代码结构的开发者与 AI 编程代理，通过追踪依赖、调用链、模块聚类与执行流等关系，让代理工具（如 Cursor、Claude Code 等）获得更完整的架构上下文，减少遗漏依赖与错误修改。典型场景是大型仓库的架构梳理、影响分析、跨模块定位与让小模型在复杂代码上保持可靠编辑。

**关键词**: 代码智能, 知识图谱构建, 代码库索引, 依赖图, 执行流分析, MCP 服务器, 浏览器端运行, 编辑器集成

**评分**: 54

**项目地址**: [GitHub](https://github.com/abhigyanpatwari/GitNexus)

---

