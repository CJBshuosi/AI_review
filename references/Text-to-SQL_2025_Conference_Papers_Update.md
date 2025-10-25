# Text-to-SQL 2025年顶会论文最新更新

> **更新时间**: 2025-10-18
> **涵盖会议**: ICLR 2025, NeurIPS 2025, ACL 2025, NAACL 2025, COLING 2025, AAAI 2025
> **论文总数**: 17+ 篇已确认接收的论文

---

## 📊 2025年顶会接收统计

| 会议 | 接收Text-to-SQL论文数 | 会议时间 | 录取率 | 亮点 |
|------|---------------------|---------|-------|------|
| **ICLR 2025** | 3篇+ (含1篇Oral) | 2025年4月 | - | Spider 2.0 Oral |
| **NeurIPS 2025** | 1篇+ | 2025年 | 24.52% (总体) | BIRD-CRITIC基准 |
| **ACL 2025** | 3篇 (Findings) | 2025年7月 | - | 数据合成、语义桥接 |
| **NAACL 2025** | 5篇+ | 2025年5月 | - | 多样化应用场景 |
| **COLING 2025** | 1篇 (已知) | 2025年1月 | - | MAC-SQL |
| **AAAI 2025** | 3篇+ | 2025年2月 | - | 一致性验证 |

**总计**: **17+篇**已确认的Text-to-SQL相关论文被2025年顶会接收

---

## 🏆 ICLR 2025 (International Conference on Learning Representations)

### 会议信息
- **时间**: 2025年4月24-28日
- **地点**: 新加坡
- **官网**: https://iclr.cc/Conferences/2025

---

### 1. ⭐ Spider 2.0: Evaluating Language Models on Real-World Enterprise Text-to-SQL Workflows (Oral)

**📄 论文信息**
- **类型**: Oral Presentation (口头报告 - 顶级论文标志)
- **报告时间**: Friday, April 25, 3:42PM — 3:54PM
- **arXiv ID**: 2411.07763
- **作者**: 来自 xlang-ai 团队
- **官网**: https://spider2-sql.github.io/
- **GitHub**: https://github.com/xlang-ai/Spider2
- **OpenReview**: https://openreview.net/forum?id=XmProj9cPs

**🎯 核心贡献**

**新基准数据集**:
- **632个真实企业级Text-to-SQL工作流问题**
- 来源于真实企业数据库应用场景
- 数据库规模：通常**超过1000列**
- 支持多种数据库系统：**BigQuery, Snowflake** 等云数据库

**任务复杂度**:

解决Spider 2.0任务需要：
1. **理解和搜索数据库元数据**
2. **阅读SQL方言文档**
3. **浏览项目级代码库**
4. **处理超长上下文** (远超传统基准)
5. **生成多个SQL查询** (通常超过100行代码)
6. **执行复杂推理**

**📊 性能对比**

| 模型 | Spider 1.0 | BIRD | Spider 2.0 | 性能下降 |
|------|-----------|------|-----------|---------|
| **o1-preview (Code Agent)** | 91.2% | 73.0% | **21.3%** | 📉 -69.9% |
| **o1-preview** | - | - | **17.1%** | - |
| **GPT-4o** | 86.6% | - | **10.1%** | 📉 -76.5% |

**关键洞察**:
- ✅ Spider 2.0 比 Spider 1.0 难度提升 **4-8倍**
- ✅ 即使是最先进的 o1-preview 也只能解决 **21.3%** 的任务
- ✅ 表明现有方法在真实企业场景下仍有巨大提升空间

**💡 主要影响**

- 🔥 重新定义了 Text-to-SQL 任务的难度标准
- 🔥 推动研究从学术基准走向真实应用
- 🔥 Snowflake 赞助支持 Spider 2.0 挑战赛
- 🔥 ICLR 2025 Oral (仅少数顶级论文获此殊荣)

---

### 2. CHASE-SQL: Multi-Path Reasoning and Preference Optimized Candidate Selection in Text-to-SQL

**📄 论文信息**
- **类型**: Poster
- **arXiv ID**: 2410.01943
- **评分**: 5.75 (ICLR评审分数)
- **作者**: Mohammadreza Pourreza, Hailong Li, Ruoxi Sun, Yeounoh Chung, Shayan Talaei, Gaurav Tarlok Kakkar, Yu Gan, Amin Saberi, Fatma Özcan, Sercan Ö. Arik
- **机构**: Google Cloud, Stanford University
- **OpenReview**: https://openreview.net/forum?id=CvGqMD5OtX
- **ICLR页面**: https://iclr.cc/virtual/2025/poster/30489

