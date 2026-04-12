# Python 单仓库训练计划 | Single-Repo Python Training Plan

## 目标 | Goal

把这个仓库作为一个连续演进的训练项目，用来完成从 Java 工程开发到 Python 后端与 AI 应用工程的迁移。

EN: Use this repository as one continuous training project for the transition from Java engineering to Python backend and AI application engineering.

## 原则 | Principles

1. 通过编码学习，而不是只记笔记。
2. 保持一个仓库，按阶段逐步演进。
3. 把语言学习、工程化、后端开发和 AI 编排按层分开。
4. 每天都要有代码、测试和总结。

EN:
1. Learn by coding, not by collecting notes.
2. Keep one repository and let it evolve by phase.
3. Separate language learning, engineering setup, backend development, and AI orchestration by layer.
4. End each day with code, tests, and written conclusions.

## 阶段路线 | Phase Roadmap

### Phase 1: 仓库骨架与学习规则 | Repository skeleton and learning rules

- 建立主包、测试、文档、脚本和示例目录。
- 后续所有练习都放在这个仓库里。
- 用文档记录迁移笔记和每日进度。

### Phase 2: Python 语言迁移 | Python language migration

- 只聚焦语言和标准库。
- 学习函数、集合、异常、模块、数据类、生成器、装饰器和异步基础。
- 每个学习模块都要写测试。

### Phase 3: 工程化工具 | Engineering tooling

- 增加 `pyproject.toml`、依赖管理、lint、测试、类型检查、pre-commit 和日志规范。
- 让仓库具备真正项目化的感觉。

### Phase 4: FastAPI 后端 | FastAPI backend

- 增加 API 路由、请求响应模型、依赖注入和集成测试。

### Phase 5: 数据库与缓存 | Database and cache

- 增加 SQLAlchemy、Alembic、Redis 和配置分层。

### Phase 6: 模型接入与 RAG | Model integration and RAG

- 增加 LLM 封装、embedding 流程、切分、检索和基础评估。

### Phase 7: 图数据库与知识图谱 | Graph database and knowledge graph

- 增加图建模、图查询和图增强检索实验。

### Phase 8: Agent 工作流编排 | Agent workflow orchestration

- 增加工具、状态、工作流和端到端编排。

## 日节奏顺序（按阶段编号） | Day-Based Sequence (Per Phase)

1. Phase 1（Day 1-5）：`src/study_lab/core` 中的 Python 基础（函数、集合、异常）
2. Phase 2（Day 1-5）：Pythonic 模式与类型标注进阶（dataclass、typing、generator、decorator、context manager、async）
3. Phase 3（Day 1-4）：项目工具链（pyproject、pytest、lint、type check、logging、env）
4. Phase 4（Day 1-5）：FastAPI 基础与接口测试
5. Phase 5（Day 1-5）：数据库与缓存
6. Phase 6（Day 1-5）：模型服务与 RAG
7. Phase 7（Day 1-5）：图数据库与知识图谱
8. Phase 8（Day 1-6）：Agent 编排与端到端整合

## 仓库边界 | Repository Guardrails

- 正式代码必须放在 `src/` 和 `tests/`。
- 文档用来解释决策，但不能替代代码。
- AI 框架不能决定仓库顶层结构。
- 新增层应尽量依赖更少、更稳定的下层模块。