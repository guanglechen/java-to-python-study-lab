# Java vs Python 迁移笔记 | Migration Notes

这个文件是持续维护的迁移日志，核心用中文记录，必要时补英文关键词。

EN: Use this file as a running migration log. Keep Chinese as the main language and add English keywords when useful.

## 第 1 阶段起步笔记 | Phase 1 Starter Notes

1. Python 变量是对象名称绑定，不是带静态类型的值槽位。 EN: name binding, not typed slots.
2. Python 里很多行为直接写函数就够了，不需要先抽一个 service class。 EN: functions first.
3. 列表推导式和字典推导式能替代很多冗长的循环和临时变量。 EN: comprehensions.
4. Python 的包结构更轻，不需要坚持 Java 那种每个类单独文件的习惯。 EN: lightweight package layout.
5. 异常应该表示真正的非法状态，而不是把所有分支都包成 try-catch。 EN: exceptions for invalid states.

## 继续补充 | Add Your Own Notes

- Python 的协程并发与 Java 线程池不同：协程是单线程事件循环（基于非阻塞 IO），而 Java 线程池是多线程并发。
- Python 中处理“等待多个任务”最直接的对应物是 `asyncio.gather`，其语义比 Java 的 `CompletableFuture.allOf` 更简洁。