**🔬 核心方法**

**多智能体建模 + 测试时计算 (Multi-Agent Modeling + Test-Time Compute)**

**三种候选生成策略**:

1. **Divide-and-Conquer Method (分而治之)**
   - 将复杂查询分解为可管理的子查询
   - 单次 LLM 调用完成分解

2. **Query Execution Plan-Based Reasoning (基于查询执行计划的推理)**
   - 使用 Chain-of-Thought 推理
   - 模拟数据库引擎的执行步骤
   - 反映查询执行的实际过程

3. **Instance-Aware Synthetic Examples (实例感知的合成示例)** ⭐ 创新点
   - 为测试问题**定制化**生成 few-shot 示例
   - 示例与具体问题高度相关
   - 显著提升生成质量

**候选选择机制**:

- **Selection Agent (选择智能体)**:
  - 通过成对比较对候选进行排序
  - 使用微调的二元候选选择 LLM
  - 比传统选择方法更鲁棒

**📊 性能表现**

- **Spider 测试集**: **87.6% 执行准确率**
- **排名**: 在针对 Spider 进行训练或提示优化的方法中**排名第二**
- 优于多数未针对 Spider 专门优化的通用方法

**💡 创新亮点**

- ✅ 多路径推理提供多样化候选
- ✅ 实例感知示例生成提升针对性
- ✅ 成对比较选择机制更可靠
- ✅ 来自 Google Cloud 和 Stanford 的联合研究

---

### 3. ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL

**📄 论文信息**
- **类型**: Poster
- **arXiv ID**: 2412.10138
- **评分**: 5.00 (ICLR评审分数)
- **GitHub**: https://github.com/D2I-ai/Route (PyTorch实现)
- **OpenReview**: https://openreview.net/forum?id=BAglD6NGy0

**🔬 核心方法**

**RObust mUltitask Tuning and collaboration mEthod (ROUTE)**

**两大核心组件**:

**1. Multitask Supervised Fine-Tuning (MSFT) - 多任务监督微调**

引入多个与SQL生成相关的SFT任务：
- **Schema Linking (模式链接)**: 识别相关表和列
- **Noise Correction (噪声修正)**: 纠正输入中的错误
- **Continuation Writing (续写)**: 补全部分SQL
- **SQL Generation (SQL生成)**: 完整生成SQL

使用各种合成训练数据进行多任务学习

**2. Multitask Collaboration Prompting (MCP) - 多任务协作提示**

- 灵感来自 **LLM 智能体的协作模式**
- 利用多个SQL相关任务的协作
- **减少幻觉** (Hallucination) 现象
- SQL生成过程中的多任务协同

**📊 实验结果**

- **8个开源LLM** 上进行广泛实验
- **5个广泛使用的基准** 上评估
- **超越最新的Text-to-SQL方法**
- **取得领先性能**

**💡 主要贡献**

- ✅ 提出鲁棒的多任务调优方法
- ✅ 多任务协作减少幻觉
- ✅ 在多个开源LLM上验证有效性
- ✅ 开源PyTorch实现

---

## 🧠 NeurIPS 2025 (Neural Information Processing Systems)

### 会议信息
- **提交数**: 21,575篇 (Main Track)
- **接收数**: 5,290篇
- **录取率**: 24.52%
- **决定公布**: 2025年9月19日
- **官网**: https://neurips.cc/Conferences/2025

---

### 1. SWE-SQL: Illuminating LLM Pathways to Solve User SQL Issues in Real-World Applications

**📄 论文信息**
- **类型**: Main Conference Paper
- **arXiv ID**: 2506.18951
- **GitHub**: https://github.com/bird-bench/BIRD-CRITIC-1
- **官网**: https://bird-critic.github.io/
- **别名**: BIRD-CRITIC 1.0

**🎯 核心贡献**

**新基准: BIRD-CRITIC**

**数据集规模**:
- **BIRD-CRITIC-PG**: 530个 PostgreSQL 任务
- **BIRD-CRITIC-Multi**: 570个多方言任务
- **总计**: 1,100+ 真实用户SQL问题

**支持的SQL方言**:
- MySQL
- PostgreSQL
- SQL Server
- Oracle

