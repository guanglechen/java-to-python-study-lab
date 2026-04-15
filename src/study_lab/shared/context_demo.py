"""第 2 阶段 Day 4：上下文管理器示例。 EN: Phase 2 Day 4 context manager demos."""

from __future__ import annotations

from time import perf_counter, sleep


class TimerContext:
    """用于 with 语句的简易计时器。 EN: A small timer context manager."""

    def __init__(self) -> None:
        self.start_time = 0.0
        self.end_time = 0.0
        self.duration = 0.0
        self.exited = False

    def __enter__(self) -> TimerContext:
        self.start_time = perf_counter()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: object | None,
    ) -> None:
        self.end_time = perf_counter()
        self.duration = self.end_time - self.start_time
        self.exited = True


def main() -> None:
    """手动验证上下文管理器行为。 EN: Manual check for context manager behavior."""
    with TimerContext() as timer:
        sleep(0.01)

    print(f"duration={timer.duration:.6f}s")
    print(f"exited={timer.exited}")


if __name__ == "__main__":
    main()
