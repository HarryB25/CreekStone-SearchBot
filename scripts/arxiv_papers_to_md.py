import os
import time
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("dotenv 模块未安装，将直接使用环境变量")

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from datetime import datetime, timezone, timedelta
import openai
import json
from typing import List, Dict
from common.storage import save_structured_items, build_item_id
from common.scoring import score_content
from common.openai_fallback import chat_completion_content, get_openai_timeout, is_gpt5_model
from common.keyword_utils import (
    investor_keyword_prompt,
    investor_keyword_repair_prompt,
    extract_keywords_from_response,
    finalize_keywords,
    keyword_quality_check,
    synthesize_keywords_from_context,
)

# AI 过滤关键词（用于后处理保护，一般已由分类过滤）
AI_KEYWORDS = [
    'ai', 'artificial intelligence', 'machine learning', 'ml',
    'deep learning', 'neural network', 'llm', 'gpt', 'claude',
    'agent', 'autonomous', 'chatbot', 'assistant', 'copilot',
    'generative', 'diffusion', 'transformer', 'embedding',
    'rag', 'retrieval', 'vector', 'semantic search',
    'proactive ai', 'agent infra', 'autonomous agents', 'multi-agent', 'openclaw', 'mcp',
    'context', 'hijacking', 'laude code sdk', 'cowork', 'vibe coding', 'agent-friendly tooling',
    'human-in-the-loop', 'online learning', 'reward model', 'reward fine-tune', 'sft', 'rlhf',
    'rlaif', 'dpo', 'hero user', 'product self-iteration', 'intent prediction', 'non-consensus ai',
    'ai-density', 'agentic workflow', 'workflow'
]

EXCLUDE_KEYWORDS = [
    'crypto', 'nft', 'blockchain', 'web3', 'token',
    'game', 'gaming', 'casino', 'betting',
    'adult', 'dating', 'porn'
]

def _allow_mock_data() -> bool:
    return os.getenv("ALLOW_MOCK_DATA", "").strip().lower() == "true"


