import json
import re
from typing import Iterable, List


_BANNED = {
    "ai",
    "人工智能",
    "machine learning",
    "机器学习",
    "keyword",
    "keywords",
    "关键词",
    "N/A",
    "投资",
    "投资回报",
    "商业化",
    "商业化潜力",
    "商业价值",
    "变现",
    "增长渠道",
    "roi",
}

_ENGLISH_WHITELIST = {
    "LLM",
    "RAG",
    "Agent",
    "Multi-Agent",
    "Diffusion",
    "Infra",
    "Agent Infra",
    "OCR",
    "API",
    "SDK",
}

_CANONICAL_MAP = {
    "大语言模型": "LLM",
    "大型语言模型": "LLM",
    "llm": "LLM",
    "检索增强生成": "RAG",
    "rag": "RAG",
    "智能体": "Agent",
    "代理": "Agent",
    "agent": "Agent",
    "agents": "Agent",
    "多智能体": "Multi-Agent",
    "multi-agent": "Multi-Agent",
    "多代理": "Multi-Agent",
    "扩散模型": "Diffusion",
    "diffusion": "Diffusion",
    "基础设施": "Infra",
    "infra": "Infra",
    "agent infra": "Agent Infra",
    "智能体基础设施": "Agent Infra",
}

_FALLBACK_STOPWORDS = {
    "the",
    "and",
    "with",
    "for",
    "from",
    "using",
    "based",
    "that",
    "this",
    "这些",
    "这个",
    "一种",
    "一个",
    "可以",
    "以及",
    "系统",
    "方法",
    "模型",
    "项目",
    "产品",
    "平台",
    "工具",
    "技术",
    "能力",
    "方案",
    "服务",
}


def investor_keyword_prompt(subject: str, title: str, subtitle: str, description: str) -> List[dict]:
    # 保持函数名不变，兼容现有调用方；语义已改为“中性关键词抽取”。
    system = "你是中英技术关键词抽取助手。只返回JSON，不解释。"
    user = (
        f"对象类型: {subject}\n"
        f"名称/标题: {title}\n"
        f"副标题: {subtitle}\n"
        f"描述: {description}\n\n"
        "请输出JSON，格式为: {\"keywords\": [\"...\", \"...\"]}\n"
        "要求:\n"
        "1) 输出8-12个关键词。\n"
        "2) 只基于给定文本，不需要使用预设模板词。\n"
        "3) 优先给定文本中提到的相关实体（产品名称、技术、功能、场景），避免空泛词。\n"
        "4) 同义词只保留一种写法，避免同义重复。\n"
        "5) 英文词尽量少，仅在术语或专有名词必要时使用。\n"
        "6) 不要输出泛词: AI, 人工智能, 机器学习。\n"
        "7) 关键词尽量短，去重。"
    )
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def extract_keywords_from_response(text: str) -> List[str]:
    if not text:
        return []
    parsed = None
    try:
        parsed = json.loads(text)
    except Exception:
        parsed = None
    if isinstance(parsed, dict) and isinstance(parsed.get("keywords"), list):
        return [str(x).strip() for x in parsed["keywords"] if str(x).strip()]
    text = text.replace("，", ",").replace("、", ",").replace("；", ",").replace(";", ",")
    chunks = re.split(r"[,|\n]+", text)
    return [c.strip(" -\t") for c in chunks if c.strip(" -\t")]


def _normalize_term(term: str) -> str:
    t = re.sub(r"\s+", " ", term.strip())
    if not t:
        return ""
    lower = t.lower()
    if lower in _CANONICAL_MAP:
        return _CANONICAL_MAP[lower]
    if t in _CANONICAL_MAP:
        return _CANONICAL_MAP[t]
    return t


def _is_english_token(term: str) -> bool:
    if not term:
        return False
    ascii_letters = sum(ch.isascii() and ch.isalpha() for ch in term)
    return ascii_letters >= max(3, int(len(term) * 0.6))


def _context_candidates(context: str) -> List[str]:
    if not context:
        return []
    text = re.sub(r"https?://\S+", " ", context)
    text = re.sub(r"[_`*#>]", " ", text)
    parts = re.split(r"[\s,，。；;:：/\\|()\[\]{}]+", text)
    out: List[str] = []
    seen = set()
    for raw in parts:
        term = _normalize_term(raw)
        term = term.strip(" .-_\t")
        if not term:
            continue
        if len(term) < 2 or len(term) > 24:
            continue
        lower = term.lower()
        if lower in _BANNED or lower in _FALLBACK_STOPWORDS:
            continue
        if re.fullmatch(r"[0-9.]+", term):
            continue
        key = lower
        if key in seen:
            continue
        seen.add(key)
        out.append(term)
    return out


def finalize_keywords(
    raw_keywords: Iterable[str],
    context: str,
    source: str,
    min_items: int = 8,
    max_items: int = 12,
) -> List[str]:
    cleaned: List[str] = []
    seen = set()

    for k in raw_keywords:
        term = _normalize_term(str(k))
        if not term:
            continue
        if term.lower() in _BANNED:
            continue
        key = term.lower()
        if key in seen:
            continue
        seen.add(key)
        cleaned.append(term)

    # 基于上下文补充候选，但不引入任何固定模板词，避免频率偏置。
    if len(cleaned) < min_items:
        for tag in _context_candidates(context):
            key = tag.lower()
            if key not in seen:
                seen.add(key)
                cleaned.append(tag)
            if len(cleaned) >= min_items:
                break

    # 控制英文术语数量和白名单
    english_count = 0
    filtered: List[str] = []
    deferred_english: List[str] = []
    for term in cleaned:
        if _is_english_token(term):
            if term not in _ENGLISH_WHITELIST:
                deferred_english.append(term)
                continue
            if english_count >= 3:
                continue
            english_count += 1
        filtered.append(term)

    cleaned = filtered

    # 最终兜底：再从上下文取词，仍不注入模板词。
    if len(cleaned) < min_items:
        more = _context_candidates(context)
        known = {x.lower() for x in cleaned}
        for term in more:
            if term.lower() not in known:
                cleaned.append(term)
                known.add(term.lower())
            if len(cleaned) >= min_items:
                break

    # 最后兜底：若仍不足，补少量非白名单英文（避免只剩 1-2 个词）。
    if len(cleaned) < min_items and deferred_english:
        known = {x.lower() for x in cleaned}
        english_now = sum(1 for t in cleaned if _is_english_token(t))
        for term in deferred_english:
            if term.lower() in known:
                continue
            if english_now >= 5:
                break
            cleaned.append(term)
            known.add(term.lower())
            english_now += 1
            if len(cleaned) >= min_items:
                break

    return cleaned[:max_items]
