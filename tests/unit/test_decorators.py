from __future__ import annotations

import time

import pytest

from study_lab.shared.decorators import retry_once, timed


def test_timed_returns_original_result() -> None:
    @timed
    def add(a: int, b: int) -> int:
        return a + b

    assert add(2, 3) == 5


def test_timed_records_elapsed_time() -> None:
    @timed
    def tiny_sleep() -> str:
        time.sleep(0.001)
        return "ok"

    assert tiny_sleep() == "ok"
    # 这里通过类型转换告诉 mypy 这是一个带有 last_elapsed_ms 的特殊函数
    assert tiny_sleep.last_elapsed_ms >= 0


def test_retry_once_succeeds_on_second_call() -> None:
    calls = {"count": 0}

    @retry_once
    def flaky() -> str:
        calls["count"] += 1
        if calls["count"] == 1:
            raise RuntimeError("first call fails")
        return "ok"

    assert flaky() == "ok"
    assert calls["count"] == 2


def test_retry_once_raises_when_both_calls_fail() -> None:
    calls = {"count": 0}

    @retry_once
    def always_fail() -> None:
        calls["count"] += 1
        raise RuntimeError("always fail")

    with pytest.raises(RuntimeError, match="always fail"):
        always_fail()

    assert calls["count"] == 2


def test_retry_once_does_not_retry_when_successful() -> None:
    calls = {"count": 0}

    @retry_once
    def stable() -> int:
        calls["count"] += 1
        return 42

    assert stable() == 42
    assert calls["count"] == 1
