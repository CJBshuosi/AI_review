# Text-to-SQL 论文元数据库使用指南

> 📚 这是一个包含41篇Text-to-SQL领域多智能体/智能体系统论文的结构化元数据库
>
> **元数据文件**: `Text-to-SQL_Papers_Metadata.yaml`

---

## 📋 目录

- [元数据库概览](#元数据库概览)
- [文件结构](#文件结构)
- [使用场景](#使用场景)
- [数据字段说明](#数据字段说明)
- [查询示例](#查询示例)
- [统计信息](#统计信息)

---

## 📊 元数据库概览

### 基本信息

| 项目 | 数值 |
|------|------|
| **论文总数** | 41篇 |
| **2025年顶会论文** | 21篇 |
| **arXiv预印本** | 20篇 |
| **涵盖会议** | ICLR, NeurIPS, ACL, NAACL, COLING, AAAI, EMNLP, CIKM |
| **开源代码** | 17篇 (70%+) |
| **基准数据集** | 7个 |

### 分类统计

**按研究方向**:
- 多智能体系统: 10篇
- 自我修正与强化学习: 8篇
- 评估与基准: 6篇
- 检索增强与工具: 3篇
- 多轮对话: 3篇
- 综述论文: 3篇
- 效率优化: 3篇
- 其他: 5篇

**按影响力**:
- Very High: 3篇 (SQL-o1, ReFoRCE, Spider 2.0)
- High: 15篇
- Medium-High: 8篇
- Medium: 13篇

---

## 🗂️ 文件结构

YAML文件包含以下主要部分：

```yaml
metadata:                    # 元数据信息
  version: "1.0"
  last_updated: "2025-10-18"
  total_papers: 41

conference_papers:           # 顶会论文 (21篇)
  - id: paper_id
    title: "论文标题"
    authors: [...]
    venue: {...}
    links: {...}
    category: [...]
    keywords: [...]
    performance: [...]
    key_contributions: [...]

arxiv_preprints:            # arXiv预印本 (20篇)
  - id: paper_id
    title: "论文标题"
    ...

benchmarks:                 # 基准数据集 (7个)
  - name: "数据集名称"
    ...

institutions:               # 研究机构
  - name: "机构名称"
    ...

tools_frameworks:           # 工具与框架
  - name: "工具名称"
    ...

statistics:                 # 统计分析
  total_papers: 41
  by_year: {...}
  by_venue: {...}

performance_milestones:     # 性能里程碑
  spider_1_0: [...]
  spider_2_0: [...]

reading_priority:           # 推荐阅读优先级
  must_read: [...]
  highly_recommended: [...]
```

---

## 💡 使用场景

### 1. 文献调研

**快速筛选论文**:
```python
import yaml

with open('Text-to-SQL_Papers_Metadata.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

# 筛选多智能体系统相关论文
multi_agent_papers = [
    paper for paper in data['conference_papers']
    if 'Multi-Agent Systems' in paper.get('category', [])
]

print(f"找到 {len(multi_agent_papers)} 篇多智能体论文")
```

### 2. 性能对比

**提取Spider基准性能**:
```python
spider_performance = []
for paper in data['conference_papers'] + data['arxiv_preprints']:
    if 'performance' in paper:
        for perf in paper['performance']:
            if 'Spider' in perf.get('benchmark', ''):
                spider_performance.append({
                    'paper': paper['title'],
                    'score': perf.get('score')
                })
```

### 3. 趋势分析

**按年份统计**:
```python
papers_by_year = {}
for paper in data['conference_papers']:
    year = paper['venue']['year']
    papers_by_year[year] = papers_by_year.get(year, 0) + 1

print("年度论文数:", papers_by_year)
# 输出: {2024: 3, 2025: 18}
```

### 4. 寻找开源代码

**筛选有GitHub链接的论文**:
```python
open_source_papers = [
    {
        'title': paper['title'],
        'github': paper['links'].get('github')
    }
    for paper in data['conference_papers']
    if 'github' in paper.get('links', {})
]

print(f"找到 {len(open_source_papers)} 篇开源论文")
```

### 5. 构建论文阅读清单

**按优先级整理**:
```python
reading_list = []

# 必读论文
for item in data['reading_priority']['must_read']:
    paper = next(p for p in data['conference_papers']
                 if p['id'] == item['id'])
    reading_list.append({
        'priority': 'Must Read',
        'title': paper['title'],
        'reason': item['reason']
    })

# 强烈推荐
for item in data['reading_priority']['highly_recommended']:
    paper = next(p for p in data['conference_papers']
                 if p['id'] == item['id'])
    reading_list.append({
        'priority': 'Highly Recommended',
        'title': paper['title'],
        'reason': item['reason']
    })
```

---

## 📖 数据字段说明

### 论文条目（Paper Entry）

#### 基本字段

| 字段 | 类型 | 说明 | 示例 |
|------|------|------|------|
| `id` | String | 唯一标识符 | `spider2-iclr2025` |
| `title` | String | 论文标题 | `"Spider 2.0: ..."` |
| `authors` | List | 作者列表 | `[{name: "..."}]` |
| `venue` | Object | 发表信息 | 见下文 |
| `links` | Object | 相关链接 | 见下文 |
| `category` | List | 研究分类 | `["Multi-Agent Systems"]` |
| `keywords` | List | 关键词 | `["MCTS", "Self-Reward"]` |

#### venue（发表信息）

```yaml
venue:
  conference: "ICLR"        # 会议名称
  year: 2025                # 年份
  type: "Oral Presentation" # 类型 (Oral/Poster/Findings/Main)
  rating: 5.75              # 评审分数 (如适用)
```

#### links（相关链接）

```yaml
links:
  arxiv: "https://..."      # arXiv链接
  arxiv_id: "2411.07763"    # arXiv ID
  github: "https://..."     # GitHub仓库
  website: "https://..."    # 项目网站
  openreview: "https://..." # OpenReview链接
  pdf: "https://..."        # PDF链接
  acl_anthology: "https://..." # ACL Anthology
```

#### performance（性能数据）

```yaml
performance:
  - benchmark: "Spider Test"  # 基准名称
    model: "GPT-4"            # 使用模型
    metric: "Execution Accuracy" # 评估指标
    score: 87.6               # 分数
    improvement: "+10.8%"     # 提升幅度
    rank: 1                   # 排名
```

#### 特殊字段

**多智能体论文**:
```yaml
agents:
  - name: "Decomposer"
    role: "SQL generation"
    method: "Few-shot CoT"
```

**基准论文**:
```yaml
benchmark:
  name: "Spider 2.0"
  tasks: 632
  database_size: "1000+ columns"
```

**方法论文**:
```yaml
methods:
  - "MCTS Search"
  - "Self-Reward Mechanism"
```

---

## 🔍 查询示例

### 示例1: 查找特定会议的所有论文

```python
import yaml

def get_papers_by_conference(yaml_file, conference_name):
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    papers = [
        paper for paper in data['conference_papers']
        if paper['venue']['conference'] == conference_name
    ]

    return papers

# 使用
iclr_papers = get_papers_by_conference(
    'Text-to-SQL_Papers_Metadata.yaml',
    'ICLR'
)

print(f"ICLR 2025: {len(iclr_papers)} 篇论文")
for paper in iclr_papers:
    print(f"- {paper['title']}")
```

**输出**:
```
ICLR 2025: 3 篇论文
- Spider 2.0: Evaluating Language Models on Real-World Enterprise Text-to-SQL Workflows
- CHASE-SQL: Multi-Path Reasoning and Preference Optimized Candidate Selection in Text-to-SQL
- ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL
```

---

### 示例2: 按性能排序论文

```python
def get_top_papers_by_benchmark(yaml_file, benchmark_name='Spider', top_n=5):
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    paper_scores = []

    for paper in data['conference_papers'] + data['arxiv_preprints']:
        if 'performance' in paper:
            for perf in paper['performance']:
                if benchmark_name.lower() in perf.get('benchmark', '').lower():
                    paper_scores.append({
                        'title': paper['title'],
                        'score': perf.get('score', 0),
                        'benchmark': perf['benchmark']
                    })

    # 按分数排序
    paper_scores.sort(key=lambda x: x['score'], reverse=True)

    return paper_scores[:top_n]

# 使用
top_papers = get_top_papers_by_benchmark(
    'Text-to-SQL_Papers_Metadata.yaml',
    'Spider',
    top_n=5
)

print("Spider基准Top 5:")
for i, paper in enumerate(top_papers, 1):
    print(f"{i}. {paper['title']}: {paper['score']}%")
```

**输出**:
```
Spider基准Top 5:
1. GBV-SQL: ...: 97.6%
2. GBV-SQL: ...: 96.5%
3. CHASE-SQL: ...: 87.6%
4. AgentiQL: ...: 86.07%
...
```

---

### 示例3: 生成文献综述表格

```python
def generate_summary_table(yaml_file, category='Multi-Agent Systems'):
    import pandas as pd

    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    papers_data = []

    for paper in data['conference_papers']:
        if category in paper.get('category', []):
            papers_data.append({
                '标题': paper['title'],
                '会议': f"{paper['venue']['conference']} {paper['venue']['year']}",
                '关键词': ', '.join(paper.get('keywords', [])[:3]),
                '代码': '✅' if 'github' in paper.get('links', {}) else '❌',
                '影响力': paper.get('impact', 'Medium')
            })

    df = pd.DataFrame(papers_data)
    return df

# 使用
df = generate_summary_table('Text-to-SQL_Papers_Metadata.yaml')
print(df.to_markdown(index=False))
```

---

### 示例4: 生成BibTeX引用

```python
def generate_bibtex(yaml_file, paper_id):
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    # 查找论文
    paper = None
    for p in data['conference_papers'] + data['arxiv_preprints']:
        if p['id'] == paper_id:
            paper = p
            break

    if not paper:
        return None

    # 生成BibTeX
    bibtex = f"""@inproceedings{{{paper['id']},
    title = {{{paper['title']}}},
    author = {{{' and '.join([a['name'] for a in paper.get('authors', [])])}}},
    booktitle = {{{paper['venue']['conference']} {paper['venue']['year']}}},
    year = {{{paper['venue']['year']}}},
"""

    if 'arxiv_id' in paper.get('links', {}):
        bibtex += f"    arxiv = {{{paper['links']['arxiv_id']}}},\n"

    bibtex += "}"

    return bibtex

# 使用
bibtex = generate_bibtex('Text-to-SQL_Papers_Metadata.yaml', 'spider2-iclr2025')
print(bibtex)
```

**输出**:
```bibtex
@inproceedings{spider2-iclr2025,
    title = {Spider 2.0: Evaluating Language Models on Real-World Enterprise Text-to-SQL Workflows},
    author = {xlang-ai Team},
    booktitle = {ICLR 2025},
    year = {2025},
    arxiv = {2411.07763},
}
```

---

### 示例5: 寻找相关工作

```python
def find_related_papers(yaml_file, keywords, min_matches=2):
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    related_papers = []

    for paper in data['conference_papers'] + data['arxiv_preprints']:
        paper_keywords = set([kw.lower() for kw in paper.get('keywords', [])])
        search_keywords = set([kw.lower() for kw in keywords])

        # 计算匹配的关键词数量
        matches = paper_keywords.intersection(search_keywords)

        if len(matches) >= min_matches:
            related_papers.append({
                'title': paper['title'],
                'matches': list(matches),
                'match_count': len(matches)
            })

    # 按匹配数排序
    related_papers.sort(key=lambda x: x['match_count'], reverse=True)

    return related_papers

# 使用
related = find_related_papers(
    'Text-to-SQL_Papers_Metadata.yaml',
    keywords=['Multi-agent', 'Self-Correction', 'MCTS'],
    min_matches=1
)

print(f"找到 {len(related)} 篇相关论文:")
for paper in related[:5]:
    print(f"- {paper['title']}")
    print(f"  匹配关键词: {', '.join(paper['matches'])}")
```

---

### 示例6: 时间线可视化数据准备

```python
def prepare_timeline_data(yaml_file):
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    timeline = {}

    for paper in data['conference_papers']:
        year_month = f"{paper['venue']['year']}-{paper['venue'].get('date', '01')[:2]}"

        if year_month not in timeline:
            timeline[year_month] = []

        timeline[year_month].append({
            'title': paper['title'],
            'conference': paper['venue']['conference'],
            'type': paper['venue'].get('type', 'Paper')
        })

    return dict(sorted(timeline.items()))

# 使用
timeline = prepare_timeline_data('Text-to-SQL_Papers_Metadata.yaml')

for date, papers in timeline.items():
    print(f"\n{date}:")
    for paper in papers:
        print(f"  [{paper['conference']} {paper['type']}] {paper['title'][:50]}...")
```

---

## 📊 统计信息

### 可用的统计数据

元数据文件中 `statistics` 部分包含：

```yaml
statistics:
  total_papers: 41

  by_year:
    "2024": 8
    "2025": 33

  by_venue:
    "ICLR 2025": 3
    "NeurIPS 2025": 1
    "ACL 2025": 3
    "NAACL 2025": 6
    # ...

  by_category:
    "Multi-Agent Systems": 10
    "Self-Correction & RL": 8
    # ...

  code_availability:
    open_source: 17
    percentage: "70%+"
```

### 访问统计数据

```python
import yaml

with open('Text-to-SQL_Papers_Metadata.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

stats = data['statistics']

print(f"论文总数: {stats['total_papers']}")
print(f"开源代码: {stats['code_availability']['open_source']}篇 ({stats['code_availability']['percentage']})")
print("\n按类别分布:")
for category, count in stats['by_category'].items():
    print(f"  {category}: {count}篇")
```

---

## 🎯 高级用法

### 1. 构建知识图谱

```python
import networkx as nx

def build_citation_graph(yaml_file):
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    G = nx.DiGraph()

    # 添加节点（论文）
    for paper in data['conference_papers'] + data['arxiv_preprints']:
        G.add_node(
            paper['id'],
            title=paper['title'],
            year=paper.get('venue', {}).get('year', 2024)
        )

    # 可以根据关键词、类别等添加边
    # 这里简化示例

    return G
```

### 2. 推荐系统

```python
def recommend_papers(yaml_file, paper_id, top_n=5):
    """基于相似度推荐相关论文"""
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    # 找到目标论文
    target_paper = None
    all_papers = data['conference_papers'] + data['arxiv_preprints']

    for paper in all_papers:
        if paper['id'] == paper_id:
            target_paper = paper
            break

    if not target_paper:
        return []

    # 计算相似度（基于类别和关键词）
    target_keywords = set(target_paper.get('keywords', []))
    target_categories = set(target_paper.get('category', []))

    similarities = []

    for paper in all_papers:
        if paper['id'] == paper_id:
            continue

        paper_keywords = set(paper.get('keywords', []))
        paper_categories = set(paper.get('category', []))

        # 简单的相似度计算
        keyword_sim = len(target_keywords & paper_keywords)
        category_sim = len(target_categories & paper_categories) * 2

        total_sim = keyword_sim + category_sim

        if total_sim > 0:
            similarities.append({
                'paper': paper,
                'similarity': total_sim
            })

    # 按相似度排序
    similarities.sort(key=lambda x: x['similarity'], reverse=True)

    return [s['paper'] for s in similarities[:top_n]]

# 使用
recommendations = recommend_papers(
    'Text-to-SQL_Papers_Metadata.yaml',
    'spider2-iclr2025',
    top_n=3
)

print("推荐阅读:")
for paper in recommendations:
    print(f"- {paper['title']}")
```

---

## 📝 最佳实践

### 1. 数据验证

```python
def validate_metadata(yaml_file):
    """验证元数据完整性"""
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    issues = []

    for paper in data['conference_papers']:
        # 检查必需字段
        if 'id' not in paper:
            issues.append(f"Paper missing ID: {paper.get('title', 'Unknown')}")

        if 'title' not in paper:
            issues.append(f"Paper missing title: {paper.get('id', 'Unknown')}")

        # 检查链接有效性
        if 'links' in paper:
            if 'arxiv_id' in paper['links'] and 'arxiv' not in paper['links']:
                issues.append(f"Paper {paper['id']} has arxiv_id but no arxiv link")

    return issues

# 使用
issues = validate_metadata('Text-to-SQL_Papers_Metadata.yaml')
if issues:
    print("发现以下问题:")
    for issue in issues:
        print(f"  - {issue}")
else:
    print("✅ 元数据验证通过")
```

### 2. 定期更新

建议的更新流程：

1. **添加新论文**:
   ```yaml
   - id: new-paper-id
     title: "New Paper Title"
     # ... 完整字段
   ```

2. **更新统计信息**:
   ```python
   # 重新计算统计数据
   stats['total_papers'] += 1
   stats['by_year']['2025'] += 1
   ```

3. **更新版本号**:
   ```yaml
   metadata:
     version: "1.1"
     last_updated: "2025-10-25"
   ```

---

## 🛠️ 工具集成

### Jupyter Notebook

```python
# 在Jupyter中使用
import yaml
import pandas as pd
from IPython.display import display, Markdown

with open('Text-to-SQL_Papers_Metadata.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

# 创建DataFrame
papers_df = pd.DataFrame([
    {
        'Title': p['title'][:50],
        'Conference': f"{p['venue']['conference']} {p['venue']['year']}",
        'Category': ', '.join(p.get('category', [])[:2]),
        'Impact': p.get('impact', 'N/A')
    }
    for p in data['conference_papers']
])

display(papers_df)
```

### VS Code插件

推荐安装 **YAML** 插件以获得：
- 语法高亮
- 自动补全
- 错误检查
- 格式化

---

## 📚 参考资源

### YAML学习资源

- [YAML官方文档](https://yaml.org)
- [PyYAML文档](https://pyyaml.org)

### 相关工具

- **yq**: YAML查询工具 (类似jq)
- **yamllint**: YAML格式检查
- **ruamel.yaml**: 保留注释的YAML解析器

---

## 🤝 贡献指南

如果您想贡献新的论文或更新信息：

1. 确保论文符合收录标准（顶会/高质量arXiv）
2. 按照现有格式添加元数据
3. 更新统计信息
4. 运行验证脚本
5. 更新版本号和更新日期

---

## 📞 联系方式

如有问题或建议，欢迎：
- 提交Issue
- 发送Pull Request
- 联系维护者

---

**祝您研究顺利！📖✨**

*最后更新: 2025-10-18*
