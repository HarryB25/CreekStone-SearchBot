# ClawHub Skills Daily | 2026-02-28

> 共 25 个 skills

## [1. 腾讯云COS存储](https://clawhub.ai/ShawnMinh/tencent-cloud-cos)

**Slug**: `tencent-cloud-cos`  
**Version**: 1.0.3  
**Stats**: ⭐ 0 | ⬇️ 1084 | 🧩 2

**原始简介**: 腾讯云对象存储(COS)和数据万象(CI)集成技能。当用户需要上传、下载、管理云存储文件， 或需要进行图片处理（质量评估、超分辨率、抠图、二维码识别、水印）、智能图片搜索、 文档转PDF、视频智能封面生成等操作时使用此技能。

**中文介绍**: 该技能集成腾讯云对象存储 COS 与数据万象 CI，提供云端文件的上传/下载/管理能力，并支持对存储内媒体与文档进行处理，如图片质量评估、超分辨率、抠图、二维码识别与水印、智能图片搜索、文档转 PDF、视频智能封面生成等典型场景。能力边界在于仅覆盖已明确文档化的存储与媒体处理任务，依赖用户正确配置腾讯云相关鉴权与资源信息，不承诺对未收录能力或本地环境缺失工具的功能可用。关键技术形态采用统一执行策略并按可用性回退：优先 cos-mcp，其次 Node.js SDK，最后 coscmd CLI，以保证在不同运行环境下尽可能完成同一类操作。

**关键词**: 云存储文件管理, 数据万象 CI, 图片处理, 超分辨率, 二维码识别, 智能图片搜索, 腾讯云COS存储, 腾讯云对象存储

**评分**: 36

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tencent-cloud-cos)

---

## [2. Reddit 主题洞察](https://clawhub.ai/Wbule/reddit-topic-insight)

**Slug**: `reddit-topic-insight`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 输入研究主题，自动采集 Reddit 讨论，提炼爆款角度，产出 X 推文、小红书笔记、公众号文章三平台成品。7 步流水线：需求收集 → 关键词设计 → 数据采集 → 详情获取 → 角度规划 → 成品生产 → 合并输出。

**中文介绍**: 该系统以研究主题为输入，自动从 Reddit 采集讨论并提炼“爆款角度”，最终生成适配 X、小红书、公众号的成品内容并合并输出，适用于选题洞察与多平台内容批量生产。能力边界在于数据主要来自 Reddit 且质量受关键词与帖子可获取性影响，输出更偏角度与文案生成而非事实核验或深度行业研究。关键技术形态是 7 步流水线编排（需求→关键词→采集→详情→角度→生成→合并）、断点恢复机制，以及 AI SubAgent 负责创意生成、Python 脚本负责数据采集与处理的分工架构。

**关键词**: 话题洞察, 选题角度提炼, 关键词设计, 多平台内容生成, 社交媒体文案生成, 自动化流水线, 工作流编排, 断点续跑

**评分**: 45

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/reddit-topic-insight)

---

## [3. Tencent Cloud COS](https://clawhub.ai/ShawnMinh/tencent-cloud-cos-skill)

**Slug**: `tencent-cloud-cos-skill`  
**Version**: 1.0.3  
**Stats**: ⭐ 0 | ⬇️ 1074 | 🧩 2

**原始简介**: 腾讯云对象存储(COS)和数据万象(CI)集成技能。当用户需要上传、下载、管理云存储文件， 或需要进行图片处理（质量评估、超分辨率、抠图、二维码识别、水印）、智能图片搜索、 文档转PDF、视频智能封面生成等操作时使用此技能。

**中文介绍**: 该技能集成腾讯云对象存储 COS 与数据万象 CI，能力边界在于云端文件的上传下载与管理，以及围绕图片/文档/视频的标准化处理与识别（如质量评估、超分辨率、抠图、二维码识别、水印、智能图片搜索、文档转 PDF、视频封面生成等）。典型场景是应用或工作流需要对存储中的媒体与文档进行批量处理、内容检索与自动化加工时调用。关键技术形态上，v1.0.3 进行了架构重构，提供 cos-mcp 工具、Node.js SDK 脚本与 coscmd CLI 三种执行后端并带内置回退机制，以提升多环境适配与维护性。

