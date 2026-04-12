# 模块 2 学习指引：collections_demo | Module 2 Guide

## 这节学什么

这一节不再强调“函数是什么”，而是开始训练 Python 在集合处理上的表达方式。

你要重点体会三件事：

1. Python 处理列表和字典时，代码通常比 Java 更短。
2. 这里的重点不是炫技，而是用更直接的方式表达业务意图。
3. 很多在 Java 里会拆成多步处理的逻辑，在 Python 里一个小循环就够了。

## 对应文件

源码：`src/study_lab/core/collections_demo.py`

测试：`tests/unit/test_collections_demo.py`

## 你现在要看的 3 个函数

### 1. `word_frequencies`

学习点：

- 字符串切分
- 字典计数
- `dict.get` 的用法
- 小循环替代重型对象封装

Java 迁移点：

在 Java 里你可能会先考虑 `Map<String, Integer>` 加一堆判空和分支；在 Python 里可以很轻地完成同样事情。

### 2. `deduplicate_keep_order`

学习点：

- `set` 用于判重
- `list` 保留顺序
- 一边遍历一边构造结果

Java 迁移点：

这很像你在 Java 里用 `LinkedHashSet` 想解决的问题，但 Python 这里更容易把“判重”和“保序”拆清楚。

### 3. `group_scores`

学习点：

- 遍历字典
- 条件分组
- 返回字典结构

Java 迁移点：

你会发现 Python 对这种“小数据整理函数”非常友好，不需要额外定义 VO、Service、Converter 才能开工。

## 推荐学习顺序

1. 先读 `word_frequencies`
2. 再读 `deduplicate_keep_order`
3. 最后读 `group_scores`
4. 再反过来读测试，看测试怎么定义边界

## 你要自己补的思考

读这一节时，重点写下这几个问题的答案：

1. 为什么这里直接返回字典，而不是先包一层结果对象。
2. 为什么 Python 里小循环很多时候比过度抽象更自然。
3. 这几个函数如果用 Java 来写，哪些样板代码是 Python 省掉了的。

## 这节做完的最低标准

1. 你能自己解释 `dict.get(key, default)` 的作用。
2. 你能说清 `set` 为什么适合做判重。
3. 你能自己补 2 到 3 个边界测试。
4. 你能写下至少 3 条 Java 和 Python 在集合处理上的差异。

## 建议命令

```bash
/Users/chenguangyue/Documents/code/python/study/.venv/bin/python -m pytest tests/unit/test_collections_demo.py
```