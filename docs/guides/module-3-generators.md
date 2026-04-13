# 模块 3 学习指引：generators_demo | Module 3 Guide

## 这节要掌握什么

这节的核心不是语法，而是执行时机。

1. list 版本：一次性算完，立即占用内存。
2. generator 版本：按需计算，边迭代边产出。

## 对应文件

源码：`src/study_lab/core/generators_demo.py`

测试：`tests/unit/test_generators_demo.py`

## 必看知识点

1. `yield` 会把函数变成生成器函数。
2. 生成器是一次性迭代流，被消费后不会自动重置。
3. 惰性计算在大数据处理场景更省内存。

## Java 对照理解

你可以把 Python generator 理解成“轻量版 Stream + Iterator 的结合体”：

1. 和 Java Stream 一样，强调按需处理。
2. 和 Java Iterator 一样，有消费过程和状态推进。
3. 但 Python 语法更轻，直接在函数里 `yield` 即可。

## 今日练习顺序

1. 先读 `even_squares_list`。
2. 再读 `even_squares_generator`。
3. 最后读 `first_n_values`，理解流式消费。
4. 跑测试并观察“消费一次后为空”的行为。

## 建议命令

```bash
/Users/chenguangyue/Documents/code/python/study/.venv/bin/python -m pytest tests/unit/test_generators_demo.py
```