**关键词**: 云存储文件管理, 多后端执行, 故障回退, 命令行工具, 图片处理, 智能图片搜索, 文档转 PDF, 视频封面生成, 二维码识别

**评分**: 32

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tencent-cloud-cos-skill)

---

## [4. Tencent COS](https://clawhub.ai/ShawnMinh/tencent-cos-skill)

**Slug**: `tencent-cos-skill`  
**Version**: 1.0.3  
**Stats**: ⭐ 2 | ⬇️ 1580 | 🧩 4

**原始简介**: 腾讯云对象存储(COS)和数据万象(CI)集成技能。当用户需要上传、下载、管理云存储文件， 或需要进行图片处理（质量评估、超分辨率、抠图、二维码识别、水印）、智能图片搜索、 文档转PDF、视频智能封面生成等操作时使用此技能。

**中文介绍**: 该技能集成腾讯云 COS 与 CI，用于云端文件的上传下载与目录管理，以及图片处理（质检、超分、抠图、二维码、水印等）、智能图像搜索、文档转 PDF、视频智能封面生成等多媒体增值能力。能力边界在于仅覆盖 COS/CI 官方接口与工具链支持的对象存储与数据处理操作，不提供业务侧内容生产、人工审核或超出服务权限范围的处理。关键技术形态上执行会在三种官方方式间自动探测与切换（优先级与回退机制）：cos-mcp MCP、Node.js SDK 脚本、coscmd CLI，并统一了配置与参考资源以简化集成与维护。

**关键词**: 云存储文件管理, 数据万象, 图像处理, 智能图片搜索, 视频封面生成, 二维码识别, 水印添加, 命令行工具

**评分**: 34

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tencent-cos-skill)

---

## [5. Veadk Go Skills](https://clawhub.ai/helloldm/veadk-go-skills)

**Slug**: `veadk-go-skills`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 根据用户的功能需求，完成与 VeADK-Go 相关的功能; 包括：直接根据需求生成 Agent；将Enio Agent转换为VeADK-Go Agent。

**中文介绍**: VeADK-Go 技能集合可根据用户功能需求自动生成符合 VeADK-Go 规范的 Agent 代码，并支持将现有 Enio Agent 代码转换为 VeADK-Go Agent。能力边界在于聚焦于代码生成与转换及产物命名规范（标准输出为 agent_name/agent.py），不覆盖运行部署与业务效果验证等全流程。典型场景包括从需求快速搭建新 Agent、以及对存量 Enio Agent 进行框架迁移与规范化改造，关键技术形态是基于参考文档约束的代码生成/代码转换流水线与标准化工程结构输出。

**关键词**: Agent 代码生成, 需求驱动开发, Agent 代码转换, Go 生态工具链, 代码脚手架, 标准化代码产物, 命名规范, 开发文档引导

**评分**: 34

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/veadk-go-skills)

---

## [6. 数联互通weather](https://clawhub.ai/jianmo1997/shulian-weather)

**Slug**: `shulian-weather`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Get current weather and forecasts via WeatherAPI.com. Use when: user asks about weather, temperature, or forecasts for any location. IMPORTANT: You must conf...

**中文介绍**: 该技能基于 WeatherAPI.com 提供全球任意地点的实时天气与预报查询，适用于用户询问天气、气温或未来几天走势等场景。能力边界在于只覆盖天气相关信息且依赖第三方接口返回结果，使用前需用户自备并配置 WeatherAPI Key。关键技术形态为通过 API 拉取数据并在运行环境中以环境变量或配置方式注入密钥完成鉴权与调用。

