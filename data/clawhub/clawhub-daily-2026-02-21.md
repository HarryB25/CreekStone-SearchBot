# ClawHub Skills Daily | 2026-02-21

> 共 8 个 skills

## [1. Nova App Builder](https://clawhub.ai/zfdang/nova-app-builder)

**Slug**: `nova-app-builder`  
**Version**: 1.2.5  
**Stats**: ⭐ 1 | ⬇️ 27 | 🧩 9

**原始简介**: Build and deploy Nova Platform apps (TEE apps on Sparsity Nova / sparsity.cloud). Use when a user wants to create a Nova app, write enclave application code,...

**中文介绍**: 该能力用于在 Sparsity Nova / sparsity.cloud 上构建与部署 Nova Platform 的 TEE 应用，覆盖从创建 Nova 应用到编写 enclave 端代码并触发平台构建发布的流程。能力边界在于本地侧不再负责执行旧的 build_push.py 或手工维护构建配置，平台会在构建时从 Git 拉取源码并在 app-hub 自动生成 enclaver.yaml 与 nova-build.yaml。典型场景是开发者基于脚手架快速初始化项目、迭代 enclave 代码后提交到仓库，由平台完成后续构建与部署。关键技术形态是基于 Git 的平台化构建流水线与构建时自动生成的 enclave/构建描述文件配套调整了 scaffold 的后续指引。

**关键词**: 可信执行环境, 构建部署工具, Git 驱动构建, CI/CD 流水线, 配置文件生成, Nova, App, Builder

**评分**: 29

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/nova-app-builder)

---

## [2. Mauritius Retail Prices](https://clawhub.ai/v7wm8gqgdr-design/mauritius-retail-prices)

**Slug**: `mauritius-retail-prices`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Scrapes max retail prices from PFU Mauritius government website with pagination support to find items with effective dates matching today

**中文介绍**: 该能力从毛里求斯政府 PFU 网站抓取并汇总商品最高零售价数据，支持跨页检索并仅返回生效日期为当天的条目，输出包含品牌、产品、价格与条码等结构化结果。适用于每日价格更新监测、零售合规核查与内部价格数据库自动同步等场景。能力边界在于仅覆盖 PFU 网站已公开发布的数据与当日生效记录，且依赖网站结构与可访问性，无法保证历史补全或站点变更后的稳定性。关键技术形态为基于网页抓取的分页遍历与日期过滤管道，并内置网络错误、分页异常与限流的自动处理机制。

**关键词**: 政府网站爬虫, 零售价格数据, 最高零售价, 分页抓取, 当日生效过滤, 结构化数据输出, 命令行工具, 条形码数据, 限流处理, 网络错误重试

**评分**: 22

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/mauritius-retail-prices)

---

## [3. FairScale Solana](https://clawhub.ai/RisheeA/fairscale-solana)

**Slug**: `fairscale-solana`  
**Version**: 1.0.5  
**Stats**: ⭐ 0 | ⬇️ 696 | 🧩 7

**原始简介**: Solana wallet reputation. Ask anything in plain English — "is this a bot?", "whale?", "diamond hands?" — get instant answers.

**中文介绍**: 该产品提供面向 Solana 钱包的实时“信誉/风险”评估能力，支持用自然语言询问钱包是否为机器人、巨鲸或长期持有者等并快速返回结果，但能力边界主要在链上行为与规则建模的推断，无法保证对钱包真实身份或未来行为作确定性判断。典型场景包括交易前的风险预检与限额建议、对单一或批量地址的风控筛查，以及按业务自定义规则进行评分。关键技术形态为基于 API 的信誉评分服务与端点体系（如 /check、/score/custom、/batch），结合风险等级与最大建议交易额输出，并提供鉴权与限流以及 Pro/Enterprise 的批处理与高级特性。

**关键词**: 钱包信誉评分, 链上风控, 交易前风险评估, 风险等级, 机器人检测, 鲸鱼识别, 批量评分API, 自定义评分规则, 自然语言查询API

**评分**: 46

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/fairscale-solana)

---

## [4. gog-test-demo](https://clawhub.ai/ph4ntonn/gog-test-demo)

**Slug**: `gog-test-demo`  
**Version**: 1.0.10  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 10

**原始简介**: gog-test-demo

**中文介绍**: gog-test-demo 目前仅保留为演示性质的技能，原先与股票市场相关的能力（如新闻、期权、yfinance 脚本辅助等）已被移除，能力边界基本限定在“占位/示例”而非可用的金融数据工具。典型场景是用于测试技能元数据与链接展示、验证最小化文档与流程是否可跑通，而不适合实际行情分析或交易决策。关键技术形态上更偏向轻量级技能壳与元数据配置更新（名称、描述、主页链接），以“Just a demo”作为简化说明。

**关键词**: 技能元数据, 演示项目, 股票市场工具, 期权数据, 财经新闻数据, Python 脚本辅助工具, 文档占位, 主页链接

