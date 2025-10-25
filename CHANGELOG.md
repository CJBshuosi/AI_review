# Changelog

本文档记录Text-to-SQL研究项目的所有重要变更。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
并遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

---

## [Unreleased]

### 计划中
- 复杂度分类器实现
- Baseline系统开发
- Spider数据集评估

---

## [0.1.0] - 2025-10-19

### 🎉 项目启动 - Phase 1 完成

这是项目的第一个重要里程碑，标志着文献调研和项目规划阶段的完成。

### ✨ Added (新增)

#### 核心文档
- **README.md** - 项目总览，包含快速开始指南和项目结构说明
- **research_proposal.md** - 详细研究计划，包含3个研究方向的完整设计
  - 方向1: ARES - 自适应路由多智能体系统 (主推)
  - 方向2: SQL调试系统
  - 方向3: 小模型集成系统
- **PROJECT_SUMMARY.md** - Phase 1 项目总结报告
- **QUICK_REFERENCE.md** - 快速参考手册
- **DELIVERY_REPORT.md** - 完整交付报告
- **CHANGELOG.md** - 本变更日志

#### 参考资料
- **Text-to-SQL_2025_Conference_Papers_Update.md** - 2025年顶会论文更新 (17篇)
  - ICLR 2025: 3篇
  - NeurIPS 2025: 1篇
  - ACL 2025: 3篇
  - NAACL 2025: 6篇
  - COLING 2025: 1篇
  - AAAI 2025: 3篇
- **Text-to-SQL_Multi-Agent_Research_Survey_2024-2025.md** - 多智能体系统综述 (41篇论文)
- **Text-to-SQL_Papers_Metadata.yaml** - 结构化论文元数据库
- **Text-to-SQL_Metadata_Usage_Guide.md** - 元数据库使用指南

#### 项目笔记
- **notes/meetings/2025-10-19_kickoff.md** - 项目启动会议记录
- **notes/todo/weekly_tasks.md** - 每周任务清单和进度追踪
- **notes/ideas/research_ideas.md** - 8个核心研究想法
- **notes/GIT_GUIDE.md** - Git使用指南和工作流

