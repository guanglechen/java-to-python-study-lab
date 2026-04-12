# 第 2 阶段日计划：Pythonic 进阶（Java 加速版） | Phase 2 Day Plan

## 适用人群

你已有扎实 Java 工程经验，希望快速完成 Python 进阶能力补齐。

## 节奏建议

总计 5 天，每天 1.5 到 2.5 小时，全部以“代码 + 测试 +笔记”方式完成。

## Day 1：dataclass 与类型标注进阶

目标：掌握 Python 中轻量数据模型的写法。

任务：

1. 新建 `src/study_lab/shared/models.py`，定义 2 个 dataclass。
2. 增加 `Optional`、`list[str]`、`dict[str, int]` 类型标注示例。
3. 新建 `tests/unit/test_models.py`，覆盖构造、默认值和字段访问。

验收：

1. 能解释 dataclass 与 Java POJO/record 的差异。
2. 单测通过。

## Day 2：生成器与迭代器

目标：理解惰性计算和内存友好处理。

任务：

1. 新建 `src/study_lab/core/generators_demo.py`。
2. 实现 2 个函数：一个返回 list，一个 yield 生成器。
3. 新建 `tests/unit/test_generators_demo.py`，对比输出一致性。

验收：

1. 能说明什么时候用 list，什么时候用 generator。
2. 单测通过。

## Day 3：装饰器

目标：掌握横切逻辑抽离。

任务：

1. 新建 `src/study_lab/shared/decorators.py`。
2. 实现 `@timed`（统计耗时）和 `@retry_once`（失败重试一次）示例。
3. 新建 `tests/unit/test_decorators.py`。

验收：

1. 能解释装饰器和 Java AOP 的异同。
2. 单测通过。

## Day 4：上下文管理器

目标：掌握资源生命周期控制。

任务：

1. 新建 `src/study_lab/shared/context_demo.py`。
2. 写一个 `with` 资源管理示例（例如临时计时器或文件包装器）。
3. 新建 `tests/unit/test_context_demo.py`。

验收：

1. 能解释 `with` 与 try-finally 的关系。
2. 单测通过。

## Day 5：async/await 基础

目标：建立协程心智模型。

任务：

1. 新建 `src/study_lab/core/async_demo.py`。
2. 实现 2 个协程函数和 1 个并发 gather 示例。
3. 新建 `tests/unit/test_async_demo.py`（使用 `pytest.mark.asyncio`）。

验收：

1. 能解释同步函数、协程函数、事件循环三者关系。
2. 单测通过。

## 每日固定动作

1. 跑当日新增测试。
2. 更新 `docs/notes/java-vs-python-notes.md` 至少 2 条迁移结论。
3. 更新 `docs/tracking/progress.md` 的当前阶段和下一步。

## 完成标准

1. 第 2 阶段新增代码全部测试通过。
2. 你能用 Java 视角解释 dataclass、decorator、context manager、async 的工程价值。
3. 你能说清楚 Pythonic 写法和“Java 直译写法”的边界。