**关键词**: 天气查询, 天气预报, 气温查询, 全球地点天气, 第三方天气API, API密钥配置, 环境变量配置, 命令行依赖curl, 技能插件（Skill）

**评分**: 2

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/shulian-weather)

---

## [7. Tencent Cloud COS](https://clawhub.ai/ShawnMinh/tencentcloud-cos-skill)

**Slug**: `tencentcloud-cos-skill`  
**Version**: 1.0.3  
**Stats**: ⭐ 0 | ⬇️ 1066 | 🧩 3

**原始简介**: 腾讯云对象存储(COS)和数据万象(CI)集成技能。当用户需要上传、下载、管理云存储文件， 或需要进行图片处理（质量评估、超分辨率、抠图、二维码识别、水印）、智能图片搜索、 文档转PDF、视频智能封面生成等操作时使用此技能。

**中文介绍**: 该技能用于集成腾讯云对象存储（COS）与数据万象（CI），提供云端文件的上传、下载与管理，并支持图片处理（质量评估、超分辨率、抠图、二维码识别、水印）、智能图片搜索、文档转 PDF、视频智能封面生成等能力。能力边界在于仅覆盖 COS/CI 提供的存储与媒体处理接口与其可支持的数据类型，涉及复杂业务流程编排或超出服务能力范围的自定义算法不在内。典型场景是将文件统一存储到云端并按需触发图片/文档/视频的标准化处理与检索。关键技术形态上提供一致的执行框架与回退策略，优先通过 MCP 工具（cos-mcp）调用，其次可回退到 Node.js SDK 脚本或 COSCMD CLI 以确保兼容性与可用性。

**关键词**: 云存储文件管理, 容错回退机制, 图像质量评估, 图像超分辨率, 图像抠图, 二维码识别, 文档转 PDF, 视频封面生成

**评分**: 38

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tencentcloud-cos-skill)

---

## [8. Auto Doc Index](https://clawhub.ai/ERerGB/auto-doc-index)

**Slug**: `auto-doc-index`  
**Version**: 1.2.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: Auto-generate document index tables (ADR, RFC, Pitfall, etc.) from file frontmatter. In real-world testing, hand-maintained indexes had a 62% error rate — ti...

**中文介绍**: 该工具从文档文件的 frontmatter 自动生成 ADR、RFC、Pitfall 等索引表，避免手工维护索引在真实测试中出现的高错误率（约 62%）。能力边界在于依赖 frontmatter 的完整性与一致性，主要覆盖索引汇总与格式转换，不替代内容编写或质量评审。典型场景是多类型工程文档库的目录/索引自动化维护与同步更新，尤其适合协作频繁、文档数量增长快的仓库。关键技术形态包括基于元数据解析的索引生成、面向多代理/多编辑器生态（Cursor MDC、Windsurf、GitHub Copilot）的格式翻译，以及内置“何时使用”触发器与边界约束校验（SkillKit 验证 Grade B，88/100）。

**关键词**: 文档索引生成, 文档元数据管理, 文档治理自动化, 索引一致性校验, 多 Agent 格式转换, Auto, Doc, Index

**评分**: 39

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/auto-doc-index)

---

## [9. notion-agent-memory](https://clawhub.ai/vladchatware/notion-agent-memory)

**Slug**: `notion-agent-memory`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 209 | 🧩 6

**原始简介**: Structured memory system for AI agents using Notion. Use when setting up agent memory, discussing memory persistence, or helping agents remember context acro...

**中文介绍**: 这是一个基于 Notion 的结构化记忆系统，用于为 AI Agent 提供可持久化的上下文存取与检索能力，适合在搭建 Agent 记忆层、讨论长期记忆/短期记忆策略、让 Agent 跨会话“记住”关键信息时使用。能力边界在于记忆的写入与读取依赖 Notion 数据库与其 API 的可用性与权限配置，并不提供模型侧推理增强本身，只负责外部记忆的组织与访问。关键技术形态是通过 Notion API 以脚本方式进行读写与查询，示例改为仅使用 shell 调用，并从 JSON 文件读取访问 token。

