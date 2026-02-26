# ClawHub Skills Daily | 2026-02-24

> 共 6 个 skills

## [1. Auto Memory](https://clawhub.ai/jim-counter/auto-memory)

**Slug**: `auto-memory`  
**Version**: 0.1.0-beta.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Upload and download files to permanent decentralized storage on the Autonomys Network via Auto Drive. Save memories as a linked-list chain for resurrection —...

**中文介绍**: 该能力提供在 Autonomys Network 上通过 Auto Drive 上传/下载文件并以 CID 作为永久引用，同时将代理记忆以链上不可变的链表结构持续追加存储，实现从单个 CID 恢复完整上下文与“复活”。能力边界在于写入与检索依赖 AUTO_DRIVE_API_KEY 的鉴权调用，记忆模型限定为追加式不可变链且以 CID 驱动更新与回溯。典型场景包括为智能体持久化长期记忆、跨会话迁移/恢复状态，以及对关键文件与记忆快照进行去中心化永久归档与引用。关键技术形态是基于 CID 的内容寻址存储 + 链上 linked-list 记忆链（支持 JSON 封装与压缩）并兼容新旧记忆格式。

**关键词**: 去中心化永久存储, 内容寻址（CID）, 链上不可变存储, 代理记忆存储, 记忆链（链表）, 上下文恢复, 命令行工具（CLI）, 数据压缩

**评分**: 47

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/auto-memory)

---

## [2. OpenClaw Arena](https://clawhub.ai/billychl1/openclawarena-arena)

**Slug**: `openclawarena-arena`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Register and manage AI Lobster Agents in OpenClaw Arena — create agents, join matchmaking, check leaderboards, and view match results.

**中文介绍**: 该能力用于在 OpenClaw Arena 中注册与管理 AI Lobster Agent，支持创建/注册代理、加入匹配队列、查询排行榜与历史战绩并查看对局结果。能力边界主要在“赛事与数据管理层”，通过 REST API 与 OCBP 协议对接竞技场，不覆盖代理内部策略训练或客户端运行环境。典型场景包括自动化报名参赛、批量调度代理打天梯、赛后复盘与社区讨论互动。关键技术形态为一组 REST API 端点配合完整 OCBP 协议文档，并提供 Node.js 代理示例及物理规则与策略指南以辅助实现对局行为。

**关键词**: AI 代理竞技场, 多智能体对战, 排行榜系统, 代理注册管理, 协议规范, 游戏物理模拟, OpenClaw, Arena

**评分**: 37

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/openclawarena-arena)

---

## [3. Onebot Adapter 1.0.0](https://clawhub.ai/haohaodlam/onebot-adapter-1-0-0)

**Slug**: `onebot-adapter-1-0-0`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Connect OpenClaw to OneBot protocol for QQ bot integration. Use when receiving or sending QQ messages via NapCat or other OneBot servers.

**中文介绍**: 该 onebot-adapter 用于将 OpenClaw 接入 OneBot 协议服务器（如 NapCat），实现 QQ 私聊与群聊消息的收发联动，适合需要基于 OneBot 生态快速打通 QQ 机器人的场景。能力边界在于仅覆盖 OneBot 协议层的连接与消息收发，不包含账号登录、风控绕过或平台侧能力扩展。关键技术形态为 WebSocket（推荐）与 HTTP 两种连接模式，并提供相应脚本与 API 以对接消息事件和发送接口。

**关键词**: QQ 机器人, 适配器, 消息收发, 群聊消息, 私聊消息, Onebot, Adapter, Connect

**评分**: 24

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/onebot-adapter-1-0-0)

---

## [4. Flux](https://clawhub.ai/EckmanTechLLC/flux)

**Slug**: `flux`  
**Version**: 2.0.0  
**Stats**: ⭐ 1 | ⬇️ 332 | 🧩 4

**原始简介**: Publish events and query shared world state via Flux state engine. Use when agents need to share observations, coordinate on shared data, or track entity sta...

**中文介绍**: 该能力通过 Flux 状态引擎发布事件并查询共享世界状态，用于多智能体在同一命名空间内共享观测、基于共享数据协同决策、以及持续跟踪实体状态变化等场景。能力边界在于它主要提供状态存取与一致性保障的协作底座，不负责具体业务推理、任务编排或外部行动执行。关键技术形态为事件发布/订阅与状态查询接口相结合，依托公共 Flux 实例的鉴权与命名空间隔离，并对一致性机制与文档进行了更新完善。

**关键词**: 事件发布, 事件驱动架构, 状态引擎, 共享世界状态, 多智能体协作, 状态同步, 观察共享, 实体跟踪, 状态查询API, 最终一致性, 命名空间隔离, 身份认证

**评分**: 43

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/flux)

---

## [5. Stable Browser](https://clawhub.ai/jarvis563/stable-browser)

**Slug**: `stable-browser`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Set up reliable browser automation using Chrome DevTools Protocol (CDP) instead of the flaky browser extension relay. Use when browser relay keeps disconnect...

**中文介绍**: 该能力通过直接使用 Chrome DevTools Protocol（CDP）建立浏览器自动化连接，替代易断连的浏览器扩展中继，边界在于需要可控的 Chrome 环境与可用的 CDP 接口而非完全无依赖的远程浏览器服务。典型场景是扩展中继频繁断开、WebSocket/端口不稳定时的自动化迁移与稳定运行，覆盖抓取、表单填写以及无头/有头模式的流程执行。关键技术形态是基于专用 Chrome Profile 的直连 CDP 自动化通道，并配套迁移与排障以降低连接与会话稳定性问题。

**关键词**: 浏览器自动化, 稳定性, 无头模式, 数据抓取, 表单填写, 迁移指导, Stable, Browser

**评分**: 40

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/stable-browser)

---

## [6. Kraken Exchange](https://clawhub.ai/askbeka/tentactl)

**Slug**: `tentactl`  
**Version**: 0.3.1  
**Stats**: ⭐ 0 | ⬇️ 26 | 🧩 7

**原始简介**: Interact with the Kraken cryptocurrency exchange — spot + futures, REST + WebSocket. Use when: (1) checking crypto prices or market data, (2) viewing account...

**中文介绍**: 该能力用于与 Kraken 加密货币交易所交互，覆盖现货与期货市场，并通过 REST 与 WebSocket 提供行情与账户相关数据的查询与订阅。典型场景包括获取实时/历史价格与市场数据、查看账户资产与持仓、跟踪订单与成交等。能力边界在于仅能操作 Kraken 交易所范围内的功能，实际下单/风控等受账户权限、API 限额与交易所规则约束，且对链上转账等非交易所接口不直接覆盖。关键技术形态是以 REST 进行请求-响应式查询与管理，以 WebSocket 进行低延迟行情/事件流推送。

**关键词**: 加密货币交易所API, 现货交易, 期货交易, 实时行情数据, 市场数据查询, 账户资产查询, 交易下单, 实时数据流

**评分**: 18

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tentactl)

---

