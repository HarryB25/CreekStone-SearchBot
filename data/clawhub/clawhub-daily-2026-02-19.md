# ClawHub Skills Daily | 2026-02-19

> 共 8 个 skills

## [1. Post Job](https://clawhub.ai/zhangdong/post-job)

**Slug**: `post-job`  
**Version**: 1.1.9  
**Stats**: ⭐ 0 | ⬇️ 31 | 🧩 15

**原始简介**: Post free job ads to 20+ job boards such as LinkedIn, Indeed, Ziprecruiter etc. to receive applicant resumes via email.

**中文介绍**: 该能力用于将职位信息一键分发到 LinkedIn、Indeed、ZipRecruiter 等 20+ 招聘平台，并通过邮件汇总接收候选人简历。能力边界在于它主要覆盖“发布与收集投递”链路，不保证各平台的曝光、排序或投递转化效果，也不包含后续筛选、面试与录用流程。典型场景是招聘团队需要快速铺量发布、统一管理多平台投递入口并集中收取简历。关键技术形态是多渠道职位分发的聚合接口/服务与基于邮件的简历回传；近期仅更新文档校验说明，移除了职位描述最少 100 字限制且无功能变更。

**关键词**: 职位发布, 职位广告分发, 招聘渠道聚合, 多招聘网站集成, 招聘自动化, 简历收集, 邮件接收简历, 职位描述校验, 参数校验

**评分**: 25

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/post-job)

---

## [2. Coding Agent Backup](https://clawhub.ai/nickchan0412/coding-agent-backup)

**Slug**: `coding-agent-backup`  
**Version**: 1.0.0  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 1

**原始简介**: Delegate coding tasks to Codex, Claude Code, or Pi agents via background process. Use when: (1) building/creating new features or apps, (2) reviewing PRs (sp...

**中文介绍**: 这是一个通过后台进程把编码任务委派给 Codex、Claude Code 或 Pi 等智能体的能力，采用 bash-first 的工作流，并要求交互式会话必须在 pty:true 的伪终端中运行。典型场景是开发新功能/新应用、在临时目录做 PR 评审、重构等需要隔离工作目录并可并行推进的任务（可配合 git worktrees 监控与管理进程）。能力边界在于不适用于简单修补、纯代码阅读类工作，也不建议在特定的默认工作区（如 ~/clawd）内执行。关键技术形态是 CLI 驱动的后台任务编排、可指定任意工作目录的智能体拉起与会话管理。

**关键词**: 代码代理, 任务委派, 后台进程, 命令行工具, 伪终端 pty, 进程监控, 临时目录代码审查, 重构自动化

**评分**: 46

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/coding-agent-backup)

---

## [3. Self Improving](https://clawhub.ai/ivangdavila/self-improving)

**Slug**: `self-improving`  
**Version**: 1.1.2  
**Stats**: ⭐ 5 | ⬇️ 3053 | 🧩 5

**原始简介**: Self-reflection + Self-criticism + learning from corrections. Agent evaluates its own work, catches mistakes, and improves permanently.

**中文介绍**: 该能力聚焦于让智能体对自身输出进行自我反思与自我批判，并将外部纠错反馈沉淀为可复用的改进以降低重复错误，边界在于仅能基于已有输入与反馈进行评估与调整，无法保证在缺少真实标注或环境验证时的绝对正确。典型场景包括生成内容后的自检、代码/文档审阅、根据用户指出的问题迭代回答与长期优化提示策略。关键技术形态是“自评估—发现错误—应用纠正—形成记忆/规则”的闭环学习机制，变更记录仅新增 EXTRA_FILES.txt，不影响功能与对用户可见特性。

**关键词**: 纠错学习, 持续学习, 错误检测, 反馈回路, 记忆更新, 自动化质量控制, Self, Improving

**评分**: 36

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/self-improving)

---

## [4. Ghost Browser](https://clawhub.ai/neothelobster/neo-stealth-browser)

**Slug**: `neo-stealth-browser`  
**Version**: 1.0.4  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 5

**原始简介**: Automated Chrome browser using nodriver for AI agent web tasks. Full CLI control with LLM-optimized commands — text-based interaction, markdown output, sessi...

**中文介绍**: 该工具基于 nodriver 自动化控制 Chrome，用于 AI Agent 执行网页任务，提供面向 LLM 的命令式 CLI，实现纯文本交互并可输出 Markdown。能力边界在于依赖本地/可用的 Chrome 环境与 DevTools/CDP 驱动能力，主要覆盖浏览器可自动化的操作与数据提取，不保证对强反爬、复杂验证码或深度权限隔离站点稳定生效。典型场景包括自动登录与表单填写、信息检索与抓取、跨页面流程编排、将网页操作串联为可复用脚本。关键技术形态是“CLI + LLM 优化指令集 + Chrome/CDP 自动化”，并通过扩展（如 cdp-input-fix）修复输入交互等兼容性问题。

**关键词**: 浏览器自动化, 命令行接口（CLI）, Agent 网页任务, 文本交互, 浏览器扩展, Ghost, Browser, Automated

