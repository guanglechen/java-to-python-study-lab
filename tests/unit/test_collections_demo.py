from study_lab.core.collections_demo import deduplicate_keep_order, group_scores, word_frequencies


def test_word_frequencies_normalizes_case_and_punctuation() -> None:
    text = "Python, python! Java? python."
    assert word_frequencies(text) == {"python": 3, "java": 1}


def test_word_frequencies_returns_empty_dict_for_empty_text() -> None:
    assert word_frequencies("") == {}


def test_deduplicate_keep_order_preserves_first_occurrence() -> None:
    values = ["redis", "mysql", "redis", "kafka", "mysql"]
    assert deduplicate_keep_order(values) == ["redis", "mysql", "kafka"]


def test_deduplicate_keep_order_returns_empty_list_for_empty_input() -> None:
    assert deduplicate_keep_order([]) == []


def test_group_scores_splits_names_into_bands() -> None:
    scores = {"Ann": 92, "Ben": 81, "Cara": 70}
    assert group_scores(scores) == {
        "excellent": ["Ann"],
        "good": ["Ben"],
        "needs_work": ["Cara"],
    }


def test_group_scores_handles_boundary_values() -> None:
    scores = {"A": 90, "B": 75, "C": 74}
    assert group_scores(scores) == {
        "excellent": ["A"],
        "good": ["B"],
        "needs_work": ["C"],
    }


def test_group_scores_returns_empty_bands_for_empty_input() -> None:
    assert group_scores({}) == {
        "excellent": [],
        "good": [],
        "needs_work": [],
    }
