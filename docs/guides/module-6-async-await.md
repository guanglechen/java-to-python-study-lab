# 模块 6 学习指引：async/await | Module 6 Guide

## 这节学什么

这节重点是“协程并发模型”。

1. 区分同步函数和协程函数。
2. 理解 `await` 的意义：在等待 IO 时让出执行权。
3. 理解 `asyncio.gather`：并发调度多个协程并汇总结果。

## 对应文件

源码：`src/study_lab/core/async_demo.py`

测试：`tests/unit/test_async_demo.py`

## 先建立 4 个核心概念

1. 协程函数
- 用 `async def` 定义，调用后不会立即执行，而是返回协程对象。

2. 事件循环（event loop）
- 负责调度协程何时运行。
- 在这个仓库里你会看到 `asyncio.run(...)` 来启动一次事件循环。

3. await
- 只能在 `async def` 内使用。
- 表示“我现在要等一个可等待对象，同时把控制权还给事件循环”。

4. gather
- `asyncio.gather(a, b, c)` 会并发等待多个协程并返回结果列表。

## 对照 Java 的理解

可以这样迁移理解：

1. Python 协程并发更像 Java 的 `CompletableFuture` 组合流程。
2. 不同点是 Python 的 `await` 写法更线性，代码阅读成本更低。
3. 如果任务是 IO 等待型，协程通常比“每个任务一个线程”更轻量。

## 本节代码里你要重点看什么

### 1) 两个基础协程

- `fetch_user_name(user_id, delay)`
- `fetch_user_score(user_id, delay)`

观察点：

1. 内部都有 `await asyncio.sleep(delay)`，模拟 IO 等待。
2. 返回值分别是字符串和整数，便于测试验证。

### 2) 一个并发汇总函数

- `gather_user_names(user_ids, delay)`

观察点：

1. 先构造协程任务列表。
2. 用 `await asyncio.gather(*tasks)` 并发执行。
3. 返回值顺序与传入任务顺序一致。

### 3) main 手动验证入口

- `main()` 通过 `asyncio.run(gather_user_names(...))` 执行并打印结果。

## 建议学习顺序

1. 先读 `fetch_user_name`，确认协程最小结构。
2. 再读 `gather_user_names`，理解“一个 await 带起多个协程”。
3. 跑测试看行为断言，特别是并发快于串行的测试。
4. 最后运行模块的 `main()` 做一次手动验证。

## 建议命令

```bash
/Users/chenguangyue/Documents/code/python/study/.venv/bin/python -m pytest tests/unit/test_async_demo.py
/Users/chenguangyue/Documents/code/python/study/.venv/bin/python -m study_lab.core.async_demo
```

## 常见坑

1. 在普通 `def` 里写 `await`（语法错误）。
2. 忘记在顶层用 `asyncio.run(...)` 驱动协程。
3. 把 CPU 密集任务当成协程并发优化对象（通常收益很小）。
4. 误以为协程自动并行到多核。协程是并发，不等于多核并行。

## 自检标准

完成本节后，你应该能回答：

1. 为什么 `async def` 调用后返回的是协程对象而不是结果。
2. `await` 到底在“等待”什么。
3. 为什么 `gather` 在 IO 场景通常比串行更快。
4. 协程并发和 Java 线程池并发的核心差异是什么。