**关键词**: 结构化记忆, 记忆持久化, 上下文管理, 外部记忆存储, 知识库同步, JSON 凭证管理, notion-agent-memory, Structured

**评分**: 31

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/notion-agent-memory)

---

## [10. Password Generator](https://clawhub.ai/Yukin1218/password-generator)

**Slug**: `password-generator`  
**Version**: 1.1.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: 生成随机安全密码。长度12-16位随机(默认)，包含大小写字母、数字、符号。当用户要求生成密码、创建密码、随机密码时使用此技能。

**中文介绍**: 该能力用于在用户提出“生成密码/创建密码/随机密码”等需求时生成安全随机密码，默认长度为12–16位并包含大小写字母、数字与符号。能力边界是仅负责生成并输出随机字符串，不涉及保存、找回、校验强度策略定制或与账号系统的绑定。典型场景包括注册、重置密码、为新服务创建高强度密码等。关键技术形态为密码学安全随机数生成与字符集组合策略，并在最近升级中将默认长度调整为12–16位随机。

**关键词**: 密码生成器, 随机密码, 安全密码, 密码长度策略, 12-16位长度, 字符集组合, 大小写字母, 数字字符, 特殊符号

**评分**: 9

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/password-generator)

---

## [11. Tencent Cloud COS](https://clawhub.ai/ShawnMinh/tencentcloud-cos-skills)

**Slug**: `tencentcloud-cos-skills`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 915 | 🧩 2

**原始简介**: 腾讯云对象存储(COS)和数据万象(CI)集成技能。当用户需要上传、下载、管理云存储文件， 或需要进行图片处理（质量评估、超分辨率、抠图、二维码识别、水印）、智能图片搜索、 文档转PDF、视频智能封面生成等操作时使用此技能。

**中文介绍**: 该技能集成腾讯云 COS 与数据万象 CI，提供云存储文件的上传、下载与管理，以及面向图片/文档/视频的处理与分析能力，包括图片质量评估、超分辨率、抠图、二维码识别、水印、智能图片搜索、文档转 PDF、视频智能封面生成等典型场景。能力边界在于仅覆盖 COS/CI 提供的对象存储与媒体处理接口，不包含业务侧内容生产与自定义算法训练。关键技术形态采用三层降级执行链路：优先通过 cos-mcp，其次使用 Node.js SDK 脚本，最后回退到 COSCMD，以保证在不同运行环境下的可用性与一致的能力映射。

**关键词**: 云存储文件管理, 数据万象 CI, 图片处理, 图像质量评估, 超分辨率, 二维码识别, 水印处理, Tencent

**评分**: 23

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tencentcloud-cos-skills)

---

## [12. Money Idea Generator](https://clawhub.ai/devotion-coding/openclaw-skill-money-idea-generator)

**Slug**: `openclaw-skill-money-idea-generator`  
**Version**: 0.1.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: 赚钱灵感生成器 | Money Idea Generator. 自动发现 AI 变现机会，生成可落地的赚钱灵感。触发词：赚钱灵感、赚钱机会、AI 变现、商业灵感.

**中文介绍**: 这是一个用于自动发现 AI 变现机会并生成可落地赚钱灵感的工具，面向“赚钱灵感/赚钱机会/AI 变现/商业灵感”等触发词进行内容生成与整理。典型场景包括个人或团队做商业方向头脑风暴、评估可尝试的副业/产品化机会、快速产出可执行的变现点子。能力边界在于主要提供创意与方向建议，不直接保证收益、也不替代市场调研与实际运营验证；关键技术形态以基于提示词触发的文本生成与灵感结构化输出为主。

**关键词**: 赚钱灵感生成, AI变现, 商业灵感, 创业点子生成, 副业创意, 创意生成器, 自动化创意, Money

