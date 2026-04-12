"""第 1 周练习：列表和字典转换。 EN: Week 1 exercises for list and dictionary transformations."""

from __future__ import annotations


def word_frequencies(text: str) -> dict[str, int]:
    """以大小写不敏感的方式统计词频。 EN: Count words in a case-insensitive way.

    这个函数想说明一件事：和很多 Java 写法相比，一个小循环往往比堆一组
    辅助对象更直接、更清楚。

    EN: This function demonstrates that a small loop is often clearer than
    building multiple helper objects as you might in a Java implementation.
    """
    frequencies: dict[str, int] = {}
    for raw_word in text.split():
        word = raw_word.strip(".,!?;:").lower()
        if not word:
            continue
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def deduplicate_keep_order(values: list[str]) -> list[str]:
    """去重并保留首次出现顺序。 EN: Return values without duplicates while preserving first-seen order."""
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        ordered.append(value)
    return ordered


def group_scores(scores: dict[str, int]) -> dict[str, list[str]]:
    """按简单成绩区间分组学生姓名。 EN: Group student names into simple performance bands."""
    bands = {"excellent": [], "good": [], "needs_work": []}
    for name, score in scores.items():
        if score >= 90:
            bands["excellent"].append(name)
        elif score >= 75:
            bands["good"].append(name)
        else:
            bands["needs_work"].append(name)
    return bands