**任务定义**: SQL 问题调试 (SQL Issue Debugging)
- 给定一个有错误的SQL和问题描述
- 要求模型诊断并修复SQL问题
- 模拟真实开发者的调试场景

**📊 性能基线**

| 模型 | BIRD-CRITIC-PG | BIRD-CRITIC-Multi |
|------|----------------|-------------------|
| **O3-Mini** (领先推理模型) | **38.87%** | **33.33%** |
| **Bird-Fixer** (Qwen-2.5-Coder-14B) | **38.11%** | **29.65%** |
| **Claude-3.7-Sonnet** | <38.11% | <29.65% |
| **GPT-4.1** | <38.11% | <29.65% |

**关键发现**:
- ✅ SQL调试比SQL生成更具挑战性
- ✅ 14B开源模型 (Bird-Fixer) **超越闭源模型** (Claude, GPT-4)
- ✅ 任务复杂度极高，最佳模型仅解决 ~38% 的问题

**🔧 训练环境: Six-Gym (SQL-fIX-Gym)**

**SQL-Rewind 策略**:
- 自动生成可执行的问题-解决方案数据集
- 通过**逆向工程**从验证过的SQL生成问题
- 从正确的SQL反推可能的错误

**f-Plan Boosting (计划提升)**:
- 从SQL解决方案中提取**高层调试计划**
- 使教师LLM产生 **73.7%** 更多成功轨迹
- 用于训练学生模型

**🤖 Bird-Fixer Agent**

基于 **Qwen-2.5-Coder-14B** 开发:
- 专门用于SQL问题调试
- 通过 Six-Gym 训练
- 超越 Claude-3.7-Sonnet 和 GPT-4.1

**💡 主要影响**

- 🔥 首个大规模SQL调试基准
- 🔥 揭示SQL调试的巨大挑战
- 🔥 开源模型在特定任务上超越闭源模型
- 🔥 提供完整的训练环境和数据集

---

## 📝 ACL 2025 (Annual Meeting of the Association for Computational Linguistics)

### 会议信息
- **会议时间**: 2025年7月
- **接收类型**: Findings (研究发现)
- **论文列表**: https://2025.aclweb.org/program/find_papers/

---

### 1. PARSQL: Enhancing Text-to-SQL through SQL Parsing and Reasoning

**📄 论文信息**
- **类型**: Findings
- **作者**: Yaxun Dai, Haiqin Yang, Mou Hao, Pingfu Chao

**🔬 核心方法**

- 通过 **SQL 解析** (SQL Parsing) 增强 Text-to-SQL
- 结合 **推理** (Reasoning) 机制
- 提升SQL生成的准确性和可解释性

**💡 创新点**

- ✅ 显式的SQL解析步骤
- ✅ 推理增强生成过程
- ✅ 提升复杂查询处理能力

---

### 2. UCS-SQL: Uniting Content and Structure for Enhanced Semantic Bridging In Text-to-SQL

**📄 论文信息**
- **类型**: Findings
- **作者**: Zhenhe Wu, Zhongqiu Li, Jie Zhang, Zhongjiang He, Jian Yang, Yu Zhao, Ruiyu Fang, Bing Wang, Hongyan Xie, Shuangyong Song, Zhoujun Li

**🔬 核心方法**

**统一内容与结构 (Uniting Content and Structure)**:
- **Content (内容)**: 自然语言问题的语义
- **Structure (结构)**: 数据库模式的结构

**增强语义桥接 (Enhanced Semantic Bridging)**:
- 建立问题与数据库之间的强语义连接
- 统一表示内容和结构信息
- 提升模式链接准确性

**💡 创新点**

- ✅ 内容-结构统一表示
- ✅ 增强的语义桥接机制
- ✅ 改进模式理解能力

---

### 3. SQLForge: Synthesizing Reliable and Diverse Data to Enhance Text-to-SQL Reasoning in LLMs

**📄 论文信息**
- **类型**: Findings
- **作者**: Yu Guo, Dong Jin, Shenghao Ye, Shuangwu Chen, Jianyang, Xiaobin Tan

**🔬 核心方法**

**合成可靠且多样的训练数据**:

**数据合成策略**:
1. **Reliability (可靠性)**:
   - 生成语法正确的SQL
   - 确保语义一致性
   - 验证可执行性

2. **Diversity (多样性)**:
   - 覆盖多种查询模式
   - 不同复杂度级别
   - 多样化的数据库模式