**评分**: 10

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/openclaw-skill-money-idea-generator)

---

## [13. Self-improving Agent Memory Upgrade (SurrealDB)](https://clawhub.ai/maverick-software/surrealdb-knowledge-graph-memory)

**Slug**: `surrealdb-knowledge-graph-memory`  
**Version**: 2.2.3  
**Stats**: ⭐ 0 | ⬇️ 960 | 🧩 10

**原始简介**: A comprehensive knowledge graph memory system with semantic search, episodic memory, working memory, automatic context injection, and per-agent isolation.

**中文介绍**: 这是一个面向多智能体的知识图谱记忆系统，提供语义检索、情节记忆与工作记忆，并支持自动上下文注入与按 Agent 隔离的数据边界。典型场景是在对话/任务执行中持续沉淀事实与经历、快速召回相关信息，同时避免不同 Agent 之间的记忆串扰。其关键技术形态包括基于向量相似度的去重与基于置信度和时效性的图谱清理机制，并通过定时作业实现每日近重复事实去重与每周陈旧低置信事实修剪、孤立实体清理及重复实体合并，以维持图谱健康。

**关键词**: 智能体记忆系统, 知识图谱记忆, 语义搜索, 事实去重, 低置信度事实清理, 陈旧知识修剪, 实体去孤儿, 情景记忆, 工作记忆, 自动上下文注入

**评分**: 48

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/surrealdb-knowledge-graph-memory)

---

## [14. smartsheet-write](https://clawhub.ai/Roollond/smartsheet-write)

**Slug**: `smartsheet-write`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 当用户请求写入数据（添加新记录或更新已有记录）时，可以使用本技能向企业微信智能表格写入数据。本技能**强制先检查并主动向用户索要** Webhook 地址和该工作表的「示例数据」schema（若缺少则立即询问并保存），之后根据 schema 精确构建 JSON payload。内置 8 个复杂度递增的完整示例、日...

**中文介绍**: 该技能用于在用户需要新增或更新记录时，通过企业微信智能表格的 Webhook 写入数据，但能力边界是必须先获取并保存完整 Webhook 地址与该表「示例数据」schema，否则会立即向用户追问并在确认后才执行写入。典型场景包括按业务表单/工单/客户信息等结构化字段进行批量或单条新增、按条件更新，以及处理日期换算、成员/用户字段、附件等复杂字段。关键技术形态是基于 schema 的严格字段类型与取值映射规则来精确构建 JSON payload，配合配置校验、用户确认、按会话持久化关键信息与写入安全/限额提醒，并提供逐级复杂的完整示例覆盖常见写入与更新模式。

**关键词**: 企业微信智能表格, 数据写入, 记录更新, 字段类型映射, 交互式配置收集, 写入安全校验, smartsheet-write, 当用户请求写入数据（添加新记录或更新已有记录）时

**评分**: 36

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/smartsheet-write)

---

## [15. Audio Editor](https://clawhub.ai/jwl1992/audio-editor)

**Slug**: `audio-editor`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Perform audio editing tasks including trimming, volume adjustment, format conversion, and extracting audio from video files using natural language commands.

**中文介绍**: 该能力支持通过自然语言对音频进行剪辑、音量调整与格式转换，并可从视频文件中提取音频，适用于快速处理素材、生成不同发布规格或提取配音/背景声等场景。能力边界在于聚焦基础编辑与抽取，不涵盖复杂多轨混音、降噪修复或母带级处理。关键技术形态为以 edit_audio、extract_audio 等命令封装音频处理流程，底层依赖 ffmpeg（>=5.0）执行编解码与裁剪等操作。

**关键词**: 音频编辑, 自然语言指令, 命令行工具, 音频剪辑, 音量调整, 音频格式转换, 视频提取音频, 自动化音频处理, 技能插件集成

**评分**: 14

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/audio-editor)

---

## [16. Search Cluster](https://clawhub.ai/1999AZZAR/search-cluster)

