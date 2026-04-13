"""第 2 阶段 Day 3：装饰器示例。 EN: Phase 2 Day 3 decorator demos."""

from __future__ import annotations

from functools import wraps
from time import perf_counter
from typing import Callable
from typing import ParamSpec
from typing import TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def timed(func: Callable[P, R]) -> Callable[P, R]:
    """记录函数最近一次执行耗时（毫秒）。 EN: Record last execution time in milliseconds."""

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            wrapper.last_elapsed_ms = (perf_counter() - start) * 1000

    wrapper.last_elapsed_ms = 0.0
    return wrapper


def retry_once(func: Callable[P, R]) -> Callable[P, R]:
    """失败后重试一次。 EN: Retry once if the first call fails."""

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        try:
            return func(*args, **kwargs)
        except Exception:
            return func(*args, **kwargs)

    return wrapper