**评分**: 43

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/neo-stealth-browser)

---

## [5. Prayer Times Id](https://clawhub.ai/zckyachmd/prayer-times-id)

**Slug**: `prayer-times-id`  
**Version**: 1.0.3  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 4

**原始简介**: Menjadwalkan reminder waktu shalat (Indonesia) ke OpenClaw System Event berdasarkan lokasi, lengkap dengan quote harian Islami dan status Ramadan otomatis.

**中文介绍**: 该能力用于根据用户所在位置自动计算并在 OpenClaw System Event 中创建/更新每日礼拜（shalat）提醒，同时附带每日伊斯兰语录，并能自动识别与标记斋月状态。能力边界在于其依赖外部祷告时间数据源与地理位置信息的准确性，主要面向印尼语用户的日常祷告提醒与宗教氛围内容推送场景。关键技术形态包括位置到祷告时间的计算与接口调用（如对 Aladhan timings URL 的参数透传与 methodSettings 调整）、事件调度写入系统事件流，以及按日刷新内容与状态逻辑。

**关键词**: 伊斯兰礼拜时间, 礼拜提醒, 位置定位, 事件调度, 系统事件触发, 斋月状态检测, 每日伊斯兰语录, Prayer

**评分**: 23

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/prayer-times-id)

---

## [6. virtual-remote-desktop](https://clawhub.ai/zhangxin15435/virtual-remote-desktop)

**Slug**: `virtual-remote-desktop`  
**Version**: 1.0.3  
**Stats**: ⭐ 1 | ⬇️ 336 | 🧩 4

**原始简介**: KasmVNC-based virtual desktop for headless Linux with AI-first automation and human handoff. Use when most steps are automated but a user must manually inter...

**中文介绍**: 这是一个基于 KasmVNC 的无头 Linux 虚拟桌面，面向 AI 优先的自动化流程，并支持在自动化完成大部分步骤后将控制权交接给人工进行必要的手动操作。能力边界在于它主要提供远程桌面与人机协作承载，不负责具体业务逻辑自动化本身，适用于“自动化为主、人工介入为辅”的远程处理场景。关键技术形态是基于 VNC 的虚拟桌面会话与自动化/人工接管协作机制；1.0.3 版本仅为元数据更新，无代码或文档变化。

**关键词**: 虚拟桌面, 远程桌面, 浏览器访问桌面, 自动化流程, 人机协同, 人工接管, 远程交互, virtual-remote-desktop

**评分**: 43

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/virtual-remote-desktop)

---

## [7. Explorium AgentSource](https://clawhub.ai/yossigolan/explorium-agentsource)

**Slug**: `explorium-agentsource`  
**Version**: 1.0.1  
**Stats**: ⭐ 0 | ⬇️ 11 | 🧩 2

**原始简介**: Find and export B2B companies or contacts using AgentSource filters with options for enrichment, events, and CSV export.

**中文介绍**: 该能力用于基于 AgentSource 过滤条件检索并导出 B2B 公司或联系人，支持补全/丰富信息、结合活动数据，并可输出为 CSV。能力边界在于依赖外部 Explorium AgentSource API 与密钥认证，用户查询文本在特定调用模式下会发送到远端且需要用户同意，密钥必须通过环境变量或 CLI 安全配置而不能在对话中提供。典型场景包括销售线索挖掘、市场拓展名单生成、活动相关的目标账户筛选与数据导出。关键技术形态是基于过滤器的检索与鉴权流程、可选的 enrichment 与事件数据联动、以及对远端数据发送与环境变量需求的元数据声明与隐私控制。

**关键词**: B2B公司检索, 联系人检索, 线索挖掘, 数据丰富化, 事件数据, 筛选器查询, API密钥管理, 隐私合规

**评分**: 37

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/explorium-agentsource)

---

## [8. Ticket Monitor Ichinosuke](https://clawhub.ai/texka001/ticket-monitor-ichinosuke)

**Slug**: `ticket-monitor-ichinosuke`  
**Version**: 1.0.3  
**Stats**: ⭐ 0 | ⬇️ 0 | 🧩 4

**原始简介**: Monitors 春風亭一之輔's official site for new Tokyo performance tickets and sends notifications to a specified Discord webhook.

**中文介绍**: 该能力用于监控春風亭一之輔官网的东京公演票务是否上新，并在检测到新票时通过指定的 Discord Webhook 推送通知。能力边界在于仅覆盖官网公开的票务更新与通知触发，不负责购票、账号登录或跨平台票源整合。典型场景是粉丝或运营人员需要及时获知开票动态并同步到社群频道。关键技术形态为网页内容监测/差异检测 + Webhook 事件通知，配置上以环境变量注入 Webhook 地址而非本地配置文件保存。

**关键词**: 票务监控, 演出票提醒, 网页监测, 网页抓取, 变更检测, 通知推送, 自动化脚本, 环境变量配置

**评分**: 18

**详情地址**: [ClawHub API](https://clawhub.ai/api/v1/skills/ticket-monitor-ichinosuke)

---

