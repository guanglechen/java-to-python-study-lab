"""Week 1 exercises focused on simple Python functions."""

from __future__ import annotations


def calculate_order_total(prices: list[float], discount_rate: float = 0.0) -> float:
    """Return the discounted total for a list of prices.

    The function stays intentionally small to reinforce that Python often starts
    with functions rather than classes.
    """
    subtotal = sum(prices)
    discount = subtotal * discount_rate
    return round(subtotal - discount, 2)


def classify_temperature(celsius: int) -> str:
    """Classify a temperature value into a small human-readable label."""
    if celsius < 0:
        return "freezing"
    if celsius < 20:
        return "cool"
    if celsius < 30:
        return "warm"
    return "hot"


def build_greeting(name: str, city: str | None = None) -> str:
    """Build a greeting that uses an optional value instead of overloaded methods."""
    if city is None:
        return f"Hello, {name}!"
    return f"Hello, {name} from {city}!"