def _build_retry_session() -> requests.Session:
    """构建带重试策略的会话，降低 arXiv 分页过程中的临时网络错误影响。"""
    retry = Retry(
        total=3,
        connect=3,
        read=3,
        backoff_factor=1.0,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["GET"],
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session = requests.Session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

def _get_int_env(name: str, default: int) -> int:
    raw = os.getenv(name)
    if raw is None or raw.strip() == "":
        return default
    try:
        value = int(raw)
    except ValueError:
        print(f"警告: 环境变量 {name}={raw!r} 不是整数，回退默认值 {default}")
        return default
    if value <= 0:
        print(f"警告: 环境变量 {name}={raw!r} 必须大于 0，回退默认值 {default}")
        return default
    return value


def _get_request_timeout() -> float:
    return get_openai_timeout(60.0)


def _get_model_name() -> str:
    raw = os.getenv("OPENAI_MODEL", "").strip()
    return raw or "gpt-5.2-2025-12-11"


def _chat_json_content(messages, max_tokens: int, temperature: float) -> str:
    model_name = _get_model_name()
    content, used_model = chat_completion_content(
        client=client,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
        json_mode=True,
        default_model=model_name,
        timeout=_get_request_timeout(),
        retry_max_tokens=max(max_tokens, 1200 if is_gpt5_model(model_name) else 300),
    )
    if used_model != model_name:
        print(f"模型回退: {model_name} -> {used_model}")
    return content


def _get_base_url(default: str = "https://api.openai.com/v1") -> str:
    raw = os.getenv("OPENAI_BASE_URL")
    if raw is None or raw.strip() == "":
        return default
    return raw.strip()


def _contains_any(text: str, keywords) -> bool:
    if not text:
        return False
    lowered = text.lower()
    return any(k in lowered for k in keywords)


def is_ai_related(*fields: str) -> bool:
    merged = " ".join(filter(None, fields))
    if not merged:
        return False
    if _contains_any(merged, EXCLUDE_KEYWORDS):
        return False
    return _contains_any(merged, AI_KEYWORDS)

# 创建 OpenAI 客户端实例
api_key = os.getenv('OPENAI_API_KEY')
base_url = _get_base_url()
if not api_key:
    print("警告: 未设置 OPENAI_API_KEY 环境变量")
    client = None
else:
    try:
        client = openai.Client(api_key=api_key, base_url=base_url)
        print(f"成功初始化 OpenAI 客户端 (使用API地址: {base_url})")
    except Exception as e:
        print(f"初始化 OpenAI 客户端失败: {e}")
        client = None

class ArxivPaper:
    def __init__(self, entry):
        """从arXiv API返回的entry初始化论文对象"""
        self.id = entry.get('id', '').split('/')[-1]
        self.title = entry.get('title', '').replace('\n', ' ').strip()
        authors_raw = entry.get('author', [])
        if isinstance(authors_raw, dict):
            authors_raw = [authors_raw]
        elif isinstance(authors_raw, str):
            authors_raw = [{"name": authors_raw}]
        self.authors = []
        for author in authors_raw:
            if isinstance(author, dict):
                name = str(author.get('name', '')).strip()
            else:
                name = str(author).strip()
            if name:
                self.authors.append(name)
        self.summary = entry.get('summary', '').replace('\n', ' ').strip()
        self.published = entry.get('published', '')
        self.url = f"https://arxiv.org/abs/{self.id}"
        self.pdf_url = f"https://arxiv.org/pdf/{self.id}.pdf"
        
        # 提取分类
        categories = entry.get('category', [])
        if isinstance(categories, dict):
            categories = [categories]
        elif isinstance(categories, str):
            categories = [{"@term": categories}]
        self.categories = []
        for cat in categories:
            if isinstance(cat, dict):
                term = str(cat.get('@term', '')).strip()
            else:
                term = str(cat).strip()
            if term:
                self.categories.append(term)
        
        # AI增强字段
        self.ai_summary = self.generate_ai_summary()
        self.keywords = self.generate_keywords()
        self.published_at = entry.get('published', '')
        self.score = score_content(
            f"标题: {self.title}\n摘要: {self.summary}\nAI总结: {self.ai_summary}\n关键词: {self.keywords}",
            client,
            kind="arxiv",
        )

    def generate_keywords(self) -> str:
        """为论文生成中性关键词：贴合内容，术语统一，减少英文噪音。"""
        try:
            base_text = f"标题: {self.title}\n摘要: {self.summary}"
            if client is None:
                words = (self.title + ", " + self.summary).replace("&", ",").replace("|", ",").replace("-", ",").split(",")
                filtered = finalize_keywords([w.strip() for w in words if w.strip()], base_text, source="arxiv")
                ok, _ = keyword_quality_check(filtered, base_text, source="arxiv")
                if not ok:
                    filtered = synthesize_keywords_from_context(base_text, source="arxiv", max_items=10)
                return ", ".join(filtered)

            raw = _chat_json_content(
                messages=investor_keyword_prompt(
                    subject="Research Paper",
                    title=self.title,
                    subtitle=", ".join(self.categories[:3]),
                    description=self.summary,
                ),
                max_tokens=1200 if is_gpt5_model(_get_model_name()) else 220,
                temperature=0.3,
            )
            items = extract_keywords_from_response(raw)
            items = finalize_keywords(items, base_text, source="arxiv")
            ok, reason = keyword_quality_check(items, base_text, source="arxiv")
            if not ok:
                repaired_raw = _chat_json_content(
                    messages=investor_keyword_repair_prompt(
                        subject="Research Paper",
                        title=self.title,
                        subtitle=", ".join(self.categories[:3]),
                        description=self.summary,
                        bad_keywords=items,
                        reason=reason,
                    ),
                    max_tokens=1000 if is_gpt5_model(_get_model_name()) else 220,
                    temperature=0.2,
                )
                repaired = extract_keywords_from_response(repaired_raw)
                repaired = finalize_keywords(repaired, base_text, source="arxiv")
                repaired_ok, _ = keyword_quality_check(repaired, base_text, source="arxiv")
                if repaired_ok:
                    items = repaired
                else:
                    items = synthesize_keywords_from_context(base_text, source="arxiv", max_items=10)
            if not items:
                items = synthesize_keywords_from_context(base_text, source="arxiv", max_items=10)
            return ", ".join(dict.fromkeys(items))
        except Exception as e:
            print(f"关键词生成失败: {e}")
            fallback = finalize_keywords([self.title, self.summary], f"{self.title}\n{self.summary}", source="arxiv")
            ok, _ = keyword_quality_check(fallback, base_text, source="arxiv")
            if not ok:
                fallback = synthesize_keywords_from_context(base_text, source="arxiv", max_items=10)
            return ", ".join(fallback)
    
    def generate_ai_summary(self) -> Dict[str, str]:
        """使用AI生成结构化摘要"""
        if client is None:
            return {
                "tldr": self.summary[:200] + "...",
                "motivation": "AI服务不可用",
                "method": "AI服务不可用",
                "conclusion": "AI服务不可用"
            }

        prompt = f"""请分析以下AI论文并用中文提供结构化总结（若检测到任何 EXCLUDE_KEYWORDS 则回答 "跳过"）：

标题: {self.title}

摘要: {self.summary}

请提供以下四个方面的分析（每个方面用简洁的1-2句话概括）：
1. TLDR（一句话总结）
2. 研究动机（Motivation）
3. 核心方法（Method）
4. 主要结论（Conclusion）

请用JSON格式返回，格式如下：
{{"tldr": "...", "motivation": "...", "method": "...", "conclusion": "..."}}
"""
        
        try:
            print(f"正在为论文 {self.title[:50]}... 生成AI摘要")
            content = _chat_json_content(
                messages=[
                    {"role": "system", "content": "你是一位专业的AI研究论文分析专家，擅长用简洁的中文总结论文要点。"},
                    {"role": "user", "content": prompt + "\nAI_KEYWORDS: " + ", ".join(AI_KEYWORDS) + "\nEXCLUDE_KEYWORDS: " + ", ".join(EXCLUDE_KEYWORDS)}
                ],
                max_tokens=1800 if is_gpt5_model(_get_model_name()) else 800,
                temperature=0.7,
            )

            result = json.loads(content)
            print(f"成功生成AI摘要")
            return result
            
        except Exception as e:
            print(f"AI摘要生成失败: {e}")
            return {
                "tldr": self.summary[:200] + "...",
                "motivation": "自动分析失败，请查看原文",
                "method": "自动分析失败，请查看原文",
                "conclusion": "自动分析失败，请查看原文"
            }
    
    def to_markdown(self, rank: int) -> str:
        """转换为Markdown格式"""
        authors_str = ", ".join(self.authors[:3])
        if len(self.authors) > 3:
            authors_str += f" 等 {len(self.authors)} 位作者"
        
        categories_str = ", ".join(self.categories)
        
        return f"""## [{rank}. {self.title}]({self.url})

**作者**：{authors_str}  
**分类**：{categories_str}  
**发布时间**：{self.published[:10]}

### 📄 论文摘要

{self.summary}

### 🤖 AI 总结

**一句话总结**：{self.ai_summary.get('tldr', 'N/A')}

**研究动机**：{self.ai_summary.get('motivation', 'N/A')}

**核心方法**：{self.ai_summary.get('method', 'N/A')}

**主要结论**：{self.ai_summary.get('conclusion', 'N/A')}

**关键词**：{self.keywords}

**评分**：{self.score.get('total', 0)}

**论文链接**：[查看原文]({self.url}) | [下载PDF]({self.pdf_url})

---

"""

    def to_content_item(self, rank: int, date_str: str) -> dict:
        merged = f"{self.title} {self.summary}".lower()
        hit_keywords = [kw for kw in AI_KEYWORDS if kw in merged]
        return {
            "id": build_item_id("ax", date_str, rank),
            "source": "arxiv",
            "date": date_str,
            "rank": rank,
            "title": self.title,
            "url": self.url,
            "detail_url": self.pdf_url,
            "description_en": self.summary,
            "description_zh": self.ai_summary.get('tldr', ''),
            "keywords": [k.strip() for k in self.keywords.split(",") if k.strip()],
            "tags": self.categories,
            "metrics": {"authors": self.authors},
            "media": {"image": None},
            "ai_flags": {"is_ai": True, "hit_keywords": hit_keywords, "hit_excludes": []},
            "score": self.score,
            "raw": {
                "published": self.published_at,
                "ai_summary": self.ai_summary,
            },
        }

def fetch_arxiv_papers(
    categories: List[str] = None,
    max_results: int = 10,
    target_date: str = "",
) -> List[ArxivPaper]:
    """从arXiv API获取最新论文"""
    if categories is None:
        categories = ['cs.AI', 'cs.LG', 'cs.CL', 'cs.CV']
    
    # 构建查询
    category_query = ' OR '.join([f'cat:{cat}' for cat in categories])
    
    # arXiv API endpoint
    base_url = 'http://export.arxiv.org/api/query'
    
    # 获取最近7天窗口，可通过 target_date 固定窗口终点；
    # 当给定 target_date 时，优先用 submittedDate 精确过滤当天，避免深分页触发限流。
    strict_day_mode = False
    target_day_dt = None
    if target_date:
        try:
            target_day_dt = datetime.strptime(target_date, '%Y-%m-%d').replace(tzinfo=timezone.utc)
            end_date = target_day_dt + timedelta(days=1)
            strict_day_mode = True
        except ValueError:
            print(f"警告: ARXIV_TARGET_DATE={target_date!r} 格式无效，回退到当前日期窗口")
            end_date = datetime.now(timezone.utc)
    else:
        end_date = datetime.now(timezone.utc)
    start_date = end_date - timedelta(days=1 if strict_day_mode else 7)

    search_query = category_query
    if strict_day_mode and target_day_dt is not None:
        day_token = target_day_dt.strftime('%Y%m%d')
        search_query = (
            f"({category_query}) AND "
            f"submittedDate:[{day_token}0000 TO {day_token}2359]"
        )
    
    # 历史回填时不能只抓第一页；需要分页向后翻，直到覆盖目标窗口。
    batch_size = max(100, max_results * 4)
    batch_size = min(batch_size, 200)
    max_pages = _get_int_env("ARXIV_MAX_PAGES", 30)
    if strict_day_mode:
        max_pages = min(max_pages, 8)
    page_sleep = float(os.getenv("ARXIV_PAGE_SLEEP", "0.35") or "0.35")
    
    print(f"正在从arXiv获取论文...")
    print(f"查询分类: {', '.join(categories)}")
    print(f"目标数量: {max_results}")
    
    try:
        import xmltodict
        session = _build_retry_session()

        # 过滤最近7天的论文（且不超过目标日期）
        recent_entries = []
        cutoff_date = start_date.strftime('%Y-%m-%d')
        upper_date = (end_date - timedelta(days=1)).strftime('%Y-%m-%d')

        start_idx = 0
        page = 0
        while page < max_pages:
            params = {
                'search_query': search_query,
                'start': start_idx,
                'max_results': batch_size,
                'sortBy': 'submittedDate',
                'sortOrder': 'descending',
            }
            response = None
            for attempt in range(1, 6):
                response = session.get(base_url, params=params, timeout=30)
                if response.status_code == 429:
                    wait_seconds = min(30.0, 1.5 * (2 ** (attempt - 1)))
                    print(
                        f"arXiv 限流(429)，第 {attempt}/5 次重试，"
                        f"等待 {wait_seconds:.1f}s 后继续..."
                    )
                    time.sleep(wait_seconds)
                    continue
                response.raise_for_status()
                break
            if response is None:
                raise RuntimeError("arXiv 请求失败: 未收到有效响应")
            if response.status_code == 429:
                raise RuntimeError("arXiv 请求失败: 连续 5 次触发限流(429)")
            data = xmltodict.parse(response.text)
            entries = data.get('feed', {}).get('entry', [])
            if isinstance(entries, dict):
                entries = [entries]
            if not entries:
                break

            page += 1
            page_days = []
            for entry in entries:
                published_day = str(entry.get('published', ''))[:10]
                if published_day:
                    page_days.append(published_day)
                if cutoff_date <= published_day <= upper_date:
                    recent_entries.append(entry)

            if page_days:
                newest_day = max(page_days)
                oldest_day = min(page_days)
                print(
                    f"第 {page} 页: {len(entries)} 篇, 日期区间 {oldest_day} ~ {newest_day}, "
                    f"窗口命中累计 {len(recent_entries)}"
                )
                # 该页最旧日期已经早于窗口下界，后续只会更旧，可以停止。
                if oldest_day < cutoff_date:
                    break

            # 安全限制：窗口命中足够多时提前停止。
            if len(recent_entries) >= max_results * 8:
                break

            start_idx += len(entries)
            if page_sleep > 0:
                time.sleep(page_sleep)

        print(f"最近7天的论文: {len(recent_entries)} 篇")

        if not recent_entries:
            if _allow_mock_data():
                print("未找到窗口内论文，ALLOW_MOCK_DATA=true，使用模拟数据...")
                return fetch_mock_papers()
            raise RuntimeError(
                f"未找到 {cutoff_date}~{upper_date} 的论文；"
                "请增大 ARXIV_MAX_PAGES 或检查目标日期。"
            )
        
        # 关键：筛选主分类在目标分类列表中的论文，并再做一次关键词过滤
        target_categories_set = set(categories)
        filtered_papers = []

        for entry in recent_entries:
            try:
                # 提取论文的所有分类
                cats = entry.get('category', [])
                if not cats:
                    continue
                
                if isinstance(cats, dict):
                    cats = [cats]
                elif isinstance(cats, str):
                    # 如果是字符串，跳过这个entry
                    continue
                
                paper_categories = [cat.get('@term', '') if isinstance(cat, dict) else str(cat) for cat in cats]
                
                # 检查主分类（第一个分类）是否在目标分类列表中
                if paper_categories and paper_categories[0] in target_categories_set:
                    title = entry.get('title', '')
                    summary = entry.get('summary', '')
                    if not is_ai_related(title, summary):
                        print(f"跳过非AI论文: {title[:40]}...")
                        continue
                    filtered_papers.append(ArxivPaper(entry))
                    if len(filtered_papers) >= max_results:
                        break
            except Exception as e:
                print(f"处理论文时出错，跳过: {e}")
                continue
        
        if not filtered_papers:
            if _allow_mock_data():
                print("筛选后没有符合条件的AI论文，ALLOW_MOCK_DATA=true，使用模拟数据")
                return fetch_mock_papers()
            raise RuntimeError("筛选后没有符合条件的AI论文，且未启用 ALLOW_MOCK_DATA")
        
        print(f"✅ 筛选出主分类为AI相关的论文: {len(filtered_papers)} 篇")
        return filtered_papers
        
    except Exception as e:
        print(f"获取arXiv论文失败: {e}")
        if _allow_mock_data():
            print("ALLOW_MOCK_DATA=true，使用模拟数据...")
            return fetch_mock_papers()
        raise

def fetch_mock_papers() -> List[ArxivPaper]:
    """返回模拟论文数据用于测试"""
    mock_entry = {
        'id': 'http://arxiv.org/abs/2401.00001v1',
        'title': 'Sample AI Paper: Deep Learning for Time Series Forecasting',
        'author': [
            {'name': 'Zhang San'},
            {'name': 'Li Si'},
            {'name': 'Wang Wu'}
        ],
        'summary': 'This paper presents a novel deep learning approach for time series forecasting. We propose a new architecture that combines attention mechanisms with temporal convolutional networks to capture both short-term and long-term dependencies in sequential data. Extensive experiments on multiple benchmark datasets demonstrate that our method achieves state-of-the-art performance.',
        'published': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'category': [
            {'@term': 'cs.LG'},
            {'@term': 'cs.AI'}
        ]
    }
    return [ArxivPaper(mock_entry)]

def generate_markdown(papers: List[ArxivPaper], date_str: str):
    """生成Markdown文件并保存到data/arxiv目录"""
    markdown_content = f"# arXiv AI 论文日报 | {date_str}\n\n"
    markdown_content += f"> 共 {len(papers)} 篇论文，由AI自动总结\n\n"
    
    # 按分类分组
    papers_by_category = {}
    for paper in papers:
        main_category = paper.categories[0] if paper.categories else 'Other'
        if main_category not in papers_by_category:
            papers_by_category[main_category] = []
        papers_by_category[main_category].append(paper)
    
    # 生成目录
    markdown_content += "## 📑 目录\n\n"
    for category, category_papers in papers_by_category.items():
        markdown_content += f"- [{category}](#{category.replace('.', '')}) ({len(category_papers)} 篇)\n"
    markdown_content += "\n---\n\n"
    
    # 按分类生成内容
    rank = 1
    structured_items = []
    for category in sorted(papers_by_category.keys()):
        markdown_content += f"## {category}\n\n"
        for paper in papers_by_category[category]:
            markdown_content += paper.to_markdown(rank)
            structured_items.append(paper.to_content_item(rank, date_str))
            rank += 1
    
    # 确保data/arxiv目录存在
    os.makedirs('data/arxiv', exist_ok=True)
    
    # 保存文件到data/arxiv目录
    file_name = f"data/arxiv/arxiv-daily-{date_str}.md"
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    print(f"文件 {file_name} 生成成功。")
    save_structured_items(date_str, structured_items)

def main():
    """主函数"""
    # 默认抓取前一天，可通过 ARXIV_TARGET_DATE 覆盖
    target_date = os.getenv("ARXIV_TARGET_DATE", "").strip()
    if target_date:
        fetch_date_str = target_date
    else:
        yesterday = datetime.now(timezone.utc) - timedelta(days=1)
        fetch_date_str = yesterday.strftime('%Y-%m-%d')

    # 输出日期：可显式覆盖；默认在自动模式下写当天
    output_date = os.getenv("ARXIV_OUTPUT_DATE", "").strip()
    if output_date:
        date_str = output_date
    elif target_date:
        # 手动指定抓取日期但未指定输出日期时，保持历史行为
        date_str = target_date
    else:
        today = datetime.now(timezone.utc)
        date_str = today.strftime('%Y-%m-%d')
    
    # 从环境变量读取配置
    default_categories = 'cs.AI,cs.LG,cs.CL,cs.CV'
    categories_str = os.getenv('ARXIV_CATEGORIES', default_categories)
    if categories_str is None or categories_str.strip() == "":
        categories_str = default_categories
    categories = [cat.strip() for cat in categories_str.split(',') if cat.strip()]
    if not categories:
        categories = [cat.strip() for cat in default_categories.split(',')]
    max_results = _get_int_env('ARXIV_MAX_RESULTS', 30)
    
    print(f"=== arXiv AI 论文爬取开始 ===")
    print(f"抓取日期: {fetch_date_str}")
    print(f"写入日期: {date_str}")
    print(f"分类: {', '.join(categories)}")
    print(f"最大数量: {max_results}")
    
    # 获取论文
    papers = fetch_arxiv_papers(
        categories=categories,
        max_results=max_results,
        target_date=fetch_date_str
    )
    
    # 生成Markdown
    generate_markdown(papers, date_str)
    
    print(f"=== arXiv AI 论文爬取完成 ===")

if __name__ == "__main__":
    main()
