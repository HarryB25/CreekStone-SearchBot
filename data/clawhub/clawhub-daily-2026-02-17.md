# ClawHub Skills Daily | 2026-02-17

> 共 5 个 skills

## [1. Intelligence Ingestion](https://clawhub.ai/sarahmirrand001-oss/intelligence-ingestion)

**Slug**: `intelligence-ingestion`  
**Version**: 2.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Analyze and evaluate URLs, links, articles, tweets, and external info sources for strategic value. NOT a summarizer — this skill classifies, scores importanc...

**中文介绍**: 该能力用于对 URL/文章/推文等外部信息源进行分类与战略价值评估与打分，侧重“重要性与影响判断”而非单纯摘要，边界在于仅输出分析与结构化沉淀，不替代最终决策且对自动生成的新技能仅提供草案需人工审核。典型场景包括情报监测与竞争/市场动态研判、将零散信息沉淀为可追溯的知识资产、以及在 Obsidian 中形成带评分与能力边界的结构化笔记并持续更新战略能力地图。关键技术形态是 8 步零损摄取管线（读入→分类→分析→映射→存储→综合→记忆→响应）、自动技能合成草案机制、MCP/manifest.json 生态发现与透明权限/网络/隐私声明。

**关键词**: 信息摄取管线, 零损耗摄取, 内容分类, 重要性评分, 战略情报分析, 能力地图, 自动技能生成, 权限与隐私声明

**评分**: 52

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/intelligence-ingestion)

---

## [2. llm-eval-router](https://clawhub.ai/nissan/llm-eval-router)

**Slug**: `llm-eval-router`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Shadow-test local Ollama models against a cloud baseline with a multi-judge ensemble. Automatically promotes models when statistically proven equivalent — re...

**中文介绍**: 该工具用于将本地 Ollama 模型与云端基线进行影子测试，通过多评审（multi-judge）集成对输出进行对比打分，并在统计上证明等效时自动提升/替换模型版本。能力边界在于它主要评估生成质量的一致性与回归风险，结论依赖评审集合与统计检验设定，无法替代面向安全、合规或真实业务指标的端到端验证。典型场景包括本地模型迭代、量化/微调后回归检测，以及上线前与云模型对齐的自动化门禁。关键技术形态是“影子流量对照 + 多裁判集成评估 + 统计显著性判定 + 自动晋级流水线”。

**关键词**: LLM评测路由, 影子测试, 本地模型评测, 云基线对比, 多裁判集成, 统计等效性检验, 自动模型晋升, 模型回归测试

**评分**: 49

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/llm-eval-router)

---

## [3. realtime-interact-overlay](https://clawhub.ai/LightCastlePro/realtime-interact-overlay)

**Slug**: `realtime-interact-overlay`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 实时交互浮窗技能。在需要用户确认、输入或交互的场景中，通过浮窗方式在当前操作界面旁边进行交互， 而不是回到OpenClaw聊天窗口。适用于：(1) 评论内容需要用户确认后执行，(2) 删除文件前需要用户确认， (3) 购物付款时需要输入密码，(4) 任何需要即时交互的场景。支持系统级浮窗和浏览器内浮窗。

**中文介绍**: 该能力通过系统级或浏览器内浮窗在当前操作界面旁边完成确认、输入与交互，无需切回 OpenClaw 聊天窗口。典型场景包括发布评论前确认、删除文件二次确认、购物付款密码输入等所有需要即时用户介入的流程。能力边界在于仅承载交互与确认链路，不负责业务执行结果本身且依赖宿主环境对浮窗与权限的支持。关键技术形态为实时交互式浮窗组件与事件回传机制，分别覆盖系统级悬浮窗与网页内嵌浮层两种实现。

**关键词**: 实时交互, 浮窗交互, 系统级浮窗, 浏览器内浮窗, 上下文内交互, 安全输入, 密码输入, 操作前确认, 人机协同

**评分**: 42

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/realtime-interact-overlay)

---

## [4. Creative Toolkit](https://clawhub.ai/jau123/creative-toolkit)

**Slug**: `creative-toolkit`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 205 | 🧩 5

**原始简介**: Generate images from text with multi-provider routing — supports Nanobanana Pro, GPT Image, Seedream, and local ComfyUI workflows. Includes 1,300+ curated pr...

**中文介绍**: 该产品支持将文本生成图像，并可在多个提供方之间进行路由调度，覆盖 Nanobanana Pro、GPT Image、Seedream 以及本地 ComfyUI 工作流。能力边界在于其核心聚焦于“生成与编排/检索”，不直接保证特定模型的画质风格一致性或可用性，效果与成本受所选提供方与本地算力约束。典型场景包括多模型比对出图、按成本/时延自动选路、以及对生成结果图库进行语义级检索与复用。关键技术形态是多提供方适配与路由层、与 ComfyUI 的工作流集成，以及基于向量+关键词混合检索的语义搜索（用于 search_gallery）。

**关键词**: 文本生成图像, 多模型路由, 多后端集成, 本地推理, 提示词库, 图像画廊, 语义检索, 混合检索, 关键词检索

**评分**: 40

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/creative-toolkit)

---

## [5. Ticket Monitor Ichinosuke](https://clawhub.ai/texka001/ticket-monitor-ichinosuke)

**Slug**: `ticket-monitor-ichinosuke`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Monitors 春風亭一之輔's official site for new Tokyo performance tickets and sends notifications to a specified Discord webhook.

**中文介绍**: 该能力用于持续监测春風亭一之輔官网上东京场次门票是否上新，一旦发现新增票务信息会通过指定的 Discord Webhook 推送通知。能力边界在于仅覆盖官网公开的票务更新与通知转发，不涉及代购下单、登录鉴权、验证码处理或保证抢票成功等行为。典型场景是粉丝或运营人员需要第一时间获知新场次/开票信息并同步到社群频道。关键技术形态为网页内容监控/轮询比对与事件触发式通知推送（Webhook 集成）。

**关键词**: 票务监控, 演出门票提醒, 官网监测, 网页爬虫, 变更检测, 定时轮询, 通知推送, 东京演出

**评分**: 5

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ticket-monitor-ichinosuke)

---

