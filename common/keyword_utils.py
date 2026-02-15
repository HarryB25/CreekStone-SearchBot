import json
import re
from typing import Iterable, List, Tuple


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
    "title",
    "description",
    "readme",
    "abstract",
    "tags",
    "source",
    "标题",
    "描述",
    "摘要",
    "仓库",
    "标签",
    "来源",
    "create",
    "your",
    "you",
    "with",
    "from",
    "for",
    "into",
    "the",
    "and",
    "in",
    "on",
    "to",
    "by",
    "is",
    "are",
    "github",
    "readme",
    "repo",
    "repository",
    "仓库",
    "开源仓库",
    "开源项目",
    "描述与readme",
    "readme摘录",
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
    "llms": "LLM",
    "检索增强生成": "RAG",
    "rag": "RAG",
    "rag pipeline": "RAG",
    "智能体": "Agent",
    "代理": "Agent",
    "agent": "Agent",
    "agents": "Agent",
    "tool use": "tool-use",
    "tool-use": "tool-use",
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
}

_PRODUCT_CUES = {
    "agent",
    "workflow",
    "copilot",
    "mcp",
    "api",
    "sdk",
    "cli",
    "ocr",
    "rag",
    "llm",
    "infra",
    "自动化",
    "工作流",
    "智能体",
    "多智能体",
    "代理",
    "检索增强",
    "向量数据库",
    "代码生成",
    "代码审查",
    "调试",
    "监控",
    "翻译",
    "摘要",
    "大纲",
    "笔记",
    "文档处理",
    "语音转写",
    "视频生成",
    "图像生成",
    "会议助手",
    "客服",
    "营销",
    "销售",
    "教育",
    "医疗",
    "金融",
    "招聘",
    "时间管理",
    "专注",
    "情绪追踪",
    "安全",
    "隐私",
}

_PHRASE_NOISE_PREFIX = (
    "我们",
    "你",
    "这款",
    "这个",
    "那款",
    "借助",
    "轻松",
    "让你",
    "让我们",
)

_SENTENCE_CUE_RE = re.compile(
    r"(我们|你|我|他|她|它|谁|什么|怎么|为何|如果|例如|比如|这款|这个|能够|可以|帮助|用于|通过|支持|让|使|将|会|专为|面向|打造|推出|适合|了解|发现|理解|成为|带来|提供|并且|而且|以及|并|结果|过去|遇到|打开|加入|进行|用统计|用)",
    re.IGNORECASE,
)

_GENERIC_CN = {
    "高级",
    "简单",
    "好用",
    "应用",
    "工具",
    "平台",
    "产品",
    "功能",
    "内容",
    "系统",
    "模型",
    "方案",
    "能力",
    "效率",
    "体验",
    "支持",
}

_BAD_SUFFIX_CN = {"情况", "方式", "功能", "信息", "内容", "结果", "时候", "东西", "应用"}
_CN_CONCEPT_RE = re.compile(
    r"([\u4e00-\u9fff]{1,8}(管理|安排|提醒|统计|追踪|导览|音频|视频|图像|情绪|专注|笔记|大纲|翻译|转写|自动化|工作流|助手|规划|分析|生成|搜索|监控|调试|安全|隐私|数据库|引擎|框架|协议|插件|系统))"
)
_LEADING_CLEAN_RE = re.compile(r"^(无论是|还是|都很|并且|以及|可以|能够|支持|帮助|用于|通过|让|将|把|从)")
_LEADING_VERB_RE = re.compile(r"^(整理|梳理|创建|生成|做|制定|查看|导出|追踪|发现|理解)")


