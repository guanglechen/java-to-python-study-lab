# Python 学习实验室 | Python Study Lab

这个仓库是一个长期演进的学习项目，目标是帮助一位有经验的 Java 工程师系统转向 Python 后端开发和 AI 应用工程。

EN: This repository is a long-lived training project for a senior Java engineer moving into Python backend and AI application engineering.

## 当前重点 | Current Focus

当前先做两件事：

1. 搭一个能持续演进的单仓库学习工程。
2. 从第 1 阶段 Day 1 开始，用可运行代码和测试来学习 Python。

EN:
1. Build a single repository that can evolve from language basics into backend and AI engineering.
2. Start from Phase 1 Day 1 with runnable Python exercises and tests.

## 仓库结构 | Repository Layout

- `docs/`：学习计划、任务指引、迁移笔记（已按目录分层）
- `src/study_lab/`：学习代码和后续项目代码
- `tests/`：自动化测试
- `scripts/`：辅助脚本，包括语音播放脚本
- `examples/`：独立对比示例

EN:
- `docs/`: organized learning plans, guides, and migration notes
- `src/study_lab/`: application and learning code
- `tests/`: automated checks
- `scripts/`: helper scripts, including voice playback
- `examples/`: standalone examples

## 学习路线 | Learning Roadmap

完整路线在 `docs/plans/study-plan.md`。

当前执行目标在 `docs/plans/phase1-day-plan.md`。

如果你想听课程介绍，可以使用 `scripts/course_tts.py` 朗读 `docs/media/course-intro.md`。

## 阶段顺序 | Phase Order

1. 仓库骨架和学习规则
2. Python 语言迁移
3. 工程化工具和项目规范
4. FastAPI 后端
5. 数据库和缓存集成
6. 模型接入和 RAG
7. 图数据库和知识图谱
8. Agent 工作流编排

EN:
1. Repository skeleton and learning rules
2. Python language migration
3. Engineering tooling and project conventions
4. FastAPI backend
5. Database and cache integration
6. Model integration and RAG
7. Graph database and knowledge graph
8. Agent workflow orchestration

## 第 1 阶段学习结果 | Phase 1 Outcome

第 1 阶段只覆盖 Python 语言和标准库基础：

- 函数
- 列表和字典处理
- 异常设计
- 包和导入

目标很明确：先写出干净、自然的 Python 代码，不把 Java 的类式写法带进每个文件。

## 继续学习入口 | Resume Point

如果后面中断，再回来时优先看：

1. `docs/plans/phase1-day-plan.md`
2. `docs/notes/java-vs-python-notes.md`
3. `docs/media/course-intro.md`
4. `docs/tracking/progress.md`
5. `tests/unit/`

## 建议命令 | Suggested Command

准备好 Python 环境后，可以运行：

```bash
pytest tests/unit
```

如果你想直接听课程介绍，可以运行：

```bash
/Users/chenguangyue/Documents/code/python/study/.venv/bin/python scripts/course_tts.py --speak
```