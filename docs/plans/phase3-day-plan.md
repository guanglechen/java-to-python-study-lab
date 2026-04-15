# 第 3 阶段日计划：工程化工具链 | Phase 3 Day Plan

## 目标

从“写 Python 脚本”转向“维护 Python 项目”。引入标准工具链，解决 Lint、类型检查、测试规范和日志问题。

## Day 1：现代 `pyproject.toml` 与 Ruff 配置

目标：统一 Lint 和格式化工具，替代 Flake8/Black/Isort。

任务：
1. 更新 `pyproject.toml`，增加 `[tool.ruff]` 配置。
2. 配置常用规则（E, F, I, B, UP）。
3. 运行 `ruff check` 和 `ruff format` 规范现有项目代码。

验收：
- 项目代码无 Lint 错误。
- 格式化风格统一。

## Day 2：静态类型检查 (Mypy)

目标：通过 Mypy 强制执行类型安全，接近 Java 的严谨性。

任务：
1. 在 `pyproject.toml` 中配置 `[tool.mypy]`。
2. 开启 `strict = true` 或常用的严格标志。
3. 修复现有代码中的类型提示漏洞。

验收：
- `mypy src` 无错误输出。

## Day 3：高效测试与日志 (Pytest & Logging)

目标：规范测试结构与日志记录。

任务：
1. 学习 `pytest` 常用插件（如 `pytest-asyncio`, `pytest-cov`）。
2. 在 `src/study_lab/shared/logging_config.py` 中建立标准日志配置。
3. 确保所有 `print()` 被 `logging` 替代。

验收：
- 测试覆盖率报告生成。
- 运行代码有标准日志输出。

## Day 4：环境管理与 CI/CD 预览

目标：隔离环境并准备自动化。

任务：
1. 配置 `.env` 文件读取示例（使用 `python-dotenv`）。
2. 在 `scripts/` 中编写 `check.sh`，一键运行 lint, format, test。

验收：
- 一个脚本完成全流程检查。
