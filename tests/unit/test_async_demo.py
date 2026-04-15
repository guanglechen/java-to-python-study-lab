from __future__ import annotations

import asyncio
from time import perf_counter

from study_lab.core.async_demo import fetch_user_name, fetch_user_score, gather_user_names


def test_fetch_user_name_returns_expected_value() -> None:
    assert asyncio.run(fetch_user_name(7, delay=0.0)) == "user-7"


def test_fetch_user_score_returns_expected_value() -> None:
    assert asyncio.run(fetch_user_score(7, delay=0.0)) == 70


def test_gather_user_names_returns_all_values() -> None:
    assert asyncio.run(gather_user_names([1, 2, 3], delay=0.0)) == [
        "user-1",
        "user-2",
        "user-3",
    ]


def test_gather_user_names_is_faster_than_sequential_calls() -> None:
    user_ids = [1, 2, 3]
    delay = 0.03

    start = perf_counter()
    sequential = [asyncio.run(fetch_user_name(user_id, delay=delay)) for user_id in user_ids]
    sequential_elapsed = perf_counter() - start

    start = perf_counter()
    concurrent = asyncio.run(gather_user_names(user_ids, delay=delay))
    concurrent_elapsed = perf_counter() - start

    assert concurrent == sequential
    assert concurrent_elapsed < sequential_elapsed
