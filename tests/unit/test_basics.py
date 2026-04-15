from study_lab.core.basics import build_greeting, calculate_order_total, classify_temperature


def test_calculate_order_total_with_empty_prices() -> None:
    assert calculate_order_total([]) == 0.0


def test_calculate_order_total_with_discount() -> None:
    assert calculate_order_total([100.0, 50.0], discount_rate=0.1) == 135.0


def test_calculate_order_total_without_discount() -> None:
    assert calculate_order_total([19.99, 10.01]) == 30.0


def test_classify_temperature_ranges() -> None:
    assert classify_temperature(-3) == "freezing"
    assert classify_temperature(12) == "cool"
    assert classify_temperature(24) == "warm"
    assert classify_temperature(33) == "hot"


def test_build_greeting_with_optional_city() -> None:
    assert build_greeting("Alice") == "Hello, Alice!"
    assert build_greeting("Bob", city="Shanghai") == "Hello, Bob from Shanghai!"