def investor_keyword_prompt(subject: str, title: str, subtitle: str, description: str) -> List[dict]:
    # 保持函数名不变，兼容现有调用方；语义升级为“趋势分析关键词抽取”。
    source_map = {
        "Open Source Repository": "github",
        "Research Paper": "arxiv",
        "Product": "producthunt",
    }
    source = source_map.get(subject, "other")
    system = (
        "你是“AI 产品/项目/论文”的关键词抽取器。"
        "目标是提取可用于长期趋势分析的关键词。"
        "关键词必须可聚合、可比较、尽量规范化，并减少噪声词。"
        "你可以在内部完成分类、同义词合并、去噪与权重判断，但最终只输出简洁JSON。"
    )
    user = (
        "输入如下:\n"
        f"- source: {source}\n"
        f"- title: {title}\n"
        f"- description: {description}\n"
        f"- tags: {subtitle}\n"
        f"- readme_or_abstract: {description}\n"
        "- optional_fields: {}\n\n"
        "抽取规则:\n"
        "1) 先理解核心：解决什么问题、面向什么场景、采用什么技术。\n"
        "2) 关键词优先选择可横向比较的概念词，通常1-3词，避免句子化。\n"
        "3) 规范化：统一命名与大小写，合并近义词（如 LLMs->LLM，tool use->tool-use）。\n"
        "4) 去噪：过滤过泛词（AI、machine learning、platform、solution等）、营销词、纯品牌词、版本号。\n"
        "5) source偏好:\n"
        "   - arxiv: 优先任务/方法/评测框架\n"
        "   - github: 优先系统形态/实现技术/生态集成\n"
        "   - producthunt: 优先产品形态/使用场景/差异化技术\n"
        "6) 输出8-12个关键词；信息不足时允许最少6个，但必须准确。\n\n"
        "7) 强约束:\n"
        "   - 不要输出字段名（source/title/description/tags/readme/abstract 及其中英文）。\n"
        "   - 不要输出停用词（如 in/on/to/by/is/and/the/create/your 等）。\n"
        "   - 不要拆成无意义碎片词；优先 1-3 词的概念短语。\n"
        "   - 中文优先，仅保留必要英文术语（例如 LLM/RAG/Agent/MCP/API/SDK）。\n\n"
        "最终只输出JSON，格式必须是:\n"
        "{\"keywords\": [\"kw1\", \"kw2\", \"...\"]}\n"
        "不要输出其他字段，不要Markdown。"
    )
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def investor_keyword_repair_prompt(
    subject: str,
    title: str,
    subtitle: str,
    description: str,
    bad_keywords: Iterable[str],
    reason: str,
) -> List[dict]:
    source_map = {
        "Open Source Repository": "github",
        "Research Paper": "arxiv",
        "Product": "producthunt",
    }
    source = source_map.get(subject, "other")
    bad = ", ".join([str(x).strip() for x in bad_keywords if str(x).strip()][:20])
    system = (
        "你是关键词纠偏器。"
        "上一版关键词存在质量问题，请重新输出高质量关键词。"
        "只输出JSON，不解释。"
    )
    user = (
        f"source: {source}\n"
        f"title: {title}\n"
        f"subtitle/tags: {subtitle}\n"
        f"description: {description}\n"
        f"上一版关键词: {bad}\n"
        f"问题: {reason}\n\n"
        "纠偏要求:\n"
        "1) 关键词必须是可聚合概念，不要标题拆词，不要句子碎片。\n"
        "2) 中文优先；仅保留必要英文术语（LLM/RAG/Agent/MCP/API/SDK等）。\n"
        "3) 8-12个关键词，覆盖 技术方法 + 应用场景 + 产品形态。\n"
        "4) 严禁输出字段名、停用词、营销词、纯品牌词。\n\n"
        "只输出JSON: {\"keywords\": [\"...\", \"...\"]}"
    )
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def extract_keywords_from_response(text: str) -> List[str]:
    if not text:
        return []
    parsed = None
    try:
        parsed = json.loads(text)
    except Exception:
        start = text.find("{")
        end = text.rfind("}")
        if start >= 0 and end > start:
            try:
                parsed = json.loads(text[start : end + 1])
            except Exception:
                parsed = None
        else:
            parsed = None
    if isinstance(parsed, dict) and isinstance(parsed.get("keywords"), list):
        out: List[str] = []
        for x in parsed["keywords"]:
            if isinstance(x, dict):
                term = str(x.get("term", "")).strip()
                if term:
                    out.append(term)
            else:
                term = str(x).strip()
                if term:
                    out.append(term)
        if out:
            return out
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