**评分**: 5

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/gog-test-demo)

---

## [5. Recruiter Assistant](https://clawhub.ai/gakkiismywife/recruiter-assistant)

**Slug**: `recruiter-assistant`  
**Version**: 1.4.2  
**Stats**: ⭐ 0 | ⬇️ 27 | 🧩 12

**原始简介**: A professional recruitment workflow assistant. Evaluates resumes against dynamic requirements and AI proficiency, provides critical Pros/Cons analysis, and p...

**中文介绍**: 这是一个面向招聘流程的智能助手，能将候选人简历与动态岗位要求（含 AI 能力要求）进行对齐评估，并输出有依据的优劣势分析以辅助筛选与沟通。其能力边界在于主要依赖简历与设定标准做文本理解与匹配，不直接替代面试判断、背景调查或对真实性作最终确认。典型场景包括批量初筛、岗位需求变更后的快速复评、以及为面试官生成针对性的追问线索。关键技术形态以规则/权重可配置的要求体系叠加大模型语义解析与对比总结为主，并已针对飞书集成的页面渲染问题通过“先创建后追加”的写入逻辑做了修复。

**关键词**: 招聘流程自动化, 简历解析, 候选人匹配, 岗位需求动态匹配, AI能力评估, 优劣分析, 人才筛选, 飞书集成, 招聘工作流助手, 招聘评估报告生成

**评分**: 42

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/recruiter-assistant)

---

## [6. OpenMM Portfolio](https://clawhub.ai/adacapo21/openmm-portfolio)

**Slug**: `openmm-portfolio`  
**Version**: 0.1.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Balance tracking, order overview, and market data across exchanges using OpenMM.

**中文介绍**: OpenMM 可用于跨多个交易所统一查看资产余额、订单概览与市场数据，但能力边界主要在于信息查询与组合管理辅助，实际可用范围受各交易所所需凭证、资产符号格式与最小下单规则等限制。典型场景包括做跨所资产盘点与风险敞口汇总、跟踪订单与成交、以及拉取订单簿和交易数据用于监控与分析。关键技术形态上以标准化工具接口提供数据访问与发现能力，新增如 get_orderbook、get_trades、discover_pools 等工具，并在元数据中明确了工具权限与参考数据文件以支撑一致的数据读取与解析。

**关键词**: 加密资产组合管理, 多交易所聚合, 余额追踪, 订单概览, 市场数据接口, 订单簿数据, 成交数据, API 凭证管理, 环境变量配置

**评分**: 32

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/openmm-portfolio)

---

## [7. EVC Team Relay](https://clawhub.ai/venturecrew/evc-team-relay)

**Slug**: `evc-team-relay`  
**Version**: 1.1.1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 2

**原始简介**: Read and write Obsidian notes stored in EVC Team Relay collaborative vault. Use when agent needs to: read note content from a shared Obsidian vault, create o...

**中文介绍**: 该能力用于在 EVC Team Relay 的协作 Obsidian vault 中读取与写入笔记内容，适合代理需要从共享知识库检索信息、同步记录或生成新笔记的场景。能力边界在于仅覆盖 vault 内笔记的内容级读写与基础元信息交互，不涉及更广泛的外部系统编排或复杂知识推理。关键技术形态为通过 Relay 的脚本/接口对 Obsidian 文件进行操作，并支持以 `RELAY_TOKEN` 环境变量方式进行鉴权以降低泄露风险与便于配置管理，同时通过补充 `version` 与 `metadata` 提升可发现性与配置治理。

**关键词**: 协作知识库, 笔记读写, 共享笔记库, 环境变量鉴权, 访问令牌管理, 配置管理, 元数据规范, EVC

**评分**: 29

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/evc-team-relay)

---

## [8. Temp Skill](https://clawhub.ai/wzratgit/temp-skill)

**Slug**: `temp-skill`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 提供基于免费数据源的多资产投资组合分析，支持滚动窗口风险平价调仓及完整回测和图表报告生成。

**中文介绍**: 该能力提供基于免费行情数据源的多资产投资组合分析，覆盖股票、ETF、加密货币等，并可自动生成包含收益、风险与配置指标的文字与图表报告。典型场景是做风险平价策略研究、资产配置评估与历史回测复盘，支持滚动窗口调仓以避免未来数据泄露。能力边界在于依赖第三方免费数据的覆盖度与质量，输出用于研究与决策辅助而非交易执行或收益保证。关键技术形态包括多源数据接入与清洗、滚动窗口风险平价权重计算、回测引擎与可视化报表生成（收益曲线、配置图、相关性热力图等）。

**关键词**: 多资产投资组合, 投资组合分析, 风险平价, 滚动窗口, 自动调仓, 回测框架, 前视偏差控制, 免费行情数据源, 量化投资报告, 金融数据可视化

**评分**: 28

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/temp-skill)

---