#### 项目结构
- **code/** - 代码实现框架
  - `ares/` - 核心系统代码目录
    - `classifier/` - 复杂度分类器模块
    - `agents/` - 智能体实现 (5个子模块)
    - `validators/` - 验证器 (4个子模块)
    - `memory/` - 失败记忆系统
    - `router/` - 自适应路由
    - `utils/` - 工具函数
  - `scripts/` - 执行脚本目录
  - `configs/` - 配置文件目录
  - `notebooks/` - Jupyter Notebooks目录
  - `tests/` - 单元测试目录
- **data/** - 数据集目录
  - `spider/` - Spider数据集
  - `bird/` - BIRD数据集
  - `spider2/` - Spider 2.0数据集
  - `failure_cases/` - 失败案例
  - `training_data/` - 训练数据
- **experiments/** - 实验目录
  - `results/` - 实验结果
  - `logs/` - 日志
  - `checkpoints/` - 模型检查点
  - `figures/` - 实验图表
- **papers/** - 论文撰写目录
  - `drafts/` - 草稿
  - `submissions/` - 投稿版本
  - `reviews/` - 评审意见
- **docs/** - 文档目录
  - `design/` - 设计文档
  - `api/` - API文档
  - `tutorials/` - 教程
- **notes/** - 笔记目录
- **references/** - 参考资料目录

### 📊 Research (研究成果)

#### 文献调研
- 深度分析 **41篇** 2024-2025年Text-to-SQL顶会论文
  - 顶会论文: 21篇 (51%)
  - arXiv预印本: 20篇 (49%)
- 创建结构化元数据库 (YAML格式)
- 识别5个主要研究趋势:
  1. 多智能体协作成为主流 (10篇, 29%)
  2. 自我修正+强化学习带来性能突破 (+10.8%)
  3. Spider 2.0揭示真实场景gap (SOTA仅21.3%)
  4. 14B开源模型逼近GPT-4 (仅差3.58%)
  5. SQL调试成为全新研究方向

#### 研究方向
- 确定主推方向: **ARES** (Adaptive Routing for Efficient SQL generation)
- 定义4个核心创新:
  1. 自适应路由机制
  2. 轻量级多智能体架构
  3. 混合验证策略
  4. 失败记忆与持续学习
- 设定性能目标:
  - Spider: 88-90% EX (+0.4-2.4%)
  - BIRD: 65-68% EX (+1.77-4.77%)
  - 延迟: <2秒 (2-2.5x提升)
  - 成本: $0.03/query (降低70%)

#### 实施计划
- 制定8个月详细路线图:
  - Month 1-2: 文献调研 ✅
  - Month 3-4: 系统实现 (待开始)
  - Month 5-6: 实验评估 (待开始)
  - Month 7-8: 论文撰写 (待开始)
- 确定投稿目标: ICLR 2026 (首选)

### 📝 Documentation (文档)

#### 会议记录
- 2025-10-19: 项目启动会议
  - 确认研究方向
  - 讨论技术路线
  - 制定时间表
  - 分配下一步任务

#### 任务管理
- 创建每周任务清单系统
- 定义Phase 1-4的详细任务
- 设置里程碑和检查点

#### 研究想法
- 记录8个核心研究想法:
  1. 自适应路由的阈值学习
  2. 分层验证策略
  3. 失败案例的主动学习
  4. 多模型集成的智能投票
  5. 渐进式SQL生成
  6. 基于语义的SQL去重
  7. 跨域迁移的Few-shot Adaptation
  8. 实时性能监控与自动调优

### 🎯 Milestones (里程碑)

- ✅ **Phase 1 完成** (2025-10-19)
  - 文献调研 100%
  - 研究方向确定 100%
  - 项目规划完成 100%
  - 基础设施搭建 100%

### 📈 Statistics (统计)

- **文献阅读**: 41篇论文 (~100小时)
- **文档撰写**: 13个文件 (~220KB)
- **项目结构**: 47个目录
- **研究想法**: 8个核心想法
- **实验计划**: 3个消融实验
- **时间投入**: 约2周
- **代码行数**: 0 (Phase 2开始)

---

## [0.0.1] - 2025-10-18

### Added
- 初始化Git仓库
- 创建基础README

---

## 版本说明

### 版本命名规则

本项目遵循语义化版本 `MAJOR.MINOR.PATCH`

- **MAJOR**: 重大里程碑 (Phase完成)
- **MINOR**: 功能模块完成 (系统组件)
- **PATCH**: 小修复和改进

### Phase与版本对应

| Phase | 版本 | 状态 |
|-------|------|------|
| Phase 0: 项目初始化 | 0.0.x | ✅ 完成 |
| Phase 1: 文献调研 | 0.1.0 | ✅ 完成 |
| Phase 2: 系统实现 | 0.2.0 | ⏳ 待开始 |
| Phase 3: 实验评估 | 0.3.0 | ⏳ 待开始 |
| Phase 4: 论文撰写 | 0.4.0 | ⏳ 待开始 |
| Phase 5: 论文投稿 | 1.0.0 | ⏳ 待开始 |

---

## 未来计划

### [0.2.0] - 预计 2025-12

#### Planned
- [ ] 实现复杂度分类器
- [ ] 开发多路径执行引擎
- [ ] 实现混合验证机制
- [ ] 构建失败记忆系统
- [ ] Spider baseline评估

### [0.3.0] - 预计 2026-02

#### Planned
- [ ] Spider完整评估
- [ ] BIRD完整评估
- [ ] 消融实验
- [ ] 延迟和成本分析
- [ ] Spider 2.0测试

### [0.4.0] - 预计 2026-03

#### Planned
- [ ] 论文初稿完成
- [ ] 实验结果整理
- [ ] 图表制作
- [ ] 相关工作完善

### [1.0.0] - 预计 2026-04

#### Planned
- [ ] 论文最终版本
- [ ] ICLR 2026投稿
- [ ] 代码开源发布
- [ ] 文档完善

---

## 变更类型说明

- **Added**: 新增功能/文件
- **Changed**: 现有功能的变更
- **Deprecated**: 即将移除的功能
- **Removed**: 已移除的功能
- **Fixed**: Bug修复
- **Security**: 安全问题修复
- **Research**: 研究成果
- **Documentation**: 文档更新
- **Performance**: 性能改进

---

## 链接

- [项目仓库](https://github.com/your-org/tecent_text2sql) (待创建)
- [研究计划](./research_proposal.md)
- [项目总结](./PROJECT_SUMMARY.md)
- [快速参考](./QUICK_REFERENCE.md)

---

**维护者**: Research Team
**最后更新**: 2025-10-19
**文档版本**: 1.0
