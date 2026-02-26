# ClawHub Skills Daily | 2026-02-22

> 共 8 个 skills

## [1. Kekik Crawler](https://clawhub.ai/keyiflerolsun/kekik-crawler)

**Slug**: `kekik-crawler`  
**Version**: 0.1.0-rc1  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Scrapling-only, deterministic web crawler with clean SRP architecture, presets, checkpointing, and JSONL/report outputs.

**中文介绍**: 这是一个基于 Scrapling 的确定性网页爬虫，采用清晰的单一职责（SRP）架构，并提供预设策略、断点/检查点续爬能力与 JSONL/报告输出。能力边界在于面向可重复、可控的抓取流程与结构化结果产出，不强调多引擎混用或高度动态渲染页面的处理。典型场景包括批量站点巡检、内容归档与数据采集任务的稳定复现，以及需要审计与可追踪抓取过程的离线分析。关键技术形态体现为“Scrapling-only + 确定性调度/执行 + 预设配置 + checkpoint 状态管理 + 结构化输出与测试/报告链路”。

**关键词**: 确定性爬取, 单一职责原则（SRP）, 模块化架构, 自动化测试, Kekik, Crawler, Scrapling-only, deterministic

**评分**: 27

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/kekik-crawler)

---

## [2. Skill](https://clawhub.ai/askbeka/tentactl)

**Slug**: `tentactl`  
**Version**: 0.3.0  
**Stats**: ⭐ 0 | ⬇️ 26 | 🧩 6

**原始简介**: Interact with the Kraken cryptocurrency exchange — spot + futures, REST + WebSocket. Use when: (1) checking crypto prices or market data, (2) viewing account...

**中文介绍**: 该能力用于与 Kraken 加密货币交易所交互，覆盖现货与合约，并同时支持 REST 与 WebSocket 两种接口形态。典型场景包括查询行情/市场数据、查看账户与资产信息、以及执行或管理交易相关操作。能力边界在于仅能在 Kraken 提供的接口与权限范围内进行数据读取和下单等动作，无法替代交易所之外的数据源或进行链上直接操作；最近更新新增多项工具并强化错误处理与整体清理。

**关键词**: 加密货币交易, 现货交易, 期货交易, 市场数据, 账户查询, 交易机器人, 错误处理, Skill

**评分**: 19

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tentactl)

---

## [3. Delx Ops Guardian](https://clawhub.ai/davidmosiah/delx-ops-guardian)

**Slug**: `delx-ops-guardian`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: Automatically detects, assesses, and safely mitigates incidents in OpenClaw production agents, providing detailed reports and verified recovery.

**中文介绍**: 该能力用于自动检测与评估 OpenClaw 生产代理中的运行事故，并在安全约束下执行缓解与恢复，输出包含处置过程与结果校验的详细报告。能力边界在于仅在明确的 allowlist/disallowlist 范围内操作，超出范围不执行且关键步骤需人工审批把关。典型场景包括生产代理异常、任务失败、资源/依赖波动等需要快速止损与恢复验证的事件。关键技术形态是事件检测与风险评估、受限动作编排（白黑名单策略）以及带人审门的自动化恢复与验证闭环。

**关键词**: 事故检测, 事件响应, 自动化缓解, 生产环境 Agent 运维, 安全护栏, 允许名单/拒绝名单, 人工审批流程, 恢复验证, 运行报告

**评分**: 55

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/delx-ops-guardian)

---

## [4. TrustMyAgent](https://clawhub.ai/Anecdotes-Yair/trust-my-agent-ai)

**Slug**: `trust-my-agent-ai`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: 🛡️ TrustMyAgent - Security posture monitoring for AI agents. Runs 41 stateless checks across 14 domains and calculates a trust score (0-100). Supports local...

**中文介绍**: TrustMyAgent 是面向 AI 代理的安全态势监控工具，通过覆盖 14 个领域的 41 项无状态、只读检查来评估配置与运行环境，并以 0–100 的信任分数及逐项通过/失败结果呈现。它的能力边界在于仅做检测与评分，不执行修复或主动防护，且可在本地模式下完全离线运行以避免任何网络调用。典型场景包括在部署前/变更后对代理环境做基线体检、合规与风险自查、以及在隐私敏感环境中进行周期性安全扫描。关键技术形态是规则化的无状态检查引擎 + 可解释的评分与明细报告，并提供可选的干跑预览与开源透明的检查逻辑/遥测数据格式。

**关键词**: Agent安全态势监控, 安全基线检查, 静态安全检查, 信任评分, 合规自评估, 本地离线扫描, 安全遥测, 开源可审计, 定时安全扫描

**评分**: 39

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/trust-my-agent-ai)

---

## [5. Neolata Memory Engine](https://clawhub.ai/Jeremiaheth/neolata-mem)

