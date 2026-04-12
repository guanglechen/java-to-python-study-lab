# 第 1 阶段日计划：Python 基础 | Phase 1 Day Plan

## 学习范围 | Learning Scope

这个阶段只覆盖 Python 语言基础和标准库使用。

这一阶段不要引入 Web 框架、数据库代码、Redis 或 AI SDK。

EN: This stage only covers Python language basics and standard library usage. Do not add web frameworks, database code, Redis, or AI SDKs in this stage.

## 学习目标 | Learning Objectives

1. 理解 Python 的变量绑定和对象引用。
2. 自然地使用列表、字典和推导式。
3. 用小函数替代沉重的类包装。
4. 有意识地使用异常，而不是写防御式样板代码。
5. 理解 Python 包与导入的组织方式。

## 本地代码目标 | Local Code Targets

### 模块 1：`basics.py` | Module 1

- 编写接近业务风格的小函数。
- 练习默认参数、循环、分支和返回值。

### 模块 2：`collections_demo.py` | Module 2

- 练习列表和字典转换。
- 优先使用推导式或小循环，而不是冗长的对象脚手架。

### 模块 3：`exceptions_demo.py` | Module 3

- 练习自定义异常和受控解析。
- 学会什么时候该抛出异常，什么时候该返回兜底值。

## 执行顺序 | Execution Order

1. 阅读 `src/study_lab/core/` 下的实现文件。
2. 阅读 `tests/unit/` 下的测试文件。
3. 运行测试。
4. 修改一个函数并重新运行测试。
5. 记录你觉得和 Java 最不一样的地方。

## Day 节奏安排 | Day Schedule

1. Day 1：读 `basics.py`，跑 `test_basics.py`，理解参数、返回值、可选参数。
2. Day 2：补 `basics` 边界测试，完成 1 个小改动并回归。
3. Day 3：读 `collections_demo.py`，跑 `test_collections_demo.py`，理解 dict/list/set 的分工。
4. Day 4：补 `collections` 边界测试，记录 Java 与 Python 集合处理差异。
5. Day 5：读 `exceptions_demo.py`，跑 `test_exceptions_demo.py`，理解异常链与业务异常封装。

## 第 1 阶段检查清单 | Phase 1 Checklist

- [ ] 读完第 1 阶段所有源码。
- [ ] 读完第 1 阶段所有测试。
- [ ] 成功运行测试。
- [ ] 能解释为什么这里以函数作为主要构建单元。
- [ ] 能举一个例子解释可变对象和不可变对象。
- [ ] 在 `docs/notes/java-vs-python-notes.md` 中至少补三条自己的迁移笔记。

## 退出标准 | Exit Criteria

到第 1 阶段结束时，你应该能说明：

1. 为什么 Python 代码不需要给每个行为都包一层类。
2. 为什么 Python 的包导入比 Java 的包命名更轻量。
3. 为什么列表和字典转换在 Python 中更简洁。
4. 为什么异常应该表示非法状态，而不是正常流程控制。