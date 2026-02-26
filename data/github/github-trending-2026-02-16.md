# GitHub Trending 日榜 | 2026-02-16

> 共 11 个项目

## 📑 目录

- [Python](#Python) (5 个项目)
- [Rust](#Rust) (1 个项目)
- [Shell](#Shell) (1 个项目)
- [TypeScript](#TypeScript) (4 个项目)

---

## Python

## [1. D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)

**语言**: Python  
**Stars**: ⭐ 0 (+1.7k today) | **Forks**: 🔱 1.0k

**原始描述**: 🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl!

**中文介绍（README总结）**: Scrapling 是一个自适应的 Web 抓取框架，既能处理单次请求也能扩展到并发的大规模爬取，面向爬虫开发者与需要抓取能力的普通用户。它的解析器会根据页面结构变化自动重新定位元素，并提供可绕过常见反爬（如 Cloudflare Turnstile）的抓取器。框架支持类似 Scrapy 的 Spider API、多会话（HTTP 与无头浏览器统一）、暂停/恢复、代理轮换以及流式输出与实时统计，适用于长期运行的数据采集、UI/数据管道对接和多站点持续监测等场景。

**关键词**: 网页爬虫框架, 自适应网页解析, 选择器自愈, 反爬绕过, 代理轮换, 无头浏览器抓取, 断点续爬, 流式数据输出

**评分**: 62

**项目地址**: [GitHub](https://github.com/D4Vinci/Scrapling)

---

## [2. huggingface/skills](https://github.com/huggingface/skills)

**语言**: Python  
**Stars**: ⭐ 0 (+1.5k today) | **Forks**: 🔱 394

**原始描述**: 

**中文介绍（README总结）**: Hugging Face Skills 是一套用于数据集创建、模型训练与评估等 AI/ML 任务的“技能”定义仓库，把针对特定用例的说明、脚本与资源封装成自包含目录，并用带 YAML 头信息的文件提供给编码代理读取执行。它面向使用各类编程/代码代理工具的开发者与研究者，采用标准化的 Agent Skill 格式以便在 Claude Code、OpenAI Codex、Gemini CLI、Cursor 等环境中互操作。典型场景是在不同代理工具间复用同一套任务流程与指令，让代理按需加载对应技能完成端到端的开发与评测工作。

**关键词**: 编码代理集成, 代理技能包, 插件式工作流, 跨工具互操作, YAML 前置元数据, 数据集构建, 模型训练, 模型评测

**评分**: 47

**项目地址**: [GitHub](https://github.com/huggingface/skills)

---

## [3. datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents)

**语言**: Python  
**Stars**: ⭐ 0 (+222 today) | **Forks**: 🔱 2.6k

**原始描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**中文介绍（README总结）**: Hello-Agents（《从零开始构建智能体》）是 Datawhale 发起的系统性教程，面向有一定 Python 与 LLM 调用基础的开发者/学生/自学者，讲清并带练从单智能体到多智能体的 AI Native Agent 设计与实现。内容围绕智能体核心原理与经典范式（如 ReAct）、上下文工程与 Memory/协议/评估等关键技术，并结合主流平台与框架实践，最终还会基于 OpenAI 原生 API 自研一个智能体框架。典型场景是用智能体方法落地真实应用与综合项目，如智能旅行助手、赛博小镇等。

**关键词**: 多智能体协作, Agent工作流编排, 记忆系统与长期记忆, 上下文工程, Agent评估与基准测试, 低代码智能体平台, datawhalechina, hello-agents

**评分**: 26

**项目地址**: [GitHub](https://github.com/datawhalechina/hello-agents)

---

## [4. VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)

**语言**: Python  
**Stars**: ⭐ 0 (+378 today) | **Forks**: 🔱 1.3k

**原始描述**: 📑 PageIndex: Document Index for Vectorless, Reasoning-based RAG

**中文介绍（README总结）**: PageIndex 是一种面向长篇专业文档的“无向量、基于推理”的 RAG 框架/平台，通过构建层级树状索引，让 LLM 在索引上进行多步推理检索，避免传统向量相似度搜索与切块带来的相关性偏差。它主要服务于需要高准确度文档分析的专业用户与应用，也可作为可集成的检索组件用于聊天平台、API/MCP 等形态。典型场景包括对复杂报告、手册、论文等进行人类式定位与证据追溯，以及直接对 PDF 页面图像进行无需 OCR 的视觉检索增强问答。

**关键词**: 无向量检索, 推理基础RAG, 层次树索引, 人类检索, 长文档分析, 领域专业知识, 上下文感知检索, PDF图像处理

**评分**: 72

**项目地址**: [GitHub](https://github.com/VectifyAI/PageIndex)

---

## [5. NVIDIA/Megatron-LM](https://github.com/NVIDIA/Megatron-LM)

**语言**: Python  
**Stars**: ⭐ 0 (+10 today) | **Forks**: 🔱 3.6k

**原始描述**: Ongoing research training transformer models at scale

**中文介绍（README总结）**: Megatron-LM/Megatron Core 是面向大规模 Transformer 训练的 GPU 优化库与参考实现：Megatron-LM 提供包含 Core 的预配置训练脚本，便于研究团队学习分布式训练与快速实验；Megatron Core 提供可组合的高性能构件，适合框架开发者和工程团队构建自定义训练流水线。它重点支持多种并行策略（TP/PP/DP/EP/CP）、混合精度（FP16/BF16/FP8/FP4）与相关模型结构，并可通过 Megatron Bridge 与 Hugging Face 进行双向 checkpoint 转换。典型场景包括在多 GPU/多节点环境中训练或扩展大模型、研究并行与精度优化、以及在不同生态间迁移与复用模型权重。

**关键词**: 变压器模型, 混合精度, 模型架构, 检查点转换, NVIDIA, Megatron-LM, Ongoing, research

**评分**: 44

**项目地址**: [GitHub](https://github.com/NVIDIA/Megatron-LM)

---

## Rust

## [6. katanemo/plano](https://github.com/katanemo/plano)

**语言**: Rust  
**Stars**: ⭐ 0 (+205 today) | **Forks**: 🔱 336

**原始描述**: Delivery infrastructure for agentic apps - Plano is an AI-native proxy and data plane that offloads plumbing work, so you stay focused on your agent's core logic (via any AI framework).

**中文介绍（README总结）**: Plano 是面向 agentic 应用的 AI 原生代理服务器与数据平面，把路由与编排、可观测性信号与追踪、护栏过滤与审核、以及多模型/多供应商的智能路由等“中间件”能力从业务代码中抽离出来。它主要服务需要将智能体应用安全、可靠、可重复地推向生产的开发团队，支持任意语言和 AI 框架接入。关键技术体现在低延迟多智能体编排、基于别名/偏好/自动策略的 LLM 路由、零代码采集信号与 OTEL traces/metrics，以及通过过滤链统一实现越狱防护、审核策略与记忆钩子。典型场景包括多智能体路由与扩展、线上持续评估与观测、统一安全与内容治理、以及模型切换与成本/效果优化。

**关键词**: AI 原生代理（proxy）, 多 Agent 编排, katanemo, plano, Delivery, infrastructure, agentic, apps

**评分**: 74

**项目地址**: [GitHub](https://github.com/katanemo/plano)

---

## Shell

## [7. obra/superpowers](https://github.com/obra/superpowers)

**语言**: Shell  
**Stars**: ⭐ 0 (+1.2k today) | **Forks**: 🔱 4.8k

**原始描述**: An agentic skills framework & software development methodology that works.

**中文介绍（README总结）**: Superpowers 是一套面向“编码代理”的软件开发方法论与工作流框架，通过可组合的“技能”和初始指令让代理在写代码前先澄清目标、抽取规格并分段呈现给用户确认。确认设计后，它会生成可执行的实现计划，强调红绿 TDD、YAGNI 和 DRY，然后以“子代理驱动开发”方式分解任务、执行与审查，尽量在不偏离既定计划的前提下长时间自动推进。适用于使用 Claude/Cursor/Codex 等工具的开发者在构建新功能或项目时，将需求梳理、方案评审、实现与代码审查流程更系统化与可自动化。

**关键词**: 编码智能体工作流, 智能体技能框架, 可组合技能, 需求澄清, 规格说明生成, 设计评审流程, 实现计划生成, 子智能体协作, 任务分解与审查, 测试驱动开发（TDD）

**评分**: 27

**项目地址**: [GitHub](https://github.com/obra/superpowers)

---

## TypeScript

## [8. abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+894 today) | **Forks**: 🔱 363

**原始描述**: GitNexus: The Zero-Server Code Intelligence Engine - GitNexus is a client-side knowledge graph creator that runs entirely in your browser. Drop in a GitHub repo or ZIP file, and get an interactive knowledge graph wit a built in Graph RAG Agent. Perfect for code exploration

**中文介绍（README总结）**: GitNexus 是一个客户端知识图谱创建工具，完全在浏览器中运行，用户只需上传 GitHub 仓库或 ZIP 文件，即可生成交互式知识图谱，适合代码探索。它面向开发者和 AI 代理，通过索引代码库中的每个依赖、调用链和执行流程，提供智能工具，帮助 AI 代理更好地理解和分析代码。典型场景包括在 Web UI 中与代码库进行对话，或通过 CLI 和 MCP 服务器为 AI 代理提供深度的代码库意识，从而提升代码分析的准确性和效率。

**关键词**: 客户端本地运行, 浏览器端分析, 代码知识图谱, 代码库索引, 依赖图谱, 执行流分析, MCP 服务器, CLI 工具链, 编辑器集成

**评分**: 51

**项目地址**: [GitHub](https://github.com/abhigyanpatwari/GitNexus)

---

## [9. bytedance/deer-flow](https://github.com/bytedance/deer-flow)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+59 today) | **Forks**: 🔱 2.6k

**原始描述**: An open-source SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skills and subagents, it handles different levels of tasks that could take minutes to hours.

**中文介绍（README总结）**: DeerFlow 2.0 是一个开源的“超级智能体”编排框架，用于让智能体在较长时间跨度内完成研究、写代码与内容产出等复杂任务。它面向需要构建/运行多智能体工作流的开发者与团队，核心通过可扩展的技能与工具系统，协同子智能体、长期记忆、上下文工程以及沙箱与文件系统来执行任务。典型场景包括深度资料调研与报告生成、跨文件的代码实现与修改、以及在受控沙箱环境中进行自动化实验与产物交付。

**关键词**: 多智能体编排, 技能与工具插件体系, 沙箱执行环境, 文件系统隔离, 长时记忆管理, 上下文工程, 任务分解与规划, 深度研究自动化, 代码生成与执行, 工作流自动化平台

**评分**: 40

**项目地址**: [GitHub](https://github.com/bytedance/deer-flow)

---

## [10. shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+175 today) | **Forks**: 🔱 3.8k

**原始描述**: Bash is all you need - A nano Claude Code–like agent, built from 0 to 1

**中文介绍（README总结）**: 这是一个从 0 到 1 教你用 Bash 搭建“迷你 Claude Code 风格”智能体的学习型项目，通过 12 个循序渐进的 session 在不改核心循环的前提下逐步叠加工具处理、计划可视化、进程/上下文隔离、按需加载知识、策略性遗忘与文件化状态等机制。面向想理解代码智能体工作原理与架构取舍的开发者/学习者，强调用最少构件复现可运行的 agent 模式。典型场景是作为教学与原型实验：搭建可循环执行任务的脚本化 agent，并扩展到异步协作、任务板与自组织执行等基础能力；仓库明确不追求完整生产级事件总线等机制。

**关键词**: 自主执行, 机制层叠, 任务协调, 上下文隔离, 非阻塞线程, 策略遗忘, 状态持久化, 异步邮箱

**评分**: 70

**项目地址**: [GitHub](https://github.com/shareAI-lab/learn-claude-code)

---

## [11. siteboon/claudecodeui](https://github.com/siteboon/claudecodeui)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+73 today) | **Forks**: 🔱 902

**原始描述**: Use Claude Code, Cursor CLI or Codex on mobile and web with CloudCLI (aka Claude Code UI). CloudCLI is a free open source webui/GUI that helps you manage your Claude Code session and projects remotely

**中文介绍（README总结）**: CloudCLI（又称 Claude Code UI）是一个开源的跨端 WebUI/GUI，用于在桌面和移动端远程管理 Claude Code、Cursor CLI 或 Codex 的会话与项目。它面向需要随时随地查看与操作 CLI 编程助手的开发者，提供交互式聊天、内置终端、文件树与在线编辑、Git 变更/分支管理以及会话历史与多会话管理等能力。典型场景是外出时用手机继续处理正在运行的 AI 编码会话、审阅并提交代码改动，或在不同设备间无缝接力同一项目工作。

**关键词**: LLM 编程助手 UI, 远程 CLI 管理, 跨端响应式 WebUI, 移动端开发工具, 交互式聊天界面, 集成终端, 文件浏览器与在线编辑, Git 可视化操作, 多模型兼容

**评分**: 38

**项目地址**: [GitHub](https://github.com/siteboon/claudecodeui)

---

