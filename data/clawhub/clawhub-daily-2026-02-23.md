# ClawHub Skills Daily | 2026-02-23

> 共 8 个 skills

## [1. OpenTangl](https://clawhub.ai/8co/opentangl)

**Slug**: `opentangl`  
**Version**: 0.1.10  
**Stats**: ⭐ 1 | ⬇️ 38 | 🧩 11

**原始简介**: Not a code generator — an entire dev team. You write the vision, it ships the code. Autonomous builds, PRs, reviews, and merges across multiple repos. Point...

**中文介绍**: 这是一个“自动化开发团队”式的产品：你提供需求愿景，它能在多个代码仓库中自主完成构建、提交 PR、代码评审并合并交付。能力边界在于仍以你给出的目标、约束与验收标准为前提，适合端到端工程落地与持续迭代，但不等同于替你做产品决策或在缺少上下文时保证业务正确性。典型场景是跨仓库的功能开发、批量改动与发布流程自动化；关键技术形态是自治代理工作流编排叠加 PR/Review/Merge 管道，并结合向量检索增强可发现性（含可搜索标签与分类）与分步流程护栏来降低偏航。

**关键词**: 软件开发代理, 需求到代码, 自主构建, PR 自动化, 代码审查自动化, 多仓库编排, 持续集成自动化, 任务流程编排, 质量护栏, 标签检索

**评分**: 51

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/opentangl)

---

## [2. Potato Tipper](https://clawhub.ai/CJ42/potato-tipper)

**Slug**: `potato-tipper`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Work with the Potato Tipper Foundry smart-contract repo (CJ42/potato-tipper-contracts). Understand architecture and LUKSO/LSP integrations (LSP1, LSP7, LSP26...

**中文介绍**: 该能力聚焦于理解与分析 Potato Tipper Foundry 智能合约仓库的整体架构，并梳理其与 LUKSO 标准（如 LSP1、LSP7、LSP26 等）的集成方式，输出可用于理解、排障与二次创新的技术结论。能力边界在于以代码与文档解读、流程与权限模型分析为主，不涵盖环境安装与测试/部署命令层面的操作指导。典型场景包括快速上手项目结构与关键模块、定位集成与权限配置问题、以及在既有合约设计上扩展新功能或对接新应用；关键技术形态体现在基于 Foundry 的合约工程化组织、围绕权限与配置的工作流设计，以及按 LSP 标准进行接口/资产与账户交互的集成实现。

**关键词**: 智能合约, 合约架构, 权限管理, 打赏合约, Potato, Tipper, Work, Foundry

**评分**: 15

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/potato-tipper)

---

## [3. glm-understand-image](https://clawhub.ai/Thincher/glm-understand-image)

**Slug**: `glm-understand-image`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 45 | 🧩 5

**原始简介**: 使用 GLM 视觉 MCP 进行图像理解和分析。触发条件：(1) 用户要求分析图片、理解图像、描述图片内容 (2) 需要识别图片中的物体、文字、场景 (3) 使用 GLM 的视觉理解功能

**中文介绍**: GLM 视觉 MCP 用于在用户提出分析/理解图片或需要识别图中物体、文字、场景时，调用 GLM 的视觉理解能力输出描述与分析结果。能力边界是仅对输入图片内容做识别与推理，不负责自动发现或读取本地已保存的 API Key 等环境信息。关键技术形态为基于 MCP 的视觉调用链路，当前配置流程改为直接向用户索要智谱 API Key，并支持手动填写与保存。

**关键词**: 图像内容分析, 图像描述生成, 物体识别, 场景识别, OCR文字识别, 视觉推理, MCP工具集成, API密钥管理

**评分**: 7

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/glm-understand-image)

---

## [4. Dingtalk Ai Table](https://clawhub.ai/aliramw/dingtalk-ai-table)

**Slug**: `dingtalk-ai-table`  
**Version**: 0.2.4  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 6

**原始简介**: 钉钉 AI 表格（多维表）操作技能。使用 mcporter CLI 连接钉钉 MCP server 执行表格创建、数据表管理、字段操作、记录增删改查。使用场景：创建 AI 表格、管理数据表结构、批量导入导出数据、自动化库存/项目管理等表格操作任务。

**中文介绍**: 该技能通过 mcporter CLI 连接钉钉 MCP Server，实现钉钉 AI 表格（多维表）的创建与管理，覆盖数据表结构、字段与记录的增删改查等操作，能力边界在于以表格与数据管理为核心，不涉及业务流程审批等非表格能力。典型场景包括快速搭建 AI 表格、维护数据表结构、批量导入导出数据，以及自动化库存或项目管理等表格化任务。关键技术形态是基于 MCP Server 的接口能力，由 CLI 触发执行表格相关操作，并随官方入口调整同步更新配置获取路径。

