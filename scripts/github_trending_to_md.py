import os
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
from datetime import datetime, timezone
import openai
from bs4 import BeautifulSoup
from typing import List, Dict
import time
from common.storage import save_structured_items, build_item_id
from common.scoring import score_content

# AI 过滤关键字
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

# 创建 OpenAI 客户端实例（用于翻译）
api_key = os.getenv('OPENAI_API_KEY')
base_url = os.getenv('OPENAI_BASE_URL', 'https://api.openai.com/v1')
if api_key:
    try:
        client = openai.Client(api_key=api_key, base_url=base_url)
        print(f"成功初始化 OpenAI 客户端 (使用API地址: {base_url})")
    except Exception as e:
        print(f"初始化 OpenAI 客户端失败: {e}")
        client = None
else:
    print("未设置 OPENAI_API_KEY，将不进行翻译")
    client = None

class GitHubRepo:
    def __init__(self, data: Dict):
        """从爬取的数据初始化仓库对象"""
        self.name = data.get('name', '')
        self.author = data.get('author', '')
        self.url = data.get('url', '')
        self.description = data.get('description', '')
        self.language = data.get('language', 'Unknown')
        self.stars = data.get('stars', 0)
        self.forks = data.get('forks', 0)
        self.stars_today = data.get('stars_today', 0)
        
        # 翻译描述
        self.translated_description = self.translate_description()
        # 关键词
        self.keywords = self.generate_keywords()
        # 评分
        self.score = score_content(
            f"仓库: {self.author}/{self.name}\n描述: {self.description}\n中文介绍: {self.translated_description}\n关键词: {self.keywords}",
            client,
            kind="github",
        )

    def to_content_item(self, rank: int, date_str: str) -> dict:
        merged = f"{self.author}/{self.name} {self.description}".lower()
        hit_keywords = [kw for kw in AI_KEYWORDS if kw in merged]
        return {
            "id": build_item_id("gh", date_str, rank),
            "source": "github",
            "date": date_str,
            "rank": rank,
            "title": f"{self.author}/{self.name}",
            "url": self.url,
            "detail_url": self.url,
            "description_en": self.description,
            "description_zh": self.translated_description,
            "keywords": [k.strip() for k in self.keywords.split(",") if k.strip()],
            "tags": [self.language],
            "metrics": {
                "stars": self.stars,
                "forks": self.forks,
                "stars_today": self.stars_today,
            },
            "media": {"image": None},
            "ai_flags": {"is_ai": True, "hit_keywords": hit_keywords, "hit_excludes": []},
            "score": self.score,
            "raw": {},
        }
    
    def translate_description(self) -> str:
        """使用AI翻译项目描述"""
        if not self.description or client is None:
            return self.description
        
        try:
            print(f"正在翻译 {self.author}/{self.name} 的描述...")
            response = client.chat.completions.create(
                model=os.getenv('GITHUB_MODEL_NAME', 'gpt-4o-mini'),
                messages=[
                    {"role": "system", "content": "你是技术产品说明书撰写者。"},
                    {"role": "user", "content": (
                        "请将下面的 GitHub 项目简介翻译成中文，并在 2-3 句里补充：主要功能、目标用户/场景、使用的核心技术（尤其是 AI 相关）。"
                        "保持简洁、准确、信息量更高。\n\n"
                        f"{self.description}"
                    )}
                ],
                max_tokens=200,
                temperature=0.7,
            )
            translated = response.choices[0].message.content.strip()
            print(f"成功翻译")
            return translated
        except Exception as e:
            print(f"翻译失败: {e}")
            return self.description

    def generate_keywords(self) -> str:
        """
        生成中文为主的 AI 相关关键词，英文逗号分隔。
        不输出单独“AI/人工智能”，过滤排除词，5-10 个。
        """
        try:
            base_text = f"仓库: {self.author}/{self.name}\n描述: {self.description}"
            if client is None:
                words = (self.name + ", " + self.description).replace("&", ",").replace("|", ",").replace("-", ",").split(",")
                filtered = [w.strip() for w in words if w.strip()]
                filtered = [w for w in filtered if is_ai_related(w)]
                filtered = [w for w in filtered if w.lower() != 'ai' and w != '人工智能']
                return ", ".join(dict.fromkeys(filtered))

            prompt = (
                "生成仅限 AI 相关的中文关键词（专有名词可保留英文），英文逗号分隔：\n"
                "- 至少含 1 个 AI_KEYWORDS 的词或同义词，但不要输出单独“AI/人工智能”。\n"
                "- 不含 EXCLUDE_KEYWORDS。\n"
                "- 补充 2-3 个基于项目名称/技术/功能/架构的短关键词。\n"
                "- 总数 5-10 个，去重、去空格。\n"
                f"AI_KEYWORDS: {', '.join(AI_KEYWORDS)}\n"
                f"EXCLUDE_KEYWORDS: {', '.join(EXCLUDE_KEYWORDS)}\n"
                f"{base_text}"
            )
            resp = client.chat.completions.create(
                model=os.getenv('GITHUB_MODEL_NAME', 'gpt-4o-mini'),
                messages=[
                    {"role": "system", "content": "用中文输出关键词，满足给定约束。"},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=80,
                temperature=0.5,
            )
            keywords = resp.choices[0].message.content.strip()
            if ',' not in keywords:
                keywords = ', '.join(keywords.split())
            items = [k.strip() for k in keywords.split(',') if k.strip()]
            items = [k for k in items if k.lower() not in ('ai',) and k != '人工智能']
            items = [k for k in items if not _contains_any(k, EXCLUDE_KEYWORDS)]
            if not any(_contains_any(k, AI_KEYWORDS) for k in items):
                fallback = next((kw for kw in AI_KEYWORDS if kw != 'ai' and kw in (self.name + ' ' + self.description).lower()), 'agent')
                items.append(fallback)
            return ", ".join(dict.fromkeys(items))
        except Exception as e:
            print(f"关键词生成失败: {e}")
            return ""
    
    def to_markdown(self, rank: int) -> str:
        """转换为Markdown格式"""
        # 格式化星标数
        def format_number(num):
            if num >= 1000:
                return f"{num/1000:.1f}k"
            return str(num)
        
        stars_display = format_number(self.stars)
        forks_display = format_number(self.forks)
        
        # 今日新增星标
        today_stars = f" (+{format_number(self.stars_today)} today)" if self.stars_today > 0 else ""
        
        return f"""## [{rank}. {self.author}/{self.name}]({self.url})

**语言**: {self.language}  
**Stars**: ⭐ {stars_display}{today_stars} | **Forks**: 🔱 {forks_display}

**原始描述**: {self.description}

**中文介绍（含功能/场景/技术）**: {self.translated_description}

**关键词**: {self.keywords}

**评分**: {self.score.get('total', 0)}

**项目地址**: [GitHub]({self.url})

---

"""

def fetch_github_trending(language: str = "", since: str = "daily") -> List[GitHubRepo]:
    """
    爬取GitHub Trending页面
    
    参数:
        language: 编程语言过滤 (如 "python", "javascript", "" 表示所有)
        since: 时间范围 ("daily", "weekly", "monthly")
    """
    base_url = "https://github.com/trending"
    
    # 构建URL
    if language:
        url = f"{base_url}/{language}"
    else:
        url = base_url
    
    params = {"since": since}
    
    print(f"正在从GitHub Trending获取数据...")
    print(f"语言: {language if language else '全部'}, 时间范围: {since}")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 查找所有仓库条目
        repos = []
        articles = soup.find_all('article', class_='Box-row')
        
        print(f"找到 {len(articles)} 个仓库")
        
        for article in articles:
            try:
                # 提取仓库信息
                h2 = article.find('h2', class_='h3')
                if not h2:
                    continue
                
                a_tag = h2.find('a')
                if not a_tag:
                    continue
                
                # 仓库全名 (author/repo)
                full_name = a_tag.get('href', '').strip('/')
                if '/' not in full_name:
                    continue
                
                author, name = full_name.split('/', 1)
                
                # 描述
                desc_tag = article.find('p', class_='col-9')
                description = desc_tag.get_text(strip=True) if desc_tag else ''
                
                # 语言
                lang_tag = article.find('span', attrs={'itemprop': 'programmingLanguage'})
                language = lang_tag.get_text(strip=True) if lang_tag else 'Unknown'
                
                # 星标数
                star_tag = article.find('svg', class_='octicon-star')
                if star_tag:
                    star_parent = star_tag.find_parent('a')
                    stars_text = star_parent.get_text(strip=True) if star_parent else '0'
                    stars = parse_number(stars_text)
                else:
                    stars = 0
                
                # Fork数
                fork_tag = article.find('svg', class_='octicon-repo-forked')
                if fork_tag:
                    fork_parent = fork_tag.find_parent('a')
                    forks_text = fork_parent.get_text(strip=True) if fork_parent else '0'
                    forks = parse_number(forks_text)
                else:
                    forks = 0
                
                # 今日新增星标
                today_stars_tag = article.find('span', class_='d-inline-block float-sm-right')
                stars_today = 0
                if today_stars_tag:
                    today_text = today_stars_tag.get_text(strip=True)
                    stars_today = parse_number(today_text.split()[0])
                
                repo_data = {
                    'name': name,
                    'author': author,
                    'url': f"https://github.com/{full_name}",
                    'description': description,
                    'language': language,
                    'stars': stars,
                    'forks': forks,
                    'stars_today': stars_today
                }

                # AI 相关筛选
                if not is_ai_related(name, description):
                    print(f"跳过非AI仓库: {author}/{name}")
                    continue
                
                repos.append(GitHubRepo(repo_data))
                
            except Exception as e:
                print(f"解析仓库信息时出错: {e}")
                continue
        
        if not repos:
            print("未能解析到任何仓库，使用模拟数据...")
            return get_mock_repos()
        
        print(f"成功解析 {len(repos)} 个仓库")
        return repos
        
    except Exception as e:
        print(f"获取GitHub Trending失败: {e}")
        print("使用模拟数据...")
        return get_mock_repos()

def parse_number(text: str) -> int:
    """解析GitHub上的数字格式 (如 "1.2k" -> 1200)"""
    text = text.strip().replace(',', '')
    if 'k' in text.lower():
        return int(float(text.lower().replace('k', '')) * 1000)
    try:
        return int(text)
    except:
        return 0

def get_mock_repos() -> List[GitHubRepo]:
    """返回模拟数据用于测试"""
    mock_data = [
        {
            'name': 'awesome-project',
            'author': 'test-user',
            'url': 'https://github.com/test-user/awesome-project',
            'description': 'An awesome project for demonstration purposes',
            'language': 'Python',
            'stars': 12500,
            'forks': 2300,
            'stars_today': 150
        }
    ]
    return [GitHubRepo(data) for data in mock_data]

def generate_markdown(repos: List[GitHubRepo], date_str: str, language: str = "", since: str = "daily"):
    """生成Markdown文件并保存到data/github目录"""
    
    # 时间范围中文
    since_cn = {"daily": "日榜", "weekly": "周榜", "monthly": "月榜"}.get(since, "日榜")
    
    # 语言过滤
    lang_display = f"{language.upper()} " if language else ""
    
    markdown_content = f"# GitHub Trending {lang_display}{since_cn} | {date_str}\n\n"
    markdown_content += f"> 共 {len(repos)} 个项目\n\n"
    
    # 按语言分组
    repos_by_language = {}
    for repo in repos:
        lang = repo.language
        if lang not in repos_by_language:
            repos_by_language[lang] = []
        repos_by_language[lang].append(repo)
    
    # 生成目录
    markdown_content += "## 📑 目录\n\n"
    for lang in sorted(repos_by_language.keys()):
        markdown_content += f"- [{lang}](#{lang.replace(' ', '-').replace('+', 'plus').replace('#', 'sharp')}) ({len(repos_by_language[lang])} 个项目)\n"
    markdown_content += "\n---\n\n"
    
    # 按语言生成内容
    rank = 1
    structured_items = []
    for lang in sorted(repos_by_language.keys()):
        markdown_content += f"## {lang}\n\n"
        for repo in repos_by_language[lang]:
            markdown_content += repo.to_markdown(rank)
            structured_items.append(repo.to_content_item(rank, date_str))
            rank += 1
    
    # 确保data/github目录存在
    os.makedirs('data/github', exist_ok=True)
    
    # 保存文件
    lang_suffix = f"-{language}" if language else ""
    file_name = f"data/github/github-trending{lang_suffix}-{date_str}.md"
    
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    print(f"文件 {file_name} 生成成功。")
    save_structured_items(date_str, structured_items)

def main():
    """主函数"""
    today = datetime.now(timezone.utc)
    date_str = today.strftime('%Y-%m-%d')
    
    # 从环境变量读取配置
    language = os.getenv('GITHUB_LANGUAGE', '')  # 留空表示所有语言
    since = os.getenv('GITHUB_SINCE', 'daily')  # daily, weekly, monthly
    max_results = _get_int_env('GITHUB_MAX_RESULTS', 25)
    
    print(f"=== GitHub Trending 爬取开始 ===")
    print(f"日期: {date_str}")
    print(f"语言: {language if language else '全部'}")
    print(f"时间范围: {since}")
    
    # 获取trending仓库
    repos = fetch_github_trending(language=language, since=since)
    
    # 限制数量
    repos = repos[:max_results]
    
    # 生成Markdown
    generate_markdown(repos, date_str, language, since)
    
    print(f"=== GitHub Trending 爬取完成 ===")

if __name__ == "__main__":
    main()
