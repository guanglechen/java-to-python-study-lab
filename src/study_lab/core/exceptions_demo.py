"""Week 1 exercises for explicit exception handling."""

from __future__ import annotations


class InvalidPositiveIntegerError(ValueError):
    """Raised when a value cannot be converted into a positive integer."""


def parse_positive_int(raw_value: str) -> int:
    """Parse a string into a positive integer.

    The function raises a focused domain exception instead of returning many
    status codes or flags.
    """
    try:
        parsed = int(raw_value)
    except ValueError as exc:
        raise InvalidPositiveIntegerError("value must be an integer") from exc

    if parsed <= 0:
        raise InvalidPositiveIntegerError("value must be greater than zero")
    return parsed


def safe_average(raw_values: list[str]) -> float:
    """Return the average of valid positive integers from a list of strings."""
    valid_values = []
    for raw_value in raw_values:
        try:
            valid_values.append(parse_positive_int(raw_value))
        except InvalidPositiveIntegerError:
            continue

    if not valid_values:
        raise InvalidPositiveIntegerError("at least one valid positive integer is required")

    return sum(valid_values) / len(valid_values)