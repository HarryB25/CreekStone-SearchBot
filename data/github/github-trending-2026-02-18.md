# GitHub Trending 日榜 | 2026-02-18

> 共 10 个项目

## 📑 目录

- [Python](#Python) (5 个项目)
- [Rust](#Rust) (1 个项目)
- [Shell](#Shell) (1 个项目)
- [TypeScript](#TypeScript) (3 个项目)

---

## Python

## [1. D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)

**语言**: Python  
**Stars**: ⭐ 0 (+1.7k today) | **Forks**: 🔱 1.1k

**原始描述**: 🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl!

**中文介绍（README总结）**: Scrapling 是一个自适应的 Python Web 爬取框架，既能处理单次请求也能扩展到并发的全站/大规模抓取，面向爬虫开发者及需要抓取数据的普通用户。它主打“会自我修复”的解析能力（页面改版后自动重新定位元素），并提供多种抓取会话（HTTP 与隐身无头浏览器等）、代理轮换、断点续爬、流式输出与实时统计等能力。典型场景包括在网站结构频繁变化或存在反爬（如 Cloudflare Turnstile）时的稳定采集，以及需要多会话并发、可暂停恢复的长期爬取任务。

**关键词**: 网页抓取框架, 网络爬虫框架, 异步回调, 元素定位自适应, 反爬绕过, 代理轮换, 断点续爬, 无头浏览器集成

**评分**: 31

**项目地址**: [GitHub](https://github.com/D4Vinci/Scrapling)

---

## [2. huggingface/skills](https://github.com/huggingface/skills)

**语言**: Python  
**Stars**: ⭐ 0 (+1.5k today) | **Forks**: 🔱 396

**原始描述**: 

**中文介绍（README总结）**: Hugging Face Skills 提供一组面向数据集创建、模型训练与评测等 AI/ML 任务的“技能”定义与资源封装，让编码代理在特定用例下按指引执行。它面向使用 Claude Code、OpenAI Codex、Gemini CLI、Cursor 等主流智能编程工具的开发者，采用标准化的 Agent Skill 格式，将说明、脚本与资源打包为自包含目录，并通过带 YAML 头信息的指引文件被代理发现与加载。典型场景是为不同代理统一复用任务流程、快速启用特定工作流或在不原生支持技能时直接使用相应指引文件。

**关键词**: 编码智能体, 技能插件（skill）, 跨工具互操作, YAML 前置元数据, 目录式技能包, 指令模板, 插件市场注册, 命令行智能体, 模型训练自动化, 数据集构建, 模型评测自动化

**评分**: 49

**项目地址**: [GitHub](https://github.com/huggingface/skills)

---

## [3. datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents)

**语言**: Python  
**Stars**: ⭐ 0 (+222 today) | **Forks**: 🔱 2.6k

**原始描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**中文介绍（README总结）**: Hello-Agents（《从零开始构建智能体》）是一套面向社区的系统性教程，带你从智能体核心原理出发，动手实现并搭建 AI Native 的单体到多智能体系统与应用。它主要面向具备 Python 与基础 LLM API 使用经验的 AI 开发者、软件工程师和学生，强调“穿透框架表象”理解经典范式（如 ReAct）、上下文工程、Memory、协议与评估等关键技术。典型场景包括用主流平台/框架进行智能体开发，以及从零构建自研智能体框架并完成旅行助手、赛博小镇等综合实战项目。

**关键词**: 多智能体系统, LLM 智能体, 智能体编排, 上下文工程, 智能体记忆, 智能体评估, datawhalechina, hello-agents

**评分**: 24

**项目地址**: [GitHub](https://github.com/datawhalechina/hello-agents)

---

## [4. VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)

**语言**: Python  
**Stars**: ⭐ 0 (+378 today) | **Forks**: 🔱 1.3k

**原始描述**: 📑 PageIndex: Document Index for Vectorless, Reasoning-based RAG

**中文介绍（README总结）**: PageIndex 是一种面向长篇专业文档的“无向量、基于推理”的 RAG/文档分析框架与平台，通过构建分层树状索引，让 LLM 在索引上进行代理式、上下文感知的检索与定位，避免向量库与切分带来的相似度偏差。它主要服务于需要多步推理与领域知识的文档问答/分析场景（如报告、手册、研究资料），并支持直接在 PDF 页面图像上进行视觉式（可不依赖 OCR）的检索工作流，也可通过 API/MCP 集成到现有系统中。

**关键词**: 无向量 RAG, 推理式检索, 层级树索引, 免向量数据库, 免分块, 上下文内索引, 文档分析 Agent, PDF 页面检索

**评分**: 53

**项目地址**: [GitHub](https://github.com/VectifyAI/PageIndex)

---

## [5. NVIDIA/Megatron-LM](https://github.com/NVIDIA/Megatron-LM)

**语言**: Python  
**Stars**: ⭐ 0 (+10 today) | **Forks**: 🔱 3.6k

**原始描述**: Ongoing research training transformer models at scale

**中文介绍（README总结）**: Megatron-LM/Megatron Core 是面向大规模 Transformer 训练的 GPU 优化库与参考实现：Megatron-LM 提供包含 Core 的预配置训练脚本，便于研究团队学习分布式训练与快速实验；Megatron Core 则提供可组合的高性能组件，供框架开发者与 ML 工程师构建自定义训练流水线。其关键技术包括多种并行策略（张量/流水/数据/专家/上下文并行等）、混合精度（FP16/BF16/FP8/FP4）与 Transformer 架构构件，并提供 Megatron Bridge 用于 Hugging Face 与 Megatron 间的双向 checkpoint 转换。典型场景是训练与扩展大模型、实现 MoE 等高级并行与精度优化，以及在不同生态间迁移或复用模型权重。

**关键词**: 分布式训练, GPU 加速训练框架, NVIDIA, Megatron-LM, Ongoing, research, training, transformer

**评分**: 49

**项目地址**: [GitHub](https://github.com/NVIDIA/Megatron-LM)

---

## Rust

## [6. katanemo/plano](https://github.com/katanemo/plano)

**语言**: Rust  
**Stars**: ⭐ 0 (+205 today) | **Forks**: 🔱 337

**原始描述**: Delivery infrastructure for agentic apps - Plano is an AI-native proxy and data plane that offloads plumbing work, so you stay focused on your agent's core logic (via any AI framework).

**中文介绍（README总结）**: Plano 是面向 agentic 应用的 AI 原生代理与数据平面，用来把路由、编排、可观测性/评估、守护栏与模型调用等“中间件式”的交付工作从业务代码和具体框架中剥离出来。它主要服务于要将多智能体应用安全、稳定、可重复地推向生产的开发团队，支持任意语言和 AI 框架接入。关键技术包括低延迟多智能体编排、按别名/偏好进行的 LLM 路由、零代码采集的信号与 OTEL traces/metrics、以及基于过滤链的安全审核与记忆/策略钩子，典型场景是生产环境中的多代理路由与治理、持续改进的观测闭环和模型供应商切换。

**关键词**: AI 原生代理, 数据平面, 智能体编排, 智能体路由, 模型抽象层, 可观测性, 安全护栏, 内容审核

**评分**: 55

**项目地址**: [GitHub](https://github.com/katanemo/plano)

---

## Shell

## [7. obra/superpowers](https://github.com/obra/superpowers)

**语言**: Shell  
**Stars**: ⭐ 0 (+1.2k today) | **Forks**: 🔱 4.8k

**原始描述**: An agentic skills framework & software development methodology that works.

**中文介绍（README总结）**: Superpowers 是一套面向“编码智能体”的软件开发方法与工作流框架，通过可组合的“技能”和初始指令，让智能体先从对话中澄清目标并提炼规格说明，再分段呈现设计供人确认。确认后它会生成可执行的实现计划，强调真正的红/绿 TDD、YAGNI 与 DRY，并用子智能体分工推进任务、检查与复审，尽量在不偏离计划的前提下长时间自治开发。典型场景是用 Claude/Cursor/Codex 等编码助手进行较复杂功能或项目的端到端开发与迭代。

**关键词**: 编程代理工作流, 代理技能框架, 可组合技能, 规格澄清, 设计评审, 实现计划生成, 子代理协作开发, 任务分解与审查, 测试驱动开发（TDD）, 插件市场集成

**评分**: 41

**项目地址**: [GitHub](https://github.com/obra/superpowers)

---

## TypeScript

## [8. abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+894 today) | **Forks**: 🔱 370

**原始描述**: GitNexus: The Zero-Server Code Intelligence Engine - GitNexus is a client-side knowledge graph creator that runs entirely in your browser. Drop in a GitHub repo or ZIP file, and get an interactive knowledge graph wit a built in Graph RAG Agent. Perfect for code exploration

**中文介绍（README总结）**: GitNexus 是一个零服务器的代码智能引擎：在浏览器端或通过 CLI 将 GitHub 仓库/ZIP 索引为知识图谱，覆盖依赖关系、调用链、聚类与执行流，并提供可交互的图谱与内置 Graph RAG 代理用于查询与分析。它面向需要快速理解与深入分析大型代码库的开发者，以及希望让 Cursor、Claude Code 等 AI 编程代理获得可靠上下文的用户。典型场景是代码探索、架构与影响分析、排查遗漏依赖/断裂调用链，减少代理“盲改”带来的错误。

**关键词**: 代码智能, 代码知识图谱, 代码库索引, 依赖图, 执行流分析, 浏览器端运行, 零服务器架构, MCP 服务器, 编辑器集成

**评分**: 44

**项目地址**: [GitHub](https://github.com/abhigyanpatwari/GitNexus)

---

## [9. bytedance/deer-flow](https://github.com/bytedance/deer-flow)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+59 today) | **Forks**: 🔱 2.6k

**原始描述**: An open-source SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skills and subagents, it handles different levels of tasks that could take minutes to hours.

**中文介绍（README总结）**: DeerFlow 2.0 是一个开源的“超级智能体”编排框架，用来让智能体在沙箱环境中进行研究、写代码并产出结果，覆盖从几分钟到数小时的多阶段任务。它面向需要构建复杂 Agent 工作流的开发者/研究者，核心通过可扩展的技能与工具体系，把子智能体、上下文工程、文件系统沙箱和长期记忆统一协调起来。典型场景包括深度调研与报告生成、自动化编码与修复、以及需要隔离执行与持久记忆的复杂任务流水线。

**关键词**: 多智能体系统, 技能框架, 沙箱执行, 代码生成, 深度研究, 长时记忆, 上下文工程, 文件系统隔离

**评分**: 35

**项目地址**: [GitHub](https://github.com/bytedance/deer-flow)

---

## [10. shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+175 today) | **Forks**: 🔱 3.8k

**原始描述**: Bash is all you need - A nano Claude Code–like agent, built from 0 to 1

**中文介绍（README总结）**: 这是一个从 0 到 1 的学习型仓库，演示如何用 Bash 为核心循环构建一个“类 Claude Code”的轻量智能体，并通过 12 个递进 session 逐步叠加机制而不改动主循环。面向想理解/复刻终端智能体核心模式的开发者，重点涵盖可见计划、工具处理器扩展、进程/上下文隔离、按需注入知识、遗忘与压缩后的持久状态、异步线程与邮箱、无协调者的自组织协作，以及按目录隔离与任务 ID 协调等关键技术。典型场景是把命令行工具编排成可持续运行、可拆分子任务并能并发协作的自动化执行代理，用于学习与原型验证而非完整生产系统。

**关键词**: 命令行智能体, 可见规划, 进程隔离, 上下文隔离, 上下文压缩, 文件状态持久化, 异步消息队列, 有限状态机, 任务看板调度

**评分**: 35

**项目地址**: [GitHub](https://github.com/shareAI-lab/learn-claude-code)

---