**Slug**: `search-cluster`  
**Version**: 2.4.0  
**Stats**: ⭐ 0 | ⬇️ 492 | 🧩 11

**原始简介**: Professional aggregated search tool. Integrates Google CSE, GNews RSS, and Scrapling stealth engine. Requires GOOGLE_API_KEY and GOOGLE_CSE_ID for official s...

**中文介绍**: 这是一个聚合式专业搜索工具，整合了 Google 自定义搜索（CSE）、Google 新闻 RSS 与 Scrapling 隐身抓取引擎，用于把多来源的网页与新闻结果统一检索与汇总。能力边界在于对官方搜索能力依赖较强，使用 CSE 相关功能需要提供 GOOGLE_API_KEY 与 GOOGLE_CSE_ID，抓取侧也会受目标站点反爬与合规限制影响。典型场景包括舆情/新闻监测、竞品与行业信息收集、研究与资料检索等。关键技术形态是多源检索聚合 + RSS 拉取 + 隐身网页抓取的组合，最近更新仅为内部脚本改进，无明显用户可见变化。

**关键词**: 多源搜索聚合, 元搜索, 网页爬虫, 反爬虫, API 密钥配置, Search, Cluster, Professional

**评分**: 26

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/search-cluster)

---

## [17. ShieldCortex](https://clawhub.ai/jarvis-drakon/shieldcortex)

**Slug**: `shieldcortex`  
**Version**: 2.17.0  
**Stats**: ⭐ 0 | ⬇️ 341 | 🧩 6

**原始简介**: Security framework for AI agents. Enforces instruction gateway control, external action gating, PII protection, sub-agent sandboxing, prompt injection detect...

**中文介绍**: ShieldCortex 是面向 AI Agent 的安全框架，通过指令入口网关、外部动作门控、PII 保护与子代理沙箱等机制降低提示注入与越权调用风险，但它主要提供防护与审计能力，不替代业务侧权限体系、模型能力本身或对所有未知攻击的绝对拦截。典型场景包括多工具调用的智能体、需要合规处理敏感信息的对话/流程自动化，以及存在多子代理协作的任务编排。其关键技术形态是以行为为核心的“动作闸门+安全档案+审计追踪”（Iron Dome）、可适配任意记忆后端的通用防护管线桥接（Universal Memory Bridge），并结合语义分析、结构校验与行为/异常评分形成多层检测与拦截。

**关键词**: 指令网关控制, 外部动作门控, 提示注入检测, 子代理沙箱隔离, 行为异常检测, 安全审计追踪, 语义安全分析, 结构化校验, 记忆后端防护桥接

**评分**: 55

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/shieldcortex)

---

## [18. Tender Offer Arbitrage Scanner](https://clawhub.ai/d-wwei/tender-offer-arbitrage)

**Slug**: `tender-offer-arbitrage`  
**Version**: 2.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 扫描市场上的要约收购(Tender Offer)套利机会，分析价差、odd-lot优先权和风险，生成投资分析报告。

**中文介绍**: 该能力用于在市场上自动扫描并核验要约收购（Tender Offer）套利机会，围绕要约价与市场价价差、odd-lot 优先权条款及潜在风险因素进行量化分析，并输出结构化的投资分析报告。能力边界在于依赖公开披露信息（主要为 SEC EDGAR）与可获取的行情数据进行判断，无法替代非公开信息核实、实时成交执行与个别要约条款的法律解释。典型场景包括事件驱动/并购套利团队对潜在标的的批量筛选、机会跟踪与投前研判。关键技术形态为基于 Python 的数据管道：抓取与解析 EDGAR 文件、规则校验与特征抽取、价差与风险模型计算、以及自动化报告生成。

**关键词**: 要约收购套利, 事件驱动交易, 价差分析, 监管申报解析, 自动化扫描, 投资分析报告生成, Tender, Offer

**评分**: 42

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tender-offer-arbitrage)

---