**增强LLM的Text-to-SQL推理能力**:
- 通过高质量合成数据训练
- 提升泛化能力
- 减少对人工标注的依赖

**💡 创新点**

- ✅ 自动化数据合成框架
- ✅ 可靠性和多样性的平衡
- ✅ 减少数据标注成本

---

## 🌎 NAACL 2025 (North American Chapter of the Association for Computational Linguistics)

### 会议信息
- **会议时间**: 2025年5月
- **论文列表**: https://2025.naacl.org/program/accepted_papers/
- **ACL Anthology**: https://aclanthology.org/events/naacl-2025/

---

### 1. MSc-SQL: Multi-Sample Critiquing Small Language Models For Text-To-SQL Translation

**📄 论文信息**
- **作者**: Satya Krishna Gorti, Ilan Gofman, Zhaoyan Liu, Jiapeng Wu, Noël Vouitsis, Guangwei Yu, Jesse C. Cresswell, Rasa Hosseinzadeh

**🔬 核心方法**

**Multi-Sample Critiquing (多样本批评)**:

- **Small Language Models (小型语言模型)**:
  - 针对资源受限场景
  - 使用更小的模型参数量
  - 保持竞争力性能

- **Critiquing Mechanism (批评机制)**:
  - 生成多个候选SQL
  - 智能体互相批评和改进
  - 迭代优化最终结果

**💡 创新点**

- ✅ 小模型也能高性能
- ✅ 多样本协作提升质量
- ✅ 适合资源受限环境

---

### 2. FLEX: Expert-level False-Less EXecution Metric for Text-to-SQL Benchmark

**📄 论文信息**
- **作者**: Heegyu Kim, Jeon Taeyang, SeungHwan Choi, Seungtaek Choi, Hyunsouk Cho

**🎯 核心贡献**

**新评估指标: FLEX**

**问题**: 现有评估指标的局限性
- 执行准确率 (Execution Accuracy) 存在假阳性
- SQL文本匹配 (Exact Match) 过于严格
- 需要更可靠的评估方法

**FLEX 特点**:
- **Expert-level**: 专家级别的评估标准
- **False-Less**: 减少假阳性判断
- **Execution-based**: 基于执行结果
- 更准确地反映SQL质量

**💡 主要影响**

- 🔥 提出更可靠的评估标准
- 🔥 解决现有指标的不足
- 🔥 推动基准测试的改进

---

### 3. Track-SQL: Enhancing Generative Language Models with Dual-Extractive Modules for Schema and Context Tracking in Multi-turn Text-to-SQL

**📄 论文信息**
- **作者**: Bingfeng Chen, Shaobin Shi, Yongqi Luo, Boyan Xu, Ruichu Cai, Zhifeng Hao

**🔬 核心方法**

**双提取模块 (Dual-Extractive Modules)**:

1. **Schema Tracking (模式跟踪)**:
   - 跨多轮对话跟踪相关数据库模式
   - 识别当前对话涉及的表和列
   - 动态更新模式上下文

2. **Context Tracking (上下文跟踪)**:
   - 维护对话历史
   - 追踪指代关系
   - 理解省略和简化表达

**多轮Text-to-SQL场景**:
- 用户进行连续多轮查询
- 后续问题依赖前面的上下文
- 需要持续跟踪模式和对话状态

**💡 创新点**

- ✅ 双模块协同工作
- ✅ 增强多轮对话能力
- ✅ 提升上下文理解

---

### 4. You Only Read Once (YORO): Learning to Internalize Database Knowledge for Text-to-SQL

**📄 论文信息**
- **作者**: Hideo Kobayashi, Wuwei Lan, Peng Shi, Shuaichen Chang, Jiang Guo, Henghui Zhu, Zhiguo Wang, Patrick Ng

**🔬 核心方法**

**You Only Read Once (YORO)** - 只读一次

**核心思想**:
- 让模型 **内化数据库知识** (Internalize Database Knowledge)
- 无需每次查询都重新读取完整模式
- 类似于人类对熟悉数据库的理解

**学习过程**:
1. **预先学习**: 模型学习并记忆数据库结构
2. **知识内化**: 将数据库知识编码到模型参数
3. **高效查询**: 查询时仅需问题，无需完整模式

**💡 优势**

- ✅ 显著减少输入长度
- ✅ 加快推理速度
- ✅ 降低计算成本
- ✅ 模拟人类专家的工作方式