**Slug**: `neolata-mem`  
**Version**: 0.8.5  
**Stats**: ⭐ 0 | ⬇️ 48 | 🧩 12

**原始简介**: Graph-native memory engine for AI agents — hybrid vector+keyword search, biological decay, Zettelkasten linking, trust-gated conflict resolution, explainabil...

**中文介绍**: 这是面向 AI Agent 的图原生记忆引擎，提供混合向量+关键词检索、Zettelkasten 式双向链接与可解释的记忆追溯，用于把长期知识与上下文关系结构化并可回放。其能力边界在于主要管理与检索“记忆/知识”而非替代业务执行或事实裁判，冲突处理依赖信任门控策略，遗忘/衰减属于启发式机制并不保证严格最优。典型场景包括多轮对话长期记忆、跨任务知识复用、信息源冲突整合与基于证据链的回答解释。关键技术形态是图数据模型承载记忆节点与关系，叠加混合检索、时间/生物式衰减策略、链接网络生成以及信任门控的冲突消解与解释层。

**关键词**: 智能体记忆引擎, 图原生存储, 混合检索, 关键词检索, 遗忘机制, 信任门控, 冲突消解, 可解释性

**评分**: 52

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/neolata-mem)

---

## [6. Alicloud Ai Audio Tts](https://clawhub.ai/cinience/alicloud-ai-audio-tts)

**Slug**: `alicloud-ai-audio-tts`  
**Version**: 1.0.3  
**Stats**: ⭐ 0 | ⬇️ 331 | 🧩 4

**原始简介**: Generate human-like speech audio with Model Studio DashScope Qwen TTS models (qwen3-tts-flash, qwen3-tts-instruct-flash). Use when converting text to speech,...

**中文介绍**: 该能力用于将文本转换为接近真人的语音音频，基于 DashScope Model Studio 的 Qwen TTS 模型（如 qwen3-tts-flash、qwen3-tts-instruct-flash）进行语音合成。典型场景包括内容朗读、有声化播报、语音助手输出等文本到语音的生成需求。能力边界在于它只负责 TTS 合成与相关参数控制，不覆盖语音识别、对话理解或端到端语音交互；技术形态以云端模型调用的方式输出音频结果。

**关键词**: 文本转语音, 语音合成, 语音音频生成, 云端推理, 插件技能（Skill）, Alicloud, Audio, Tts

**评分**: 6

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/alicloud-ai-audio-tts)

---

## [7. StandX CLI](https://clawhub.ai/wjllance/standx-cli)

**Slug**: `standx-cli`  
**Version**: 0.4.3  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 8

**原始简介**: Crypto trading CLI for StandX exchange v0.4.3. Use when users need to: (1) Query crypto market data (prices, order books, klines, funding rates), (2) Manage...

**中文介绍**: 这是面向 StandX 交易所的加密交易命令行工具（v0.4.3），用于在终端中查询行情数据（价格、订单簿、K线、资金费率等）并进行账户与交易管理等操作。能力边界在于只覆盖 StandX 提供的接口与权限范围，无法获取或执行超出交易所 API 的数据与动作，且主要面向偏技术用户的脚本化/自动化使用场景。典型场景包括快速拉取市场数据做监控与分析、在服务器或 CI 环境中批量下单/撤单与管理仓位。关键技术形态是基于交易所 API 的 CLI 客户端，强调命令行交互与可脚本调用的自动化能力。

**关键词**: 加密货币交易, 交易命令行工具, 交易所API集成, 市场数据查询, 实时价格, 订单簿数据, K线数据, 资金费率, 交易下单, 安装脚本

**评分**: 21

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/standx-cli)

---

## [8. TuleBank](https://clawhub.ai/aromeoes/tulebank)

**Slug**: `tulebank`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: TuleBank — check wallet balance, send ARS to any CVU/ALIAS, swap USDC/wARS, manage beneficiaries, and off-ramp crypto to Argentine bank accounts.

**中文介绍**: TuleBank 是一项面向阿根廷出金与转账的工具能力，可在 Base 链上查询并管理智能钱包余额，进行 USDC 与 wARS 的兑换，并将 ARS 转账到任意 CVU/ALIAS 或提现至阿根廷银行账户。其能力边界主要在于链上钱包与代币操作叠加本地法币出金流程，需依赖 KYC/OTP、受益人确认等合规环节，并通过 Ripio Ramps 完成银行侧落地。典型场景包括加密资产换汇后快速出金、向本地账户/收款别名转 ARS、以及批量管理受益人以便重复出金。关键技术形态是基于 CLI 的交易与账户管理入口，结合 Base 智能钱包交互、代币 Swap、以及与 Ripio Ramps 的出金接口集成。

**关键词**: 加密货币法币出金, 阿根廷银行转账, 稳定币兑换, 智能钱包, 命令行钱包, 收款人管理, TuleBank, check

**评分**: 30

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/tulebank)

---

