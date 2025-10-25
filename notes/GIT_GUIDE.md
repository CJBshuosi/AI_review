# Git 提交信息

> **项目**: Text-to-SQL 研究项目 - ARES
> **日期**: 2025-10-19

---

## 📝 推荐的提交信息

```bash
git add .
git commit -m "🎯 Phase 1 完成: 文献调研与项目规划

- ✅ 深度分析41篇2024-2025年顶会论文
- ✅ 创建论文元数据库 (YAML格式)
- ✅ 撰写详细研究计划 (research_proposal.md)
- ✅ 确定研究方向: ARES (自适应路由多智能体系统)
- ✅ 搭建完整项目目录结构
- ✅ 编写项目文档和会议记录

核心创新:
1. 自适应路由机制 (根据复杂度动态选择策略)
2. 轻量级多智能体架构 (7B/14B开源模型)
3. 混合验证策略 (多重保障)
4. 失败记忆持续学习

目标: Spider 88%+, BIRD 65%+, 延迟<2s, 成本-70%
投稿: ICLR 2026"
```

---

## 🏷️ Git 标签建议

```bash
# 标记 Phase 1 完成
git tag -a v0.1-phase1-complete -m "Phase 1: Literature Review & Planning Complete"
```

---

## 📂 .gitignore 建议

如果还没有创建，建议添加 `.gitignore`:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/
env/

# Jupyter Notebook
.ipynb_checkpoints
*.ipynb_checkpoints/

# PyCharm
.idea/

# VSCode
.vscode/

# Data files (too large for git)
data/spider/database/*
data/bird/database/*
data/spider2/test/*
*.db
*.sqlite
*.sqlite3

# Model checkpoints (too large)
experiments/checkpoints/*.pt
experiments/checkpoints/*.pth
experiments/checkpoints/*.bin
*.safetensors

# Logs
*.log
experiments/logs/*.log

# Environment variables
.env
.env.local

# OS
.DS_Store
Thumbs.db

# Large files
*.tar.gz
*.zip
*.7z
```

---

## 🌿 Git 分支策略

```bash
# 主分支
main          # 稳定版本

# 开发分支
dev           # 开发主分支

# 功能分支
feature/classifier       # 复杂度分类器
feature/router          # 自适应路由
feature/agents          # 智能体实现
feature/validators      # 验证器
feature/memory          # 失败记忆

# 实验分支
exp/spider-baseline     # Spider baseline实验
exp/bird-baseline       # BIRD baseline实验
exp/ablation           # 消融实验

# 文档分支
docs/paper             # 论文撰写
```

---

## 🔄 推荐的工作流

```bash
# 1. 创建功能分支
git checkout -b feature/classifier

# 2. 开发和提交
git add .
git commit -m "feat: 实现复杂度分类器特征提取"

# 3. 推送到远程
git push origin feature/classifier

# 4. 合并到dev
git checkout dev
git merge feature/classifier

# 5. 定期合并到main
git checkout main
git merge dev --no-ff
git tag -a v0.2 -m "Classifier implementation complete"
```

---

**最后更新**: 2025-10-19