---

### 5. PRACTIQ: A Practical Conversational Text-to-SQL dataset with Ambiguous and Unanswerable Queries

**📄 论文信息**
- **作者**: Mingwen Dong, Nischal Ashok Kumar, Yiqun Hu, Anuj Chauhan, Chung-Wei Hang, Shuaichen Chang, Lin Pan, Wuwei Lan

**🎯 核心贡献**

**新数据集: PRACTIQ**

**实用对话式Text-to-SQL数据集**:

**包含两类特殊问题**:

1. **Ambiguous Queries (模糊查询)**:
   - 问题描述不明确
   - 可能有多种理解
   - 需要澄清用户意图

   示例:
   ```
   用户: "Show me sales"
   模糊点:
   - 哪个时间段的销售？
   - 按什么维度统计？
   - 销售额还是销售量？
   ```

2. **Unanswerable Queries (无法回答的查询)**:
   - 数据库中没有相关数据
   - 问题超出数据库能力范围
   - 需要模型识别并告知用户

   示例:
   ```
   用户: "Show me customer's social media followers"
   问题: 数据库中没有社交媒体数据
   ```

**💡 主要影响**

- 🔥 更贴近真实应用场景
- 🔥 训练模型处理边界情况
- 🔥 提升系统鲁棒性
- 🔥 推动实用化研究

---

### 6. Industry Track Paper - Fine-tuning Strategies for Text-to-SQL

**📄 论文信息**
- **类型**: Industry Track (工业界论文)

**🔬 核心内容**

**减少数据库模式提示中的冗余**:

**问题**:
- 完整数据库模式可能非常长
- 包含大量无关表和列
- 浪费上下文窗口

**策略**:
- 智能模式选择
- 动态模式裁剪
- 优化提示结构

**工业界应用**:
- 实际生产环境的经验
- 性能与成本的权衡
- 可扩展性考虑

---

## 🌐 COLING 2025 (International Conference on Computational Linguistics)

### 会议信息
- **会议时间**: 2025年1月19-24日
- **地点**: 阿布扎比, 阿联酋
- **论文列表**: https://coling2025.org/program/main_conference_papers/

---

### 1. MAC-SQL: A Multi-Agent Collaborative Framework for Text-to-SQL

**📄 论文信息**
- **类型**: Main Conference Paper
- **arXiv ID**: 2312.11242
- **作者**: Bing Wang, Changyu Ren, Jian Yang, Xinnian Liang, Jiaqi Bai, Linzheng Chai, Zhao Yan, Qian-Wen Zhang, Di Yin, Xing Sun, Zhoujun Li
- **ACL Anthology**: https://aclanthology.org/2025.coling-main.36/
- **GitHub**: https://github.com/wbbeyourself/MAC-SQL

**🔬 核心方法**

(详见主文档中的完整介绍)

**三智能体协作**:
- **Selector**: 模式选择
- **Decomposer**: SQL生成
- **Refiner**: 错误修正

**📊 性能**

- **BIRD基准**: 59.59% EX (Holdout Test Set SOTA)
- **SQL-Llama基线**: 43.94% EX
- **GPT-4基线**: 46.35% EX

---

## 🔬 AAAI 2025 (Association for the Advancement of Artificial Intelligence)

### 会议信息
- **会议时间**: 2025年2月25日-3月4日
- **接收数**: 3,300+ 篇论文
- **官网**: https://aaai.org/conference/aaai/aaai-25/

---

### 已确认的Text-to-SQL论文

1. **SQLFixAgent: Towards Semantic-Accurate Text-to-SQL Parsing via Consistency-Enhanced Multi-Agent Collaboration**
   - arXiv: 2406.13408
   - (详见主文档)

2. **CogSQL: A Cognitive Framework**
   - 认知框架增强LLM的Text-to-SQL翻译能力

3. **Confidence Estimation for Error Detection in Text-to-SQL Systems**
   - GitHub: https://github.com/runnerup96/error-detection-in-text2sql
   - 使用熵基置信度估计进行错误检测

4. **MAGIC: Generating Self-Correction Guideline for In-Context Text-to-SQL**
   - arXiv: 2406.12692
   - (详见主文档)

---

## 📊 2025年Text-to-SQL研究趋势分析

### 1. 主题分布

