import os
import json
from typing import Any, Dict


def _get_timeout() -> float:
    raw = os.getenv("OPENAI_REQUEST_TIMEOUT", "60").strip()
    try:
        value = float(raw)
        if value > 0:
            return value
    except Exception:
        pass
    return 60.0


def _get_model_name() -> str:
    raw = os.getenv("OPENAI_MODEL", "").strip()
    return raw or "gpt-5-2025-08-07"


def _is_gpt5_model(model_name: str) -> bool:
    return model_name.startswith("gpt-5")


def _extract_json_object(raw: str) -> Dict[str, Any]:
    text = (raw or "").strip()
    if not text:
        raise ValueError("empty response")
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start >= 0 and end > start:
            return json.loads(text[start : end + 1])
        raise


def score_content(text: str, client, kind: str = "general") -> dict:
    """
    调用大模型对项目进行评分。
    返回结构：
    {
      "total": int,
      "breakdown": {
         "ai_native": int,
         "tech_niche": int,
         "business": int,
         "team": int,
         "bonus": int,
         "penalty": int
      },
      "reason": "short rationale"
    }
    """
    if client is None:
        return {
            "total": 0,
            "breakdown": {
                "ai_native": 0,
                "tech_niche": 0,
                "business": 0,
                "team": 0,
                "bonus": 0,
                "penalty": 0,
            },
            "reason": "No model available",
        }

    system_prompt = (
        "你是投资评审助手，请严格按给定评分标准打分。"
        "输出 JSON，字段：total（总分）、breakdown（各项分），"
        "reason（不超过120字的中文理由，包含主要加减分点）。\n\n"
        "评分标准（必须逐条对照判断，不能平均打分）：\n"
        "一、AI Native & Agent 原生程度（0–30 分）【最高优先级】\n"
        "1) 用户是否被结构性地转化为“数据标注员”\n"
        "   - 用户行为是否自然地产生高质量反馈 / data-pair\n"
        "   - 数据是否直接反哺系统能力提升\n"
        "   - 数据是否用于训练、评估或策略修正，而非仅用于日志或分析\n"
        "   判断重点：用户是否在“用产品的同时，顺手把模型教会了”\n"
        "2) 是否存在 Online Learning / Self-improvement 的闭环\n"
        "   - 系统是否随着使用而持续变“更强”\n"
        "   - 是否存在 reward / failure-driven 的能力修补机制\n"
        "   - 是否存在跨用户、跨任务的经验迁移\n"
        "   不要求已实现，但需结构可行、方向明确\n"
        "3) 是否从“概率性对话”走向“确定性工作流”\n"
        "   - 是否以交付结果而非“回复内容”为终点\n"
        "   - 是否具备自动任务拆解 / 工具调用执行 / 异常处理重试 / 闭环完成能力\n"
        "   - 包括 Coding Agent / Proactive Agent / Workflow Agent 等\n"
        "4) Agent 四要素完整度\n"
        "   - Reasoning / Memory / Tool-use / Planning 是否系统性具备\n"
        "评分锚点：0–10 互联网范式+LLM；10–20 有 Agent 形态但缺少自进化；20–30 明确 Agent-native 且能力随使用增长\n\n"
        "二、技术路径与 Niche 壁垒（0–25 分）\n"
        "1) 技术路径是否体现“非共识判断力”\n"
        "   - 是否选择主流团队不愿做 / 看不上的方向\n"
        "   - 是否解决一个不性感但足够复杂且硬的问题\n"
        "   - 是否与 Claude Code / Agent 演进方向高度一致或提前押注\n"
        "2) 是否拥有或正在构建原生私有数据飞轮\n"
        "   - 数据为使用自然副产物\n"
        "   - 数据难以被模型厂或通用平台直接获取\n"
        "   - 数据与具体 workflow / context 深度绑定\n"
        "3) 是否存在清晰且可持续的 niche 门槛\n"
        "   - 深度绑定特定行业/场景/工作流\n"
        "   - 真实且持续的 domain knowledge 依赖\n"
        "   - 离开该 niche 就没有意义\n"
        "评分锚点：0–10 易替代；10–18 垂直成立但壁垒主要来自执行；18–25 数据+场景+结构护城河\n\n"
        "三、商业模式与 Exit 形态（0–20 分）\n"
        "1) 付费是否与真实价值强绑定\n"
        "   - 结果付费 / 效率分成 / usage-based\n"
        "   - 订阅制需面向高价值用户且与生产力/决策权/结果强绑定\n"
        "2) 是否具备被大厂收购或深度集成的潜力\n"
        "   - 作为 feature/module/capability 被嵌入\n"
        "   - 解决大厂做太慢/组织成本过高/认知忽视的问题\n"
        "3) 是否显著服务于 1% 高价值用户\n"
        "   - 用户对 token 成本不敏感\n"
        "   - 显著放大头部用户能力上限\n"
        "   - 停用成本高（停了就“立刻痛”）\n"
        "评分锚点：0–8 传统 SaaS/价值弱绑定；8–15 新定价有独立公司潜力；15–20 价值密度高且 exit 多样\n\n"
        "四、团队与进化能力（0–15 分）\n"
        "1) 创始人是否 1990 年后（若早于 1990，需明确反共识亮点）\n"
        "2) 是否具备暴力学习与快速迭代能力（频繁推翻自己/吸收新范式）\n"
        "3) 是否具备 domain + AI 的复合认知\n"
        "4) 团队背景加分：有华人团队成员；来自大厂/顶级 AI startup 核心员工\n"
        "评分锚点：0–6 传统互联网或经验驱动；6–12 能力扎实但进化一般；12–15 明显 AI 原生进化型团队\n\n"
        "五、加分项（最多 +10）\n"
        "   - 明确的垂类生态或平台潜质（+3）\n"
        "   - 用户交互或界面范式创新（+3）\n"
        "   - 重点关注方向（+4）：Claude Code 产品化/垂直化、Proactive Agent、Agent Infra、极小众但结构性机会赛道\n\n"
        "六、减分项（可叠加）\n"
        "   - 老互联网公司推出的新产品（-10）\n"
        "   - 明显的互联网范式套壳 / Prompt 拼装（-10）\n"
        "   - 创始人 1990 年前且无反共识亮点（-5）\n"
        "   - 当前估值已 >1 亿美元（-5，仅影响投资优先级）\n\n"
        "重要说明：使用 Claude/GPT/Claude Code SDK 不是减分项；真正减分是仍用互联网时代范式理解问题。\n\n"
        "评分要求：\n"
        "- 禁止“平均分”；必须根据材料显著拉开差距。\n"
        "- 若材料信息不足，允许低分并在 reason 中明确“信息不足”。\n"
        "- total 必须等于（ai_native + tech_niche + business + team + bonus - penalty）。"
    )

    user_prompt = (
        f"待评项目/内容：\n{kind}\n\n"
        f"材料（可含描述、关键词、摘要等）：\n{text}\n\n"
        "请输出 JSON，格式示例：\n"
        "{\n"
        '  "total": 72,\n'
        '  "breakdown": {\n'
        '    "ai_native": 22,\n'
        '    "tech_niche": 16,\n'
        '    "business": 14,\n'
        '    "team": 10,\n'
        '    "bonus": 6,\n'
        '    "penalty": 0\n'
        "  },\n"
        '  "reason": "..." \n'
        "}\n"
        "只返回 JSON，不要额外说明。"
    )

    try:
        model_name = _get_model_name()
        kwargs = {
            "model": model_name,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "max_tokens": 900 if _is_gpt5_model(model_name) else 300,
            "temperature": 0.2 if _is_gpt5_model(model_name) else 0.4,
            "response_format": {"type": "json_object"},
            "timeout": _get_timeout(),
        }
        if _is_gpt5_model(model_name):
            kwargs["reasoning_effort"] = "low"

        try:
            response = client.chat.completions.create(**kwargs)
        except TypeError:
            # 兼容不支持 reasoning_effort 的网关
            kwargs.pop("reasoning_effort", None)
            response = client.chat.completions.create(**kwargs)

        content = response.choices[0].message.content
        if content and str(content).strip():
            return _extract_json_object(content)

        # 首次返回为空时再重试一次，放宽为纯文本 JSON 提取。
        retry_kwargs = dict(kwargs)
        retry_kwargs["max_tokens"] = 1400 if _is_gpt5_model(model_name) else 500
        retry_kwargs.pop("response_format", None)
        response = client.chat.completions.create(**retry_kwargs)
        content = response.choices[0].message.content
        return _extract_json_object(content)
    except Exception as e:
        print(f"评分失败: {e}")
        return {
            "total": 0,
            "breakdown": {
                "ai_native": 0,
                "tech_niche": 0,
                "business": 0,
                "team": 0,
                "bonus": 0,
                "penalty": 0,
            },
            "reason": f"scoring failed: {e}",
        }
