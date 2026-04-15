"""第 1 周练习：显式异常处理。 EN: Week 1 exercises for explicit exception handling."""

from __future__ import annotations


class InvalidPositiveIntegerError(ValueError):
    """当值无法转换为正整数时抛出。
    EN: Raised when a value cannot be converted into a positive integer.
    """


def parse_positive_int(raw_value: str) -> int:
    """把字符串解析成正整数。 EN: Parse a string into a positive integer.

    这里选择抛出聚焦的领域异常，而不是返回一堆状态码或标记位。

    EN: The function raises a focused domain exception instead of returning many
    status codes or flags.
    """
    try:
        parsed = int(raw_value)
    except ValueError as exc:
        raise InvalidPositiveIntegerError("值必须是整数 | value must be an integer") from exc

    if parsed <= 0:
        raise InvalidPositiveIntegerError("值必须大于 0 | value must be greater than zero")
    return parsed


def safe_average(raw_values: list[str]) -> float:
    """计算字符串列表中有效正整数的平均值。
    EN: Return the average of valid positive integers from a list of strings.
    """
    valid_values = []
    for raw_value in raw_values:
        try:
            valid_values.append(parse_positive_int(raw_value))
        except InvalidPositiveIntegerError:
            continue

    if not valid_values:
        raise InvalidPositiveIntegerError(
            "至少需要一个有效正整数 | at least one valid positive integer is required"
        )

    return sum(valid_values) / len(valid_values)