| 主题 | 论文数 | 占比 | 代表论文 |
|------|--------|------|---------|
| **多智能体系统** | 5篇 | 29% | MAC-SQL, SQLFixAgent, CHASE-SQL, MSc-SQL |
| **新基准/评估** | 4篇 | 24% | Spider 2.0, SWE-SQL, FLEX, PRACTIQ |
| **多任务学习** | 2篇 | 12% | ROUTE, Track-SQL |
| **数据合成** | 1篇 | 6% | SQLForge |
| **语义增强** | 2篇 | 12% | UCS-SQL, PARSQL |
| **效率优化** | 1篇 | 6% | YORO |
| **其他** | 2篇 | 11% | CogSQL, 工业界论文 |

---

### 2. 技术趋势

**🔥 热点方向**:

1. **真实场景基准** (Spider 2.0, SWE-SQL)
   - 从学术数据集走向企业级应用
   - 任务难度显著提升
   - 评估更贴近实际使用

2. **多智能体协作持续火热**
   - 5篇论文采用多智能体方法
   - 不同智能体角色分工
   - 协作机制多样化

3. **小模型也能高性能**
   - MSc-SQL: 小型语言模型
   - ROUTE: 开源LLM优化
   - 资源效率成为关注点

4. **评估方法创新**
   - FLEX: 更可靠的评估指标
   - Spider 2.0: 真实场景评估
   - 解决现有基准的局限性

5. **处理边界情况**
   - PRACTIQ: 模糊和无法回答的查询
   - SWE-SQL: SQL调试任务
   - 提升系统鲁棒性

---

### 3. 性能进展

**Spider 基准性能演进**:

| 时间 | 代表方法 | 性能 | 提升 |
|------|---------|------|------|
| 2023 | 早期LLM方法 | ~70% | 基线 |
| 2024 | MAC-SQL, GBV-SQL | ~85% | +15% |
| 2025 | CHASE-SQL | **87.6%** | +2.6% |

**Spider 2.0 (新基准)**:
- o1-preview: **21.3%** (代码智能体)
- GPT-4o: **10.1%**
- 性能大幅下降，凸显真实场景挑战

**BIRD 基准**:
- MAC-SQL: 59.59%
- GBV-SQL: 63.23%
- 仍有巨大提升空间

---

### 4. 研究机构分布

**顶尖机构贡献**:

- **Google**: CHASE-SQL (Google Cloud)
- **Stanford**: CHASE-SQL, Spider 2.0
- **xlang-ai**: Spider 2.0
- **中国高校**: MAC-SQL, UCS-SQL等多篇论文
- **工业界**: Industry Track论文, YORO

**国际合作**:
- 多篇论文为跨机构合作
- 学术界与工业界结合
- 全球研究热度持续升温

---

### 5. 开源趋势

**代码开源情况**:

| 论文 | 开源状态 | GitHub链接 |
|------|---------|-----------|
| Spider 2.0 | ✅ 已开源 | github.com/xlang-ai/Spider2 |
| SWE-SQL | ✅ 已开源 | github.com/bird-bench/BIRD-CRITIC-1 |
| ROUTE | ✅ 已开源 | github.com/D2I-ai/Route |
| MAC-SQL | ✅ 已开源 | github.com/wbbeyourself/MAC-SQL |
| SQLFixAgent | ✅ 已开源 | github.com/Cen-Jipeng-SUDA/SQLFixAgent |
| CHASE-SQL | ⏳ 待确认 | - |

**开源率**: **70%+** 的论文提供代码实现

---

## 🎯 关键洞察

### 1. 任务难度重新定义

**Spider 2.0 的冲击**:
- ✅ 揭示真实企业场景与学术基准的巨大差距
- ✅ 即使最先进的o1-preview也只能解决21.3%的任务
- ✅ 推动研究从"刷榜"走向"解决实际问题"

### 2. 多智能体方法成熟化

**从探索到标准化**:
- ✅ 多篇顶会论文采用多智能体架构
- ✅ 智能体角色分工趋于一致（规划、生成、验证、修正）
- ✅ 协作机制多样化（投票、共识、成对比较）

### 3. 评估方法革新

**超越简单指标**:
- ✅ FLEX: 减少假阳性的评估指标
- ✅ Spider 2.0: 真实企业工作流评估
- ✅ SWE-SQL: 调试能力评估
- ✅ PRACTIQ: 边界情况处理能力

### 4. 小模型的反击