**关键词**: 多维表, 表格自动化, 数据表结构管理, 字段管理, 批量导入导出, 钉钉集成, 库存管理自动化, 项目管理自动化

**评分**: 40

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/dingtalk-ai-table)

---

## [5. glm-web-search](https://clawhub.ai/Thincher/glm-web-search)

**Slug**: `glm-web-search`  
**Version**: 1.0.6  
**Stats**: ⭐ 0 | ⬇️ 94 | 🧩 7

**原始简介**: 使用 GLM 联网搜索 MCP 进行网络搜索。触发条件：(1) 用户要求进行网络搜索、在线搜索、查找信息 (2) 需要查询最新资讯、新闻、资料 (3) 使用 GLM 的 web_search 功能

**中文介绍**: 该能力通过 GLM 的 web_search 并结合 MCP 发起联网搜索，在用户明确要求在线查找信息或需要获取最新资讯、新闻与资料时触发。能力边界是仅负责检索与返回网络信息，不再自动从本地 auth-profiles.json 读取或推荐 API Key，而是需要用户手动输入；除这一点外其余配置与使用方式不变。典型场景包括实时新闻查询、最新资料/政策/产品动态检索与基于网页结果的快速信息汇总。关键技术形态为 MCP 连接的联网检索工具链调用（GLM web_search）。

**关键词**: 联网搜索, 网络信息检索, 搜索插件, 交互式鉴权, glm-web-search, 使用, GLM, MCP

**评分**: 3

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/glm-web-search)

---

## [6. App Store Deployment Guide](https://clawhub.ai/Skulick19/appstore-deployment-guide)

**Slug**: `appstore-deployment-guide`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: Complete guide to deploying iOS apps to the Apple App Store. Covers Apple Developer accounts (individual and organization), certificates, provisioning, App S...

**中文介绍**: 这是一个面向将 iOS 应用发布到 Apple App Store 的部署指南，核心覆盖 Apple Developer 个人/企业账号相关流程，以及证书与描述文件（Provisioning）等发布链路。能力边界在于侧重发布与签名配置的操作指导，不包含应用开发实现或第三方工具安装细节。典型场景是首次上架、证书/配置文件更新、组织账号发布准备与排错。关键技术形态围绕开发者账号体系、代码签名证书、Provisioning Profiles 与 App Store 提交流程；最新变更为修复 premium 链接。

**关键词**: Apple开发者账号, 个人开发者账号, 组织开发者账号, 代码签名, 证书管理, App, Store, Deployment

**评分**: 16

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/appstore-deployment-guide)

---

## [7. Omni Research](https://clawhub.ai/lmanchu/omni-research)

**Slug**: `omni-research`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Multi-source deep research using your own browser. Queries Perplexity, Grok, and Gemini in parallel via CDP — zero API keys, uses your existing subscriptions.

**中文介绍**: 这是一个基于自有浏览器的多源深度调研工具，通过 CDP 同时驱动 Perplexity、Grok、Gemini 并行检索与汇总，依赖你已有的账号订阅而无需 API Key。典型场景是快速对同一问题进行多模型交叉验证、对比观点与补全信息，用于技术调研、竞品分析、资料汇编等。能力边界在于必须能访问并登录相应服务，结果质量受网页可达性、订阅权限与站点反爬限制影响，且不承诺覆盖所有来源或提供离线数据。关键技术形态是浏览器自动化与并行编排，利用 Chrome DevTools Protocol 进行多标签/多会话控制与信息抽取整合。

**关键词**: 浏览器自动化, 深度研究助手, 多源信息整合, Omni, Research, Multi-source, deep, own

**评分**: 39

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/omni-research)

---

## [8. Polymarket Autopilot Experimental](https://clawhub.ai/mauonga/polymarket-autopilot-experimental)

**Slug**: `polymarket-autopilot-experimental`  
**Version**: 0.1.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Skill sperimentale per l’analisi automatica di mercati pubblici Polymarket con simulazione paper trading, controllo dei costi LLM e report in italiano con mi...

**中文介绍**: 这是一个面向 Polymarket 公共市场的实验性自动分析能力，支持基于市场数据做纸上交易（paper trading）模拟，并输出意大利语分析报告。能力边界在于偏研究与模拟验证，不直接保证真实交易收益或覆盖所有市场/数据异常情况，且会受 LLM 成本控制与调用稳定性约束。典型场景是对公开预测市场进行机会扫描、策略回测式验证与生成面向意大利语读者的摘要/报告，关键技术形态包括市场数据解析、LLM 驱动的分析与成本预算/限额控制、以及模拟交易与报表生成流程。另更新修复了 Windows 环境下发布/重试相关问题。

**关键词**: 预测市场分析, 自动化交易代理, 模拟交易, LLM 成本控制, 市场数据抓取, 交易策略回测, 自动化报告生成, 意大利语报告, 任务编排工作流

**评分**: 39

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/polymarket-autopilot-experimental)

---

