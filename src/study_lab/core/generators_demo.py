"""第 2 阶段 Day 2：生成器与迭代器示例。 EN: Phase 2 Day 2 generator and iterator demos."""

from __future__ import annotations

from collections.abc import Iterator


def even_squares_list(numbers: list[int]) -> list[int]:
    """返回偶数平方列表。 EN: Return squared values for even numbers as a list."""
    return [number * number for number in numbers if number % 2 == 0]


def even_squares_generator(numbers: list[int]) -> Iterator[int]:
    """按需产出偶数平方。 EN: Lazily yield squared values for even numbers."""
    for number in numbers:
        if number % 2 == 0:
            yield number * number


def first_n_values(stream: Iterator[int], n: int) -> list[int]:
    """从迭代流中读取前 n 项。 EN: Consume first n values from an iterator stream."""
    values: list[int] = []
    for _ in range(n):
        try:
            values.append(next(stream))
        except StopIteration:
            break
    return values
