# ClawHub Skills Daily | 2026-02-16

> 共 6 个 skills

## [1. Human Pages](https://clawhub.ai/human-pages-ai/humanpages)

**Slug**: `humanpages`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Search and hire real humans for tasks — photography, delivery, research, and more

**中文介绍**: 该产品通过 AI 代理帮助用户搜索、雇佣并支付真实人类来完成线下任务，覆盖摄影、配送、调研等需要现实执行的工作。能力边界在于 AI 负责匹配、沟通与流程管理，但任务质量、时效与可用性取决于人力供给与线下履约条件。典型场景是临时外包本地执行、快速获取现场素材或跑腿取件等。关键技术形态是“AI 代理 + 人力任务市场 + 支付与订单履约跟踪”的一体化流程。

**关键词**: 人力众包, 真人任务市场, 线下任务, 任务派单, 劳务撮合, 人机协作, Agent, 服务交付, 支付结算

**评分**: 42

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/humanpages)

---

## [2. Audiomind](https://clawhub.ai/wells1137/audiomind)

**Slug**: `audiomind`  
**Version**: 2.1.3  
**Stats**: ⭐ 1 | ⬇️ 33 | 🧩 8

**原始简介**: One skill for all AI audio: TTS, music, SFX, and voice cloning. Routes your requests to 17+ models (ElevenLabs, fal.ai) via a single proxy. Free tier include...

**中文介绍**: 这是一个统一的 AI 音频能力代理层，通过单一接口将请求路由到 17+ 第三方模型（如 ElevenLabs、fal.ai），覆盖 TTS、音乐生成、音效生成与声音克隆等典型音频生成场景。能力边界在于实际生成质量、可用性与合规约束取决于所接入的外部模型与其策略，代理本身不保证内容安全、版权与隐私合规的最终结果。关键技术形态是“模型路由/聚合代理 + 外部端点管理”，并补充了安全与隐私、信任说明及安全清单以满足审计要求。

**关键词**: 音频生成, 文本转语音, 音乐生成, 音效生成, 语音克隆, 多模型路由, 统一代理API, 第三方模型集成, 模型聚合网关, 安全与隐私, 安全合规审核

**评分**: 32

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/audiomind)

---

## [3. Paradiz](https://clawhub.ai/keeper1978/paradiz)

**Slug**: `paradiz`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Отвечать клиентам в VK по стоимости отдыха на основе Excel-прайса. Использовать, когда нужно быстро посчитать цену по датам, количеству гостей и номеру, и вы...

**中文介绍**: 该系统能够根据Excel价格表快速计算客户在VK上的休闲费用，适用于需要根据日期、客人数和房间类型迅速得出价格的场景。关键技术形态包括数据处理和实时计算，确保高效响应客户询问。能力边界在于依赖于准确的Excel数据和预设的计算逻辑。

**关键词**: VK客服自动回复, 住宿报价计算, Excel价目表解析, 日期区间计价, 人数计价, 房型定价, 快速报价, 预订咨询自动化, 旅游住宿定价

**评分**: 28

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/paradiz)

---

## [4. 日本雅虎拍卖估价](https://clawhub.ai/skills?q=yahoo-auction-estimator)

**Slug**: `yahoo-auction-estimator`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: 日本雅虎拍卖商品估价工具 - 自动获取商品信息、查询历史成交价、计算建议出价

**中文介绍**: 该工具用于在日本雅虎拍卖场景下自动抓取商品信息并查询历史成交价，据此计算并给出建议出价，适合做竞拍前的快速估值与价格参考。能力边界在于估值强依赖历史数据与抓取到的商品描述质量，无法保证对稀缺品、信息缺失或价格波动剧烈品类的准确性。关键技术形态通常包括网页数据采集/解析、成交记录检索与特征抽取、基于规则或统计模型的估价与出价策略计算。最新变更为修复版本号并重新上传。

**关键词**: 雅虎拍卖日本, 商品估价, 拍卖定价, 历史成交价查询, 建议出价计算, 商品信息抓取, 网页爬虫, 拍卖数据分析, 竞拍辅助工具, 技能插件集成

**评分**: 62

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/yahoo-auction-estimator)

---

## [5. ClawSea NFT Marketplace](https://clawhub.ai/fluxmira-moltbot/clawsea-market)

**Slug**: `clawsea-market`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 236 | 🧩 3

**原始简介**: Non-custodial automation skill for ClawSea NFT marketplace. Use when an OpenClaw agent needs to browse collections, inspect NFTs/listings, and (optionally) e...

**中文介绍**: 这是一个面向 ClawSea NFT 市场的非托管自动化能力，主要用于 OpenClaw 代理浏览合集、查看 NFT 与上架信息，并可在需要时扩展到挂单/购买/取消等交易流程。能力边界上，纯浏览不需要任何密钥或签名信息；只有在执行自主交易时才需要提供签名凭证且凭证配置按需可选。典型场景包括批量检索与筛选标的、核对单品详情与价格深度、以及在满足风控前提下触发交易操作。关键技术形态是代理驱动的市场数据抓取与解析结合可选的链上/账户签名交易编排，并加强了对凭证使用时机与安全指引的约束。

**关键词**: 非托管交易, 自动化交易, NFT合集浏览, NFT挂单检索, 订单取消, 交易签名凭证, ClawSea, NFT

**评分**: 39

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/clawsea-market)

---

## [6. Memoria Memory System](https://clawhub.ai/cuilinshen/memoria-system)

**Slug**: `memoria-system`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Manages AI assistant long-term memory with layered storage for facts, events, skills, context, and fast indexing, including backup and integrity tools.

**中文介绍**: Memoria记忆系统是一种基于认知科学的多层长期记忆管理方案，旨在为AI助手提供类似人类的记忆架构，涵盖语义记忆、情景记忆、程序记忆和工作记忆等多种类型，支持快速检索和关联。该系统适用于需要长期记忆管理的场景，如个性化助手、智能客服和决策支持系统，关键技术包括分层存储、备份与完整性工具以及自动化任务调度。

**关键词**: AI助手长期记忆, 认知架构记忆模型, 语义记忆, 情景记忆, 程序记忆, 工作记忆, 分层存储, 记忆索引检索, 记忆备份, 数据迁移回滚, 健康检查

**评分**: 44

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/memoria-system)

---

