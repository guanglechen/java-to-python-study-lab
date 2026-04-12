import pytest

from study_lab.core.exceptions_demo import InvalidPositiveIntegerError
from study_lab.core.exceptions_demo import parse_positive_int
from study_lab.core.exceptions_demo import safe_average


def test_parse_positive_int_returns_integer() -> None:
    assert parse_positive_int("42") == 42


def test_parse_positive_int_raises_for_non_integer() -> None:
    with pytest.raises(InvalidPositiveIntegerError, match="integer"):
        parse_positive_int("forty-two")


def test_parse_positive_int_raises_for_non_positive_value() -> None:
    with pytest.raises(InvalidPositiveIntegerError, match="greater than zero"):
        parse_positive_int("0")


def test_safe_average_skips_invalid_values() -> None:
    assert safe_average(["10", "bad", "20"]) == 15.0


def test_safe_average_raises_when_no_valid_values_exist() -> None:
    with pytest.raises(InvalidPositiveIntegerError, match="at least one valid"):
        safe_average(["zero", "-1"])