## [19. laiye-doc-processing](https://clawhub.ai/Jeane-li/laiye-doc-processing)

**Slug**: `laiye-doc-processing`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Enterprise-grade agentic document processing API. Accurately extracts key fields and line items from invoices, receipts, orders and more across 10+ file form...

**中文介绍**: 这是一个企业级智能文档处理API，可从发票、收据、订单、合同等多类业务文档的PDF/图片/Office等10+格式中提取关键字段与明细行，输出结构化JSON或Excel并提供字段级置信度，典型用于财务报销、采购对账、合同要素抽取与业务录入自动化。能力边界在于仅覆盖文档识别与结构化抽取本身，不负责业务规则校验、流程审批或下游系统落库。关键技术形态包括同步/异步任务式调用、URL或base64文件输入、基于VLM的文档识别结果访问，以及可通过自定义模型参数进行抽取定制与优化。

**关键词**: 文档信息抽取, 票据识别, 发票行项目抽取, 多格式文档解析, OCR, 字段级置信度评分, 异步任务 API, 自定义模型参数

**评分**: 36

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/laiye-doc-processing)

---

## [20. Claw Soul Backup](https://clawhub.ai/danielglh/claw-soul-backup)

**Slug**: `claw-soul-backup`  
**Version**: 0.1.2  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: Store encrypted OpenClaw workspace backups and restore them via token-secured API using claw-vault.com with local encryption and credential management.

**中文介绍**: 该方案用于将 OpenClaw 工作区备份在本地加密后上传到 claw-vault.com，并通过带令牌鉴权的 API 执行加密备份的存储与恢复，同时包含本地凭据管理与持久化。能力边界在于仅覆盖备份/恢复链路与凭据配置，不涉及工作区内容编辑、协作或运行环境管理。典型场景是设备更换/重装后的快速恢复、跨机器迁移以及灾备回滚等需要安全保存与取回工作区快照的流程。关键技术形态包括客户端本地加密、令牌安全 API 访问，以及将凭据配置固定在用户目录下的 JSON 配置文件中。

**关键词**: 加密备份, 工作区备份, 备份恢复, 令牌认证, API 访问控制, 本地加密, 凭证管理, 配置文件路径, 云端备份存储, 密钥管理

**评分**: 22

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/claw-soul-backup)

---

## [21. Pretenziya Ru](https://clawhub.ai/aggel008/pretenziya-ru)

**Slug**: `pretenziya-ru`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: Составь претензию или жалобу в банк, магазин, управляющую компанию, госорган или работодателя по описанной ситуации.

**中文介绍**: 该能力用于根据用户描述的具体情况自动起草面向银行、商店、物业/ управляющая компания、政府机构或雇主的正式投诉/申诉（претензия/жалоба）文本，输出以规范文书为主而非提供法律结论。能力边界在于仅生成文本草案并依赖输入信息的完整性，不能替代律师意见、事实核验或代表用户提交与跟进。典型场景包括退款纠纷、服务质量争议、劳动权益问题、行政事项投诉等，关键技术形态为基于指令与情境描述的模板化文书生成与措辞规范化，更新仅涉及归因链接从 @maya_logs 改为 t.me/maya_logs，功能与规则不变。

**关键词**: 投诉信生成, 索赔函生成, 法律文书写作, 消费维权, 银行纠纷, 电商购物纠纷, 物业管理纠纷, 政府部门申诉, 劳动争议, 俄语文本生成

**评分**: 11

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/pretenziya-ru)

---

## [22. Nalog Ru](https://clawhub.ai/aggel008/nalog-ru)

**Slug**: `nalog-ru`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: Рассчитай налог УСН 6%, НПД для самозанятых и страховые взносы ИП по введённым доходам и периоду.

