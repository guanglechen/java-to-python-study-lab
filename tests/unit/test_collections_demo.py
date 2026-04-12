from study_lab.core.collections_demo import deduplicate_keep_order
from study_lab.core.collections_demo import group_scores
from study_lab.core.collections_demo import word_frequencies


def test_word_frequencies_normalizes_case_and_punctuation() -> None:
    text = "Python, python! Java? python."
    assert word_frequencies(text) == {"python": 3, "java": 1}


def test_deduplicate_keep_order_preserves_first_occurrence() -> None:
    values = ["redis", "mysql", "redis", "kafka", "mysql"]
    assert deduplicate_keep_order(values) == ["redis", "mysql", "kafka"]


def test_group_scores_splits_names_into_bands() -> None:
    scores = {"Ann": 92, "Ben": 81, "Cara": 70}
    assert group_scores(scores) == {
        "excellent": ["Ann"],
        "good": ["Ben"],
        "needs_work": ["Cara"],
    }