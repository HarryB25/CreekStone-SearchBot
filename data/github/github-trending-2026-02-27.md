# GitHub Trending 日榜 | 2026-02-27

> 共 13 个项目

## 📑 目录

- [C](#C) (2 个项目)
- [C++](#Cplusplus) (1 个项目)
- [Python](#Python) (6 个项目)
- [Shell](#Shell) (2 个项目)
- [TypeScript](#TypeScript) (2 个项目)

---

## C

## [1. tukaani-project/xz](https://github.com/tukaani-project/xz)

**语言**: C  
**Stars**: ⭐ 0 (+85 today) | **Forks**: 🔱 208

**原始描述**: XZ Utils

**中文介绍（README总结）**: XZ Utils 提供通用数据压缩的库（liblzma）和命令行工具，原生支持 .xz 格式并兼容旧 .lzma，面向需要在应用、脚本或发行流程中集成压缩能力的开发者与系统用户。其关键技术是以 LZMA2 为主的“过滤器”链式压缩框架，liblzma 的 API 设计与 zlib 相近、xz 命令语法也类似 gzip，便于迁移。典型场景是生成比 gzip 更小的压缩包并在多处频繁解压（如软件包分发），代价是高压缩率模式可能消耗较多 CPU 与内存。

**关键词**: 数据压缩, 无损压缩, xz 格式, 命令行工具, 压缩比优化, 解压性能, C 语言实现, tukaani-project

**评分**: 18

**项目地址**: [GitHub](https://github.com/tukaani-project/xz)

---

## [2. moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine)

**语言**: C  
**Stars**: ⭐ 0 (+593 today) | **Forks**: 🔱 283

**原始描述**: Fast and accurate automatic speech recognition (ASR) for edge devices

**中文介绍（README总结）**: Moonshine Voice 是面向边缘设备的开源语音应用工具包，提供本地端实时自动语音识别，并配套转写、说话人分离与口令/指令识别等高层 API，适合开发者快速构建语音交互应用。它强调全程端上运行以获得低延迟与隐私性，模型从零训练并覆盖从约 26MB 小模型到高精度模型，宣称在高端精度上可超过 Whisper Large V3。典型场景包括麦克风流式转写、语音助手/设备控制的语义匹配唤起与多平台（Python/iOS/Android/桌面/树莓派与 IoT、可穿戴）端侧部署，并支持多种语言。

**关键词**: 端侧语音识别, 设备端推理, 流式语音识别, 低延迟, 语音转写, 说话人分离, 语音指令识别, 语义匹配, 小模型压缩, 隐私保护

**评分**: 35

**项目地址**: [GitHub](https://github.com/moonshine-ai/moonshine)

---

## C++

## [3. PaddlePaddle/Paddle](https://github.com/PaddlePaddle/Paddle)

**语言**: C++  
**Stars**: ⭐ 0 (+6 today) | **Forks**: 🔱 6.0k

**原始描述**: PArallel Distributed Deep LEarning: Machine Learning Framework from Industrial Practice （『飞桨』核心框架，深度学习&机器学习高性能单机、分布式训练和跨平台部署）

**中文介绍（README总结）**: PaddlePaddle（飞桨）是面向产业落地的深度学习与机器学习核心框架，提供高性能单机与分布式训练能力，并支持跨平台部署与从训练到推理的一体化开发。它主要服务于算法工程师与企业开发团队，覆盖制造、农业、企业服务等场景，帮助将模型快速工程化与商业化。关键技术包括动静统一、自动并行与分布式策略自动搜索，以及大模型训练与推理的统一框架支持。

**关键词**: 深度学习框架, 分布式训练, 动静统一图, 大模型训练推理一体, 跨平台部署, 高性能计算, 模型库, 端到端开发套件

**评分**: 21

**项目地址**: [GitHub](https://github.com/PaddlePaddle/Paddle)

---

## Python

## [4. Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

**语言**: Python  
**Stars**: ⭐ 0 (+605 today) | **Forks**: 🔱 14.3k

**原始描述**: Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models.

**中文介绍（README总结）**: 这是一个精选型仓库，汇集基于 RAG、AI Agents/多智能体团队、MCP 与语音代理等方案构建的各类 LLM 应用示例与项目。面向想了解、复用或对比不同大模型落地方式的开发者与研究者，覆盖 OpenAI、Anthropic、Google（Gemini）、xAI 及 Qwen、Llama 等可本地运行的开源模型。典型场景包括从代码库与网页抓取到邮箱/会议、数据分析、投研尽调、旅行与内容生产等跨领域任务的智能代理应用。

**关键词**: 检索增强生成（RAG）, AI 代理, 多代理协作, 语音代理, 多模态代理, 本地部署, 开源大模型, Shubhamsaboo

**评分**: 19

**项目地址**: [GitHub](https://github.com/Shubhamsaboo/awesome-llm-apps)

---

## [5. bytedance/deer-flow](https://github.com/bytedance/deer-flow)

**语言**: Python  
**Stars**: ⭐ 0 (+696 today) | **Forks**: 🔱 2.7k

**原始描述**: An open-source SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skills and subagents, it handles different levels of tasks that could take minutes to hours.

**中文介绍（README总结）**: DeerFlow 是一个开源的“超级智能体编排框架”，用于把研究、写代码与内容生成等任务自动化，通过协调子智能体、可扩展技能/工具、沙盒与文件系统、上下文工程和长期记忆来完成从几分钟到数小时的复杂工作。它面向希望搭建多智能体工作流的开发者与团队，提供可组合的能力模块以便按任务扩展。典型场景包括深度资料调研与总结、编程与多步骤问题求解、在隔离沙盒中执行与验证生成结果等。

**关键词**: 多智能体编排, 子代理, 技能插件, 沙箱执行, 文件系统隔离, 长期记忆, 上下文工程, 深度研究

**评分**: 42

**项目地址**: [GitHub](https://github.com/bytedance/deer-flow)

---

## [6. NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

**语言**: Python  
**Stars**: ⭐ 0 (+183 today) | **Forks**: 🔱 156

**原始描述**: 

**中文介绍（README总结）**: Hermes Agent 是一个可自部署的开源 AI 个人代理，接入你的消息账号后长期运行在服务器上，能跨会话记忆项目与偏好、按计划执行任务，并通过总结为“技能文档”逐步变强。它面向偏好终端工作流、需要持续自动化与多任务协作的个人与团队，提供完整 TUI 交互、可并行的隔离子代理，以及可通过 RPC 调用工具的脚本化能力。关键技术包括模型提供方可插拔（Nous Portal/OpenRouter/自建推理端点）、可搜索可共享且兼容 agentskills.io 的技能体系，以及本地/Docker/SSH/Singularity/Modal 等多后端沙箱执行。典型场景是长期项目助理、批量流水线任务编排、并行调研与代码生成/执行、以及在不同设备上通过消息渠道触达的持续自动化。

**关键词**: 常驻个人助理, 持久化记忆, 终端TUI界面, 任务调度, 沙箱执行环境, 多模型路由, 技能文档标准, NousResearch

**评分**: 61

**项目地址**: [GitHub](https://github.com/NousResearch/hermes-agent)

---

## [7. datagouv/datagouv-mcp](https://github.com/datagouv/datagouv-mcp)

**语言**: Python  
**Stars**: ⭐ 0 (+122 today) | **Forks**: 🔱 46

**原始描述**: Official data.gouv.fr Model Context Protocol (MCP) server that allows AI chatbots to search, explore, and analyze datasets from the French national Open Data platform, directly through conversation.

**中文介绍（README总结）**: 这是一个面向 AI 聊天机器人的 data.gouv.fr 官方 MCP 服务器，让 Claude、ChatGPT、Gemini 等可在对话中直接搜索、浏览并分析法国国家开放数据平台的数据集。主要服务于希望用自然语言快速定位和查询开放数据的开发者与数据使用者，典型问题如房地产价格有哪些数据集、巴黎最新人口数据是什么。关键在于通过 Model Context Protocol 将数据集检索与分析能力以工具形式接入聊天客户端，减少手动访问网站的流程。

**关键词**: MCP 服务器, 数据集检索, 开放数据 API, 法国开放数据, 聊天机器人连接器, 自托管部署, datagouv, datagouv-mcp

**评分**: 39

**项目地址**: [GitHub](https://github.com/datagouv/datagouv-mcp)

---

## [8. X-PLUG/MobileAgent](https://github.com/X-PLUG/MobileAgent)

**语言**: Python  
**Stars**: ⭐ 0 (+33 today) | **Forks**: 🔱 762

**原始描述**: Mobile-Agent: The Powerful GUI Agent Family

**中文介绍（README总结）**: Mobile-Agent/GUI-Owl 是阿里巴巴通义实验室推出的一组原生多平台 GUI 智能体基础模型，面向需要让模型理解界面并自动操作桌面、手机与浏览器的开发者与研究者。它基于 Qwen3-VL，强调端到端 GUI 任务执行、界面元素定位（grounding）、工具/MCP 调用与长时记忆，并在 20+ GUI 基准上达到领先表现。典型场景包括用自然语言驱动应用/网页自动化操作与评测，以及通过 OSWorld-MCP 等基准测试模型在真实工具调用流程中的能力。

**关键词**: 多平台界面自动化, 桌面自动化, 移动端自动化, 浏览器自动化, 视觉语言模型（VLM）, GUI 基础模型, 模型上下文协议（MCP）, GUI 评测基准

**评分**: 52

**项目地址**: [GitHub](https://github.com/X-PLUG/MobileAgent)

---

## [9. alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox)

**语言**: Python  
**Stars**: ⭐ 0 (+105 today) | **Forks**: 🔱 124

**原始描述**: OpenSandbox is a general-purpose sandbox platform for AI applications, offering multi-language SDKs, unified sandbox APIs, and Docker/Kubernetes runtimes for scenarios like Coding Agents, GUI Agents, Agent Evaluation, AI Code Execution, and RL Training.

**中文介绍（README总结）**: OpenSandbox 是面向 AI 应用的通用沙箱平台，为开发者提供多语言 SDK 与统一的沙箱协议/API，用于创建与管理可隔离的执行环境。它基于 Docker 与 Kubernetes 的运行时实现沙箱生命周期管理与分布式调度，并内置命令执行、文件系统与代码解释器等环境能力。典型场景包括 Coding/GUI Agents 的安全执行与自动化（如浏览器、桌面/VNC、VS Code）、Agent 评测、AI 代码执行以及强化学习训练等。

**关键词**: 沙箱执行环境, 代码执行隔离, 统一沙箱 API, 沙箱协议, 多语言 SDK, 分布式调度, 网络策略控制, 浏览器自动化

**评分**: 42

**项目地址**: [GitHub](https://github.com/alibaba/OpenSandbox)

---

## Shell

## [10. anthropics/claude-code](https://github.com/anthropics/claude-code)

**语言**: Shell  
**Stars**: ⭐ 0 (+494 today) | **Forks**: 🔱 5.7k

**原始描述**: Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

**中文介绍（README总结）**: Claude Code 是一个运行在终端的智能编码代理，能够理解你的代码库，通过自然语言指令执行常规开发任务、解释复杂代码并协助处理 Git 工作流，从而提升编码效率。它面向日常写代码的开发者，可在终端、IDE 中使用，也支持在 GitHub 上通过 @claude 触发协作。项目还提供插件机制，用自定义命令和代理扩展能力，适用于代码梳理、批量改动、提交与分支操作等场景。

**关键词**: 终端编程助手, 代码智能体, 自然语言指令, Git 工作流自动化, 代码解释, 例行任务自动化, 插件系统, anthropics

**评分**: 82

**项目地址**: [GitHub](https://github.com/anthropics/claude-code)

---

## [11. obra/superpowers](https://github.com/obra/superpowers)

**语言**: Shell  
**Stars**: ⭐ 0 (+1.5k today) | **Forks**: 🔱 5.0k

**原始描述**: An agentic skills framework & software development methodology that works.

**中文介绍（README总结）**: Superpowers 是一套面向编码代理的“技能”框架与软件开发方法论，让代理在开始写代码前先通过对话澄清目标并产出可阅读的规格说明，再在你确认设计后生成实现计划并按计划推进。它强调红/绿 TDD、YAGNI 与 DRY，并通过子代理驱动的开发流程把任务拆分执行、检查与评审，从而让代理能更长时间自主工作而不偏离既定方案。主要面向使用 Claude/Cursor/Codex 等工具的开发者团队或个人，用于从需求到实现的端到端代理化开发与协作。

**关键词**: 编码代理工作流, 代理技能框架, 可组合技能, 需求澄清, 规格说明生成, 设计评审流程, 实现计划生成, 多代理协作开发, 任务分解与执行, 测试驱动开发（TDD）

**评分**: 30

**项目地址**: [GitHub](https://github.com/obra/superpowers)

---

## TypeScript

## [12. ruvnet/ruflo](https://github.com/ruvnet/ruflo)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+531 today) | **Forks**: 🔱 1.8k

**原始描述**: 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code / Codex Integration

**中文介绍（README总结）**: Ruflo v3 是面向 Claude Code 的企业级多智能体编排平台，用于把对话式 AI 与复杂软件工程工作流组织成可自动协作的“智能体群”，在编码、评审、测试、安全审计、文档与 DevOps 等任务中分工协作并持续优化。它支持同时运行大量专用智能体并通过层级或网状协作模式共享上下文、自动拆分任务，具备自学习路由、容错一致性与企业级安全能力。关键技术包括基于 Rust 的 WASM 内核与策略/嵌入/证明相关组件、分布式群体智能、RAG 集成，以及对 Claude/GPT 等多模型的原生集成与可切换/故障切换。典型场景是团队在代码库上构建自动化开发流水线、端到端交付与质量保障的多智能体协作。

**关键词**: 多智能体编排, 智能体群体协作, 自主工作流, LLM 路由与故障切换, 分布式共识, 容错架构, 企业级安全, ruvnet

**评分**: 59

**项目地址**: [GitHub](https://github.com/ruvnet/ruflo)

---

## [13. superset-sh/superset](https://github.com/superset-sh/superset)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+156 today) | **Forks**: 🔱 176

**原始描述**: IDE for the AI Agents Era - Run an army of Claude Code, Codex, etc. on your machine

**中文介绍（README总结）**: Superset 是面向 AI 编码代理时代的“终端式 IDE”，用于在本机同时运行多个基于 CLI 的编码代理（如 Claude Code、Codex 等）并统一管理。它通过为每个任务隔离 git worktree、集中监控与通知、内置 diff 查看与编辑，降低多代理协作的上下文切换与互相干扰。典型场景是开发者并行拆分多项编码/修复/重构任务，让不同代理各自推进并快速审阅合并改动。

**关键词**: 工作区生命周期脚本, 差异审阅工具, Agent监控与通知, 可定制键盘快捷键, superset-sh, superset, IDE, Agent

**评分**: 49

**项目地址**: [GitHub](https://github.com/superset-sh/superset)

---

