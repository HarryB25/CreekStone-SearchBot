# GitHub Trending 日榜 | 2026-02-14

> 共 10 个项目

## 📑 目录

- [C++](#Cplusplus) (1 个项目)
- [Go](#Go) (1 个项目)
- [JavaScript](#JavaScript) (1 个项目)
- [Python](#Python) (2 个项目)
- [Ruby](#Ruby) (1 个项目)
- [TypeScript](#TypeScript) (4 个项目)

---

## C++

## [1. alibaba/zvec](https://github.com/alibaba/zvec)

**语言**: C++  
**Stars**: ⭐ 0 (+186 today) | **Forks**: 🔱 63

**原始描述**: A lightweight, lightning-fast, in-process vector database

**中文介绍（README总结）**: Zvec 是一个开源、可嵌入应用的轻量级向量数据库，提供生产级的低延迟、可扩展相似度检索。面向需要在本地进程中做高性能向量搜索的开发者与团队，适用于笔记本、服务器、CLI 工具和边缘设备等环境。基于阿里巴巴的 Proxima，支持稠密与稀疏向量、多向量联合查询与结合结构化过滤的混合检索，可在海量向量规模下快速返回结果，典型用于语义相似检索与精确筛选场景。

**关键词**: 进程内库, 相似度搜索, 稠密向量, 稀疏向量, 混合检索, 多向量查询, C++ 实现, 跨平台, 边缘部署, 低延迟

**评分**: 17

**项目地址**: [GitHub](https://github.com/alibaba/zvec)

---

## Go

## [2. minio/minio](https://github.com/minio/minio)

**语言**: Go  
**Stars**: ⭐ 0 (+37 today) | **Forks**: 🔱 7.0k

**原始描述**: MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license.

**中文介绍（README总结）**: MinIO 是一款高性能、与 S3 兼容的开源对象存储，用于支撑 AI/ML、数据分析和其他数据密集型工作负载。面向需要在本地或自建环境中使用 S3 接口的团队与社区用户，强调速度与可扩展性。关键特性包括完整的 S3 API 兼容和面向大规模数据管线的优化，典型场景涵盖模型训练数据管理、分析数据湖与高吞吐对象存储；该仓库已不再维护，官方给出了 AIStor Free/Enterprise 作为替代。

**关键词**: S3 兼容, 自托管, 高性能存储, 可扩展性, 裸金属部署, Go 语言, 大规模数据管道, S3 生态集成

**评分**: 27

**项目地址**: [GitHub](https://github.com/minio/minio)

---

## JavaScript

## [3. SynkraAI/aios-core](https://github.com/SynkraAI/aios-core)

**语言**: JavaScript  
**Stars**: ⭐ 0 (+223 today) | **Forks**: 🔱 234

**原始描述**: Synkra AIOS: AI-Orchestrated System for Full Stack Development - Core Framework v4.0

**中文介绍（README总结）**: Synkra AIOS 是一个以 CLI 为核心的 AI 代理编排框架，用于自修改、全栈导向的敏捷开发。面向希望由 AI 主导研发流程的团队与个人，除软件开发外也可应用于娱乐、写作、商业策略与个人助理等领域。其关键技术是多代理协作的两阶段流程：规划代理（analyst/pm/architect）生成一致的 PRD 与架构并进行人机共改，Scrum Master 将其转化为包含完整上下文的超细化开发故事，解决规划不一致与上下文丢失问题；典型场景是通过 CLI 驱动从需求到实现的端到端开发与项目管理。

**关键词**: 人类在环, 提示工程, 全栈开发, 架构文档生成, 开发故事生成, 上下文保留, SynkraAI, aios-core

**评分**: 46

**项目地址**: [GitHub](https://github.com/SynkraAI/aios-core)

---

## Python

## [4. ruvnet/wifi-densepose](https://github.com/ruvnet/wifi-densepose)

**语言**: Python  
**Stars**: ⭐ 0 (+83 today) | **Forks**: 🔱 549

**原始描述**: Production-ready implementation of InvisPose - a revolutionary WiFi-based dense human pose estimation system that enables real-time full-body tracking through walls using commodity mesh routers

**中文介绍（README总结）**: 这是一个基于WiFi的致密人体姿态估计系统，利用路由器的CSI信号与机器学习实现穿墙的实时全身追踪，无需摄像头、支持最多10人且兼顾隐私，兼容常见路由/AP并提供生产级Rust实现（<50ms延迟、30FPS）。面向企业级应用开发者、医疗/养老与健身产品、智能家居与安防集成商及应急救援团队，配有认证、限流与监控的API及WebSocket数据流。典型场景包括跌倒检测、活动识别与占用监测、家庭健身与安防监控；并提供“WiFi‑Mat”扩展用于地震、建筑坍塌等搜救中的幸存者定位。

**关键词**: 人体姿态估计, 实时多人跟踪, 隐私保护, 跌倒检测, 活动识别, 灾害搜救, ruvnet, wifi-densepose

**评分**: 48

**项目地址**: [GitHub](https://github.com/ruvnet/wifi-densepose)

---

## [5. Zipstack/unstract](https://github.com/Zipstack/unstract)

**语言**: Python  
**Stars**: ⭐ 0 (+24 today) | **Forks**: 🔱 597

**原始描述**: No-code LLM Platform to launch APIs and ETL Pipelines to structure unstructured documents

**中文介绍（README总结）**: Unstract 是面向企业与数据/运营团队的无代码 LLM 平台，用于将非结构化文档自动结构化并快速发布提取 API 与 ETL 流水线。其关键技术包括 Prompt Studio 的模式定义与跨模型对比、成本监控与通用提示工程，以及与 LLM、向量数据库、嵌入模型、文本提取器的集成，支撑高准确度的文档型代理工作流。典型场景包括对信用卡账单等多样文档的字段抽取、对账与合规归档，并将文档数据接入内部系统与分析管道。

**关键词**: 文档结构化, 文本抽取, 无代码, 提示工程, LLM 对比评估, 模式定义, 成本监控, 自托管部署

**评分**: 54

**项目地址**: [GitHub](https://github.com/Zipstack/unstract)

---

## Ruby

## [6. ruby/ruby](https://github.com/ruby/ruby)

**语言**: Ruby  
**Stars**: ⭐ 0 (+6 today) | **Forks**: 🔱 5.6k

**原始描述**: The Ruby Programming Language

**中文介绍（README总结）**: Ruby 是一种解释型面向对象编程语言，面向希望快速构建 Web 应用与自动化脚本的开发者，也适合处理文本、序列化文件和系统任务管理。它具备简单语法与可扩展的面向对象能力（类、mixin、单例方法）、迭代器与闭包、异常处理、运算符重载、垃圾回收，并在多平台上高度可移植。典型场景包括使用 Web 框架进行网站开发、编写数据与日志处理脚本、以及跨平台运维与工具原型开发。

**关键词**: 解释型语言, 脚本编程, 文本处理, 简洁语法, 运算符重载, 异常处理, 迭代器与闭包, 垃圾回收, 跨平台兼容

**评分**: 0

**项目地址**: [GitHub](https://github.com/ruby/ruby)

---

## TypeScript

## [7. tambo-ai/tambo](https://github.com/tambo-ai/tambo)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+137 today) | **Forks**: 🔱 463

**原始描述**: Generative UI SDK for React

**中文介绍（README总结）**: Tambo AI 是开源的 React 生成式 UI 工具包，用于构建能“说你的 UI”的代理：注册组件的 Zod 模式，代理选择合适组件并将 props 以流式生成供用户交互。面向希望在 React 应用中加入对话式/生成式界面的开发者与产品团队，提供前端 SDK 与后端以管理会话与代理执行。关键能力包括流式传参、状态管理与 MCP 支持，兼容 OpenAI、Anthropic、Gemini、Mistral 等提供商并可与 LangChain/Mastra 协同；典型场景如“按地区显示销售额”自动渲染图表、“添加任务”更新任务列表，可云托管或自部署。

**关键词**: 生成式UI, UI代理, 流式渲染, 代理编排, 云托管后端, tambo-ai, tambo, 描述与README

**评分**: 49

**项目地址**: [GitHub](https://github.com/tambo-ai/tambo)

---

## [8. rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+226 today) | **Forks**: 🔱 476

**原始描述**: Open-source AI coworker, with memory

**中文介绍（README总结）**: Rowboat 是开源、本地优先的 AI 协作助手，连接你的邮件与会议笔记，持续构建可视化的知识图谱与 Obsidian 兼容的 Markdown 资料库作为长期记忆，在本机私密地用上下文帮助你完成工作。面向需要在邮件、会议与文档流中高效整理与复用知识的个人与团队知识工作者。关键技术包括从 Gmail/Granola/Fireflies 等数据自动抽取关系与回链形成长期知识、上下文理解与动作执行，以及可选语音备忘录捕捉；典型场景是会前速览相关决策与开放问题、在回复邮件与写作时生成摘要和草稿、产出简报或 PDF 幻灯片。

**关键词**: 本地优先, 知识图谱, 长期记忆, 上下文感知, 智能协作助手, 反向链接, 邮件集成, 语音笔记

**评分**: 62

**项目地址**: [GitHub](https://github.com/rowboatlabs/rowboat)

---

## [9. ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+326 today) | **Forks**: 🔱 1.5k

**原始描述**: Chrome DevTools for coding agents

**中文介绍（README总结）**: Chrome DevTools MCP 是一个为编码代理（如 Gemini、Claude、Cursor、Copilot）提供的 MCP 服务器，让智能助手可控制并检查实时 Chrome 浏览器，用于可靠的自动化、深度调试与性能分析。面向需要在浏览器内进行自动化操作与诊断的开发者与代理构建者，核心技术包括 Model-Context-Protocol、Chrome DevTools、Puppeteer，并可结合 CrUX 实地数据获取性能洞察。典型场景包括记录与解析性能追踪、分析网络请求与控制台（含源码映射堆栈）、自动执行并等待页面交互结果；需注意该服务会向客户端暴露浏览器内容并默认收集使用统计。

**关键词**: 浏览器自动化, 性能分析, 性能追踪, 浏览器调试, 网络请求分析, 截图采集, 源映射堆栈跟踪, ChromeDevTools

**评分**: 37

**项目地址**: [GitHub](https://github.com/ChromeDevTools/chrome-devtools-mcp)

---

## [10. letta-ai/letta-code](https://github.com/letta-ai/letta-code)

**语言**: TypeScript  
**Stars**: ⭐ 0 (+30 today) | **Forks**: 🔱 133

**原始描述**: The memory-first coding agent

**中文介绍（README总结）**: Letta Code是一个基于Letta API的“记忆优先”编码代理框架，提供跨会话持续学习的持久化代理，并可在多种模型之间迁移（如Claude、GPT、Gemini等）。面向希望在长期项目中拥有会学习、能记住上下文的开发者与团队。其关键技术包括持久化记忆体系、可插拔技能模块以及对多家LLM的兼容与切换。典型场景是在持续迭代的代码库中累积知识、跨模型或环境稳定协作，并通过引导代理记忆与技能提升代码生成与维护效率。

**关键词**: 代码代理, 长期记忆, 模型切换, 技能模块, letta-ai, letta-code, 描述与README, memory-first

**评分**: 61

**项目地址**: [GitHub](https://github.com/letta-ai/letta-code)

---