**资源效率关注**:
- ✅ MSc-SQL: 小型语言模型也能高性能
- ✅ Bird-Fixer (14B): 超越Claude和GPT-4
- ✅ ROUTE: 开源LLM优化达到SOTA
- ✅ 降低部署成本，提升实用性

### 5. 工业界参与加深

**学术与产业融合**:
- ✅ Google, Snowflake等企业深度参与
- ✅ Industry Track论文关注实际问题
- ✅ 真实数据和场景驱动研究
- ✅ 商业化产品涌现

---

## 📚 论文阅读推荐优先级

### 🌟 必读论文 (Top Priority)

1. **Spider 2.0** (ICLR 2025 Oral)
   - 理由: 重新定义任务难度，ICLR Oral
   - 适合: 所有Text-to-SQL研究者

2. **CHASE-SQL** (ICLR 2025)
   - 理由: 87.6%性能，多路径推理创新
   - 适合: 关注多智能体方法的研究者

3. **SWE-SQL** (NeurIPS 2025)
   - 理由: SQL调试新任务，BIRD-CRITIC基准
   - 适合: 关注实际应用的研究者

---

### 🔥 强烈推荐 (High Priority)

4. **ROUTE** (ICLR 2025)
   - 理由: 多任务协作，开源LLM优化
   - 适合: 关注开源模型的研究者

5. **PRACTIQ** (NAACL 2025)
   - 理由: 边界情况处理，实用场景
   - 适合: 构建生产系统的工程师

6. **SQLForge** (ACL 2025 Findings)
   - 理由: 数据合成方法，减少标注成本
   - 适合: 数据缺乏的研究者

---

### 📖 值得阅读 (Recommended)

7. **YORO** (NAACL 2025)
   - 理由: 效率优化，内化数据库知识
   - 适合: 关注推理效率的研究者

8. **Track-SQL** (NAACL 2025)
   - 理由: 多轮对话，双提取模块
   - 适合: 对话系统研究者

9. **UCS-SQL** (ACL 2025 Findings)
   - 理由: 内容-结构统一，语义桥接
   - 适合: 关注模式链接的研究者

10. **MSc-SQL** (NAACL 2025)
    - 理由: 小模型高性能，资源效率
    - 适合: 资源受限场景

---

### 🔧 参考论文 (Reference)

11. **FLEX** (NAACL 2025)
    - 理由: 评估指标创新
    - 适合: 基准测试研究者

12. **PARSQL** (ACL 2025 Findings)
    - 理由: SQL解析与推理
    - 适合: 符号方法爱好者

13. **MAC-SQL** (COLING 2025)
    - 理由: 经典多智能体框架
    - 适合: 入门多智能体方法

---

## 🔗 资源汇总

### 📄 会议官网

- **ICLR 2025**: https://iclr.cc/Conferences/2025
- **NeurIPS 2025**: https://neurips.cc/Conferences/2025
- **ACL 2025**: https://2025.aclweb.org
- **NAACL 2025**: https://2025.naacl.org
- **COLING 2025**: https://coling2025.org
- **AAAI 2025**: https://aaai.org/conference/aaai/aaai-25/

### 💾 数据集与基准

- **Spider 2.0**: https://spider2-sql.github.io/
- **BIRD-CRITIC**: https://bird-critic.github.io/
- **PRACTIQ**: (待公布)

### 💻 开源代码

- **Spider 2.0**: https://github.com/xlang-ai/Spider2
- **SWE-SQL**: https://github.com/bird-bench/BIRD-CRITIC-1
- **ROUTE**: https://github.com/D2I-ai/Route
- **MAC-SQL**: https://github.com/wbbeyourself/MAC-SQL
- **SQLFixAgent**: https://github.com/Cen-Jipeng-SUDA/SQLFixAgent

### 📊 论文检索工具

- **Paper Copilot**: https://papercopilot.com
- **OpenReview**: https://openreview.net
- **ACL Anthology**: https://aclanthology.org
- **arXiv**: https://arxiv.org

---

## 📌 更新日志

- **2025-10-18**: 初始版本，涵盖ICLR/NeurIPS/ACL/NAACL/COLING/AAAI 2025已公开论文
- **待更新**: EMNLP 2025论文列表（会议时间: 2025年11月）

---

## 🙏 致谢

感谢所有Text-to-SQL研究者的贡献，推动这个领域快速发展！

---

**Happy Reading! 📖✨**

*文档持续更新中，欢迎反馈和补充！*
