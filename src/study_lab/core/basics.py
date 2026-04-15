"""第 1 周练习：聚焦简单 Python 函数。 EN: Week 1 exercises focused on simple Python functions."""

from __future__ import annotations


def calculate_order_total(prices: list[float], discount_rate: float = 0.0) -> float:
    """计算价格列表的折后总价。 EN: Return the discounted total for a list of prices.

    这个函数故意保持得很小，是为了强调 Python 里很多场景先写函数，
    而不是一上来就写类。

    EN: The function stays intentionally small to reinforce that Python often
    starts with functions rather than classes.
    """
    if prices is None:
        return 0.0
    if discount_rate == 1.0:
        return 0.0
    subtotal = sum(prices)
    discount = subtotal * discount_rate
    return round(subtotal - discount, 2)


def classify_temperature(celsius: int) -> str:
    """把温度值归类成可读标签。 EN: Classify a temperature value into a human-readable label."""
    if celsius < 0:
        return "freezing"
    if celsius < 20:
        return "cool"
    if celsius < 30:
        return "warm"
    return "hot"


def build_greeting(name: str, city: str | None = None) -> str:
    """构造问候语，用可选参数替代重载方法。
    EN: Build a greeting that uses an optional value instead of overloaded methods.
    """
    if city is None:
        return f"Hello, {name}!"
    return f"Hello, {name} from {city}!"
