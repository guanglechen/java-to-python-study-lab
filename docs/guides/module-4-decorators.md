# 模块 4 学习指引：decorators | Module 4 Guide

## 这节学什么

这节重点是“横切逻辑抽离”。

1. 不改业务函数签名，也能加上统计逻辑。
2. 不改业务函数主体，也能加上失败重试。
3. 把重复逻辑从业务代码里拿出来。

## 对应文件

源码：`src/study_lab/shared/decorators.py`

测试：`tests/unit/test_decorators.py`

## 本节两个装饰器

1. `@timed`
- 作用：记录最近一次函数执行耗时
- 关注点：`finally` 保证无论成功失败都能记录耗时

2. `@retry_once`
- 作用：第一次失败后自动重试一次
- 关注点：只重试一次，第二次仍失败就把异常抛出去

## Java 迁移理解

可把装饰器理解为“轻量版 AOP 包装器”：

1. Java 常见做法：AOP 或拦截器统一增强。
2. Python 常见做法：用 `@decorator` 在函数级别做增强。

## 今日练习顺序

1. 先读 `timed`，看它如何不改函数返回值。
2. 再读 `retry_once`，看异常如何被重试逻辑接管。
3. 最后跑测试，观察调用次数断言。

## 建议命令

```bash
/Users/chenguangyue/Documents/code/python/study/.venv/bin/python -m pytest tests/unit/test_decorators.py
```
