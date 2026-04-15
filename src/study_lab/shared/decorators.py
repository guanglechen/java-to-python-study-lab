"""第 2 阶段 Day 3：装饰器示例。 EN: Phase 2 Day 3 decorator demos."""

from __future__ import annotations

from collections.abc import Callable
from functools import wraps
from time import perf_counter
from typing import ParamSpec, Protocol, TypeVar

P = ParamSpec("P")
R = TypeVar("R")
R_co = TypeVar("R_co", covariant=True)


class TimedCallable(Protocol[P, R_co]):
    last_elapsed_ms: float

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R_co: ...


def timed(func: Callable[P, R]) -> TimedCallable[P, R]:
    """记录函数最近一次执行耗时（毫秒）。 EN: Record last execution time in milliseconds."""

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            wrapper.last_elapsed_ms = (perf_counter() - start) * 1000  # type: ignore[attr-defined]

    wrapper.last_elapsed_ms = 0.0  # type: ignore[attr-defined]
    return wrapper  # type: ignore[return-value]


def retry_once(func: Callable[P, R]) -> Callable[P, R]:
    """失败后重试一次。 EN: Retry once if the first call fails."""

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        try:
            return func(*args, **kwargs)
        except Exception:
            return func(*args, **kwargs)

    return wrapper
