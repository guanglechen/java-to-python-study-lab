# 模块 5：上下文管理器预热 | Context Manager Warm-up

## 这节要解决什么问题

很多资源都需要“申请 + 释放”成对出现，例如：

- 文件打开后要关闭
- 锁获取后要释放
- 临时计时器开始后要结束记录

如果你手写 try-finally，容易漏写或写散。Python 用 with 把这个模式标准化，降低出错概率。

---

## 核心概念（一句话版本）

1. 上下文管理器：一个对象，进入代码块时执行进入逻辑，离开代码块时执行退出逻辑。
2. with：语法糖，把资源生命周期收口到一个块里。
3. __enter__：进入 with 时调用，返回给 as 后面的变量。
4. __exit__：离开 with 时调用，不管是正常结束还是抛异常都会调用。

---

## 心智模型：with 等价于什么

with manager() as x:
    do_work(x)

大致等价于：

obj = manager()
x = obj.__enter__()
try:
    do_work(x)
finally:
    obj.__exit__(exc_type, exc_val, exc_tb)

要点：即使 do_work 报错，finally 仍然会执行，所以资源更安全。

---

## 和 Java 的对照

- Java try-with-resources：依赖 AutoCloseable.close()
- Python with：依赖 __enter__/__exit__（或 contextlib 的生成器写法）

共同点：都保证退出时释放资源。
差异点：

1. Python 可以很轻量地为“任意临时行为”做上下文管理，不一定是 IO 资源。
2. Python 的 __exit__ 可以决定是否吞掉异常（通常不建议吞，除非你非常明确）。

---

## Day4 推荐实现路径（你可以直接照做）

### 第 1 步：先做一个最小类版本

目标：实现一个计时器上下文管理器。

设计：

- __enter__：记录开始时间，返回 self
- __exit__：记录结束时间、计算耗时
- 暴露 duration 属性，方便测试断言

### 第 2 步：再写异常场景测试

重点不是“没有异常”，而是“有异常也会正确执行 __exit__”。

你可以在 with 块里故意 raise，再断言：

- 资源已释放（或状态已标记）
- 异常仍按预期抛出

### 第 3 步：补一版 contextlib 写法（可选）

使用 @contextmanager，把 enter/exit 放在一个生成器函数里，yield 前是进入，yield 后是退出。

---

## 测试清单（照着写）

1. 正常路径：with 结束后，duration 有值且 >= 0
2. 异常路径：with 内抛错后，清理逻辑仍执行
3. as 绑定：as 返回对象可用（例如能访问 start_time 或 duration）

---

## 常见坑

1. 在 __exit__ 返回 True 导致异常被吞掉（默认应返回 False 或 None）。
2. 把业务逻辑写进 __enter__/__exit__ 太多，导致难测。建议只放生命周期控制。
3. 测试只测正常路径，漏掉异常路径。

---

## 快速模板（类实现）

~~~python
from time import perf_counter


class TimerContext:
    def __init__(self) -> None:
        self.start_time = 0.0
        self.end_time = 0.0
        self.duration = 0.0

    def __enter__(self) -> "TimerContext":
        self.start_time = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.end_time = perf_counter()
        self.duration = self.end_time - self.start_time
        # 返回 None/False: 不吞异常
~~~

---

## 自检标准

完成 Day4 后，你应该能回答：

1. 为什么 with 比散落的 try-finally 更稳。
2. __enter__ 和 __exit__ 分别做什么。
3. 为什么异常路径测试是这节的关键。
