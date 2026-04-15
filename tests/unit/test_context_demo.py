from __future__ import annotations

import time

import pytest

from study_lab.shared.context_demo import TimerContext


def test_timer_context_records_duration_on_normal_exit() -> None:
    with TimerContext() as timer:
        time.sleep(0.001)

    assert timer.exited is True
    assert timer.duration >= 0


def test_timer_context_still_exits_when_exception_happens() -> None:
    timer = TimerContext()

    with pytest.raises(ValueError, match="boom"):
        with timer:
            raise ValueError("boom")

    assert timer.exited is True
    assert timer.duration >= 0


def test_timer_context_as_binding_returns_context_object() -> None:
    with TimerContext() as timer:
        assert isinstance(timer, TimerContext)
        assert timer.start_time > 0
