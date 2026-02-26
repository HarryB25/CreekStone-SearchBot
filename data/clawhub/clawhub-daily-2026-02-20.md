# ClawHub Skills Daily | 2026-02-20

> 共 6 个 skills

## [1. AgentWeb.live — Global Business Directory](https://clawhub.ai/zerabic/agentweb)

**Slug**: `agentweb`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: Search and retrieve business data from the AgentWeb.live global business directory. Use when: user needs to find a business, get a phone number, address, ema...

**中文介绍**: 该能力用于从 AgentWeb.live 全球企业名录中搜索并检索企业数据，可返回电话、地址、邮箱等基础联系信息，但能力边界主要限于目录中已收录且可检索的公开数据，无法保证覆盖率与实时准确性。典型场景是用户需要快速查找某个商家/机构并获取联系方式或基础档案信息。关键技术形态为对外部目录检索接口的封装与数据拉取，并在首次使用时自动注册获取免费 API Key、在缺失密钥时通过邮箱触发注册流程以完成自动化鉴权。

**关键词**: 企业目录检索, 商业数据查询, 企业联系方式获取, 电话地址查询, API 密钥自动注册, 自动化入门配置, 命令行依赖（curl）, Agent 工具技能, 业务信息聚合

**评分**: 12

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/agentweb)

---

## [2. Agent Emacs](https://clawhub.ai/PiTZE/agent-emacs)

**Slug**: `agent-emacs`  
**Version**: 1.0.2  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: Unified persistent text-based environment for AI agents. Use when an agent needs to maintain state across sessions, perform structural code editing, or manag...

**中文介绍**: 这是一个为 AI Agent 提供统一、可持久化的文本环境，用于跨会话保存状态，并支持对代码进行结构化编辑与管理。其能力边界在于主要围绕文本与代码资产的持久化、变更与组织，不强调新增推理能力或外部工具链集成。典型场景包括长任务的上下文连续维护、跨轮次迭代代码修改、以及对多文件/项目内容进行一致性管理。关键技术形态是基于文本的持久化存储与结构化代码编辑能力，本次版本与上一版本一致无功能变更。

**关键词**: AI 代理环境, 持久化状态, 文本界面, 结构化代码编辑, 代码重构, 代理工作区, 本地开发环境, Agent

**评分**: 40

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/agent-emacs)

---

## [3. Chainwatch](https://clawhub.ai/ppiankov/chainwatch)

**Slug**: `chainwatch`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Runtime safety enforcement for shell commands via chainwatch policy engine

**中文介绍**: 该方案通过 chainwatch 策略引擎对 Shell 命令执行进行运行时安全约束与拦截，可在命令落地前进行策略评估并阻断高风险操作，但边界在于主要覆盖命令执行路径本身，难以替代主机加固或对非 Shell 通道的行为做全量治理。典型场景包括自动化运维、CI/CD、以及 AI/Agent（如 OpenClaw agents）在执行系统命令时的安全护栏与合规控制。关键技术形态是“运行时策略引擎 + 命令执行监控/拦截点 + 可配置策略（policy）”的组合，并已扩展到对 OpenClaw 智能体运行时安全的支持。

**关键词**: 运行时安全, Shell 命令安全, 策略引擎, 策略即代码, 命令执行控制, 安全策略执行, 命令审计, Chainwatch

**评分**: 52

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/chainwatch)

---

## [4. HeyLead](https://clawhub.ai/D4umak/heylead)

**Slug**: `heylead`  
**Version**: 0.9.13  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 3

**原始简介**: HeyLead is an autonomous LinkedIn SDR that creates buyer personas, manages outreach campaigns, sends personalized messages, follows up, and tracks pipeline a...

**中文介绍**: HeyLead 是一款面向 LinkedIn 的自治式 SDR 工具，可自动生成买家画像、编排并执行外联活动，发送个性化消息与跟进，并对线索与管道进展进行追踪。其能力边界主要在 LinkedIn 场景内的获客与触达，依赖平台数据与消息权限，无法替代人工完成复杂谈判、跨渠道营销或对受限/缺失数据的判断。典型使用场景包括 B2B 线索挖掘、冷启动外联、序列化跟进和销售漏斗管理。关键技术形态以“自动化外联编排 + 个性化内容生成 + 线索/管道追踪”的代理式工作流为核心，当前版本更新至 v0.9.13。

**关键词**: 买家画像生成, 潜客挖掘, 外联活动管理, 个性化私信, 自动跟进, 销售管道跟踪, 线索培育, HeyLead

**评分**: 49

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/heylead)

---

## [5. Clack](https://clawhub.ai/fbn3799/clack)

**Slug**: `clack`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Deploy and manage Clack, a voice relay server for OpenClaw. Bridges voice input (WebSocket) through STT → OpenClaw agent → TTS, enabling real-time voice conv...

**中文介绍**: Clack 是面向 OpenClaw 的语音中继服务器，用于将客户端的实时语音输入通过 WebSocket 接入后，依次完成语音转文本（STT）→ OpenClaw Agent 处理 → 文本转语音（TTS）并回传，实现端到端语音对话。能力边界在于它只负责语音链路的接入与转发编排，不提供独立的对话智能或内容生成，且移动端 Clack App（iOS/Android）仍处于待发布状态。典型场景是为已部署的 OpenClaw 增加低延迟的语音交互入口，适用于移动端或其他支持 WebSocket 的语音采集端。关键技术形态包括 WebSocket 实时流、STT/TTS 管线以及与 OpenClaw Agent 的编排集成。

**关键词**: 语音中继服务器, 实时语音对话, 语音转文本（STT）, 文本转语音（TTS）, Agent 语音链路, 语音助手网关, 移动端语音客户端, 语音通信桥接

**评分**: 37

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/clack)

---

## [6. Host Hardening](https://clawhub.ai/ppiankov/server-host-hardening)

**Slug**: `server-host-hardening`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Harden an OpenClaw Linux server with SSH key-only auth, UFW firewall, fail2ban brute-force protection, and credential permissions. Use when setting up a new...

**中文介绍**: 该方案用于加固新部署的 OpenClaw Linux 服务器，核心能力是将 SSH 改为仅密钥登录，配合 UFW 防火墙与 fail2ban 实现端口访问控制和暴力破解防护，并强化凭据文件权限管理。其边界在于主要覆盖主机登录与网络入口层面的安全基线与自动化封禁，不替代应用层漏洞修复、账号体系治理或整体零信任架构。关键技术形态包括 SSHD 配置收敛、UFW 规则策略、fail2ban 监控与封禁链路，以及网关相关的 systemd 服务编排。

**关键词**: 主机加固, Linux 服务器安全, SSH 密钥认证, UFW 防火墙, 暴力破解防护, 入侵防御, 凭据权限管理, 最小权限配置, 服务器初始化

**评分**: 27

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/server-host-hardening)

---