**中文介绍**: 该能力可根据用户输入的收入与时间区间，计算俄罗斯税制下的УСН 6%简化税、面向自雇的НПД税以及个体工商户（ИП）的保险缴费，并输出对应金额结果。能力边界在于仅覆盖这几类税费的规则化计算，依赖输入数据的准确性，不处理会计做账、申报提交、税务咨询或法规争议场景。典型场景是自雇者或个体工商户在不同周期内快速估算税费负担与现金流。关键技术形态表现为参数化税务规则引擎/公式计算模块，按期间聚合收入并生成税费明细与汇总。

**关键词**: 俄罗斯税务计算器, 简化税制（УСН 6%）, 自雇税（НПД）, 个体工商户（ИП）, 保险费缴纳, 收入计算, 税期计算, 税务申报辅助

**评分**: 21

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/nalog-ru)

---

## [23. Dogovor Ru](https://clawhub.ai/aggel008/dogovor-ru)

**Slug**: `dogovor-ru`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: Объясни, разбери и выдели риски в российских договорах — аренды, трудовых, кредитных, ипотечных и любых других.

**中文介绍**: 该能力用于对俄文合同文本（如租赁、劳动、贷款、按揭等）进行解释拆解并识别潜在风险点，输出面向阅读理解与风险提示的分析结果。能力边界在于仅基于输入文本做语义与条款层面的推断，无法替代正式法律意见、也无法保证覆盖司法实践与最新法规变化。典型场景包括合同签署前审阅、条款谈判对比、风险清单与重点条款定位；关键技术形态主要是俄文法律文本解析、条款结构化抽取与风险规则/模型匹配生成。

**关键词**: 合同审查自动化, 合同风险识别, 法律文本分析, 俄语合同, 俄罗斯法律, 合同条款解读, 租赁合同, 劳动合同, 贷款合同, 抵押贷款合同, 法律合规检查

**评分**: 22

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/dogovor-ru)

---

## [24. Chinovnik Ru](https://clawhub.ai/aggel008/chinovnik-ru)

**Slug**: `chinovnik-ru`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: Переведи официальные письма, постановления, госдокументы и юридические тексты с бюрократического языка на понятный русский.

**中文介绍**: 该能力用于将官方信函、决定/ постановления、政府文件与法律文本从官僚体表述改写为通俗易懂的俄语，侧重提升可读性与理解效率而非提供法律结论或替代专业法律意见。典型场景包括公众解读政务公告、企业内部合规沟通、媒体/客服对政策内容的转述与摘要。关键技术形态是面向俄语的法律/政务文体识别与语义改写（paraphrase）能力，结合术语保真与语气降噪的风格迁移策略。最新变更仅涉及署名链接替换与版本号更新至 1.0.2。

**关键词**: 官僚语言, 简明语言, 俄语改写, 文本简化, 公文解读, 政府文件, 法律文本, 司法文书, 官方信函, 文书润色, 插件技能

**评分**: 28

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/chinovnik-ru)

---

## [25. Analizy Ru](https://clawhub.ai/aggel008/analizy-ru)

**Slug**: `analizy-ru`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: Расшифруй результаты медицинских анализов, объясни отклонения от нормы и подскажи на что обратить внимание врачу.

**中文介绍**: 该能力用于对体检/化验单结果进行解读，说明哪些指标偏离参考范围、可能代表的常见原因，并给出就诊时可提醒医生重点关注的方向与追问问题；能力边界是不替代医生诊断与处方，无法仅凭化验结果确定病因或给出治疗方案，需结合症状、病史与复查。典型场景包括用户拿到血常规、生化、尿检、激素、甲功等报告后做初步理解与就医沟通准备。关键技术形态通常为文本/图片报告结构化抽取（指标-数值-单位-参考区间）、基于医学知识库与规则/统计模型的异常判定与解释生成，以及针对风险信号的分级提示与建议补充检查项。

**关键词**: 医学检验报告解读, 化验单解析, 参考范围异常解释, 检验指标解读, 就诊准备指导, 医生沟通辅助, 患者健康教育, 临床注意事项提示

**评分**: 17

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/analizy-ru)

---