def _english_word_like(term: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z][A-Za-z0-9' -]{1,32}", term or ""))


def _has_chinese(term: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", term or ""))


def _normalize_cn_phrase(term: str) -> str:
    t = (term or "").strip()
    if not t:
        return ""
    prev = None
    while t and t != prev:
        prev = t
        t = _LEADING_CLEAN_RE.sub("", t).strip()
        t = _LEADING_VERB_RE.sub("", t).strip()
    if "的" in t:
        t = t.split("的")[-1].strip()
    return t


def _looks_sentence_like(term: str) -> bool:
    t = (term or "").strip()
    if not t:
        return True
    if len(t) > 16:
        return True
    if re.search(r"[，。！？；;:：。,.!?]", t):
        return True
    if any(t.endswith(suf) for suf in _BAD_SUFFIX_CN):
        return True
    if _SENTENCE_CUE_RE.search(t):
        return True
    if t[:1] in {"从", "对", "将", "把", "在", "用", "按", "于", "向"} and len(t) >= 3:
        return True
    if t.startswith(_PHRASE_NOISE_PREFIX):
        return True
    if _english_word_like(t):
        words = [x for x in t.split() if x]
        if len(words) >= 4:
            return True
    return False


def synthesize_keywords_from_context(context: str, source: str, max_items: int = 10) -> List[str]:
    """Deterministic fallback to avoid sentence-like or title-fragment keywords."""
    if not context:
        return []

    out: List[str] = []
    seen = set()

    if source == "producthunt":
        text = context.replace("\r", "\n")
        segments = re.split(r"[。！？；;:\n•]+", text)
        split_re = re.compile(r"(?:，|、|及|和|并|与|或|用于|帮助|支持|通过|让|使|可以|能够|专为|面向|打造|提供|实现|以及)")
        for seg in segments:
            s = seg.strip(" \t-_*")
            if not s:
                continue
                for part in split_re.split(s):
                    cand = _normalize_cn_phrase(part.strip(" \t-_*"))
                    if not cand:
                        continue
                    if not cand:
                        continue
                    if _looks_sentence_like(cand):
                        continue
                    if len(cand) < 2 or len(cand) > 10:
                        continue
                low = cand.lower()
                hit_cue = any(cue in low for cue in _PRODUCT_CUES) or any(cue in cand for cue in _PRODUCT_CUES)
                if not hit_cue:
                    continue
                if low in seen:
                    continue
                seen.add(low)
                out.append(cand)
                if len(out) >= max_items:
                    break
            if len(out) >= max_items:
                break
        if len(out) < max_items:
            for seg in segments:
                s = seg.strip(" \t-_*")
                if not s:
                    continue
                for part in split_re.split(s):
                    cand = _normalize_cn_phrase(part.strip(" \t-_*"))
                    if not cand:
                        continue
                    if _looks_sentence_like(cand):
                        continue
                    if not _has_chinese(cand):
                        continue
                    if len(cand) < 2 or len(cand) > 8:
                        continue
                    if cand in _GENERIC_CN:
                        continue
                    if "的" in cand:
                        continue
                    low = cand.lower()
                    if low in seen:
                        continue
                    seen.add(low)
                    out.append(cand)
                    if len(out) >= max_items:
                        break
                if len(out) >= max_items:
                    break
        if len(out) < max_items:
            for token in _ENGLISH_WHITELIST:
                if token.lower() in text.lower() and token.lower() not in seen:
                    seen.add(token.lower())
                    out.append(token)
                if len(out) >= max_items:
                    break
        if len(out) < max_items:
            for m in _CN_CONCEPT_RE.finditer(text):
                cand = _normalize_cn_phrase((m.group(1) or "").strip())
                if not cand:
                    continue
                if _looks_sentence_like(cand):
                    continue
                if len(cand) < 2 or len(cand) > 10:
                    continue
                if cand in _GENERIC_CN:
                    continue
                low = cand.lower()
                if low in seen:
                    continue
                seen.add(low)
                out.append(cand)
                if len(out) >= max_items:
                    break

    # Keep only clean tokens after synthesis.
    cleaned = finalize_keywords(out, context, source=source, min_items=6 if source == "producthunt" else 8, max_items=max_items)
    return cleaned[:max_items]


def keyword_quality_check(keywords: Iterable[str], context: str, source: str) -> Tuple[bool, str]:
    items = [str(x).strip() for x in keywords if str(x).strip()]
    min_required = 4 if source == "producthunt" else 6
    if len(items) < min_required:
        return False, "too_few_keywords"

    lines = [ln.strip() for ln in context.splitlines() if ln.strip()]
    title_line = lines[0] if lines else ""
    title_tokens = set(t.lower() for t in re.findall(r"[A-Za-z][A-Za-z0-9']{1,20}", title_line))

    title_overlap = 0
    english_non_whitelist = 0
    noisy_count = 0
    sentence_like_count = 0
    for term in items:
        lower = term.lower()
        if lower in _BANNED:
            noisy_count += 1
            continue
        if _looks_sentence_like(term):
            sentence_like_count += 1
            continue
        if _english_word_like(term):
            token = lower.strip()
            if token in title_tokens:
                title_overlap += 1
            if term not in _ENGLISH_WHITELIST:
                english_non_whitelist += 1
        if len(term) <= 2 and term.upper() not in {"AI", "LLM", "RAG", "API", "SDK", "MCP", "CI", "CD"}:
            noisy_count += 1

    n = len(items)
    if noisy_count > 0:
        return False, "contains_noisy_tokens"
    if source == "producthunt" and sentence_like_count > 0:
        return False, "contains_sentence_phrases"
    if source != "producthunt" and sentence_like_count >= max(2, n // 3):
        return False, "too_many_sentence_phrases"
    if source == "producthunt":
        if title_overlap >= max(3, n // 2):
            return False, "title_fragment_pollution"
        if english_non_whitelist >= max(3, int(n * 0.4)):
            return False, "english_fragment_pollution"
    return True, "ok"


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
        if re.search(r"[，。！？；;:：]", term):
            continue
        if term.startswith(_PHRASE_NOISE_PREFIX):
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
    target_min = 6 if source == "producthunt" else min_items
    cleaned: List[str] = []
    seen = set()
    lines = [ln.strip() for ln in context.splitlines() if ln.strip()]
    title_line = lines[0] if lines else ""
    subtitle_line = lines[1] if len(lines) > 1 else ""
    title_tokens = set(t.lower() for t in re.findall(r"[A-Za-z][A-Za-z0-9']{1,20}", title_line))
    subtitle_tokens = set(t.lower() for t in re.findall(r"[A-Za-z][A-Za-z0-9']{1,20}", subtitle_line))

    for k in raw_keywords:
        term = _normalize_term(str(k))
        if not term:
            continue
        term = term.strip("\"'`[](){}:;,.!?<>")
        if not term:
            continue
        if term.lower() in _BANNED:
            continue
        if source == "github":
            low_term = term.lower()
            if (
                "readme" in low_term
                or "github" in low_term
                or "repository" in low_term
                or term in {"仓库", "开源仓库", "开源项目", "描述与README", "README摘录"}
            ):
                continue
        # 过滤明显无信息量的纯英文停用词/连接词
        if re.fullmatch(r"[A-Za-z]{1,12}", term) and term.lower() in _BANNED:
            continue
        # 过滤疑似“字段名 + 冒号”残留
        if term.endswith(":"):
            continue
        # 过滤极短碎片（保留常见缩写）
        if len(term) <= 2 and term.upper() not in {"AI", "LLM", "CI", "CD"}:
            continue
        if len(term) > 20:
            continue
        if _looks_sentence_like(term):
            continue
        if re.search(r"[，。！？；;:：]", term):
            continue
        if term.startswith(_PHRASE_NOISE_PREFIX):
            continue
        if source == "producthunt" and _is_english_token(term):
            lower = term.lower()
            # 产品名/标语切词与常见英文碎词直接过滤
            if lower in title_tokens or lower in subtitle_tokens:
                continue
            if lower in {"app", "new", "launch", "launching", "we", "ve", "all", "been", "there"}:
                continue
            # Product Hunt 默认不接受非白名单英文单词级关键词
            if term not in _ENGLISH_WHITELIST and re.fullmatch(r"[A-Za-z][A-Za-z0-9' -]{1,24}", term):
                continue
        key = term.lower()
        if key in seen:
            continue
        seen.add(key)
        cleaned.append(term)

    # 基于上下文补充候选，但不引入任何固定模板词，避免频率偏置。
    if len(cleaned) < target_min and source != "producthunt":
        for tag in _context_candidates(context):
            key = tag.lower()
            if key not in seen:
                seen.add(key)
                cleaned.append(tag)
            if len(cleaned) >= target_min:
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
    if len(cleaned) < target_min and source != "producthunt":
        more = _context_candidates(context)
        known = {x.lower() for x in cleaned}
        for term in more:
            if term.lower() not in known:
                cleaned.append(term)
                known.add(term.lower())
            if len(cleaned) >= target_min:
                break

    # 最后兜底：若仍不足，补少量非白名单英文（避免只剩 1-2 个词）。
    if len(cleaned) < target_min and deferred_english and source != "producthunt":
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
            if len(cleaned) >= target_min:
                break

    # Product Hunt: 在所有兜底后再做一次严格形态约束，避免句子词回流。
    if source == "producthunt":
        strict: List[str] = []
        strict_seen = set()
        for term in cleaned:
            low = term.lower()
            if _is_english_token(term):
                if term not in _ENGLISH_WHITELIST:
                    continue
                if low in strict_seen:
                    continue
                strict_seen.add(low)
                strict.append(term)
                continue
            if not _has_chinese(term):
                continue
            if len(term) < 2 or len(term) > 10:
                continue
            if "的" in term:
                continue
            if term in _GENERIC_CN:
                continue
            if re.search(r"(我们|你|这款|这个|能够|可以|让|推出|面向|专为|通过|支持|帮助|打造|更像|真正|就是|一下)", term):
                continue
            if low in strict_seen:
                continue
            strict_seen.add(low)
            strict.append(term)
        cleaned = strict

    return cleaned[:max_items]
