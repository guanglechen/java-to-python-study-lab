from study_lab.core.generators_demo import even_squares_generator
from study_lab.core.generators_demo import even_squares_list
from study_lab.core.generators_demo import first_n_values


def test_even_squares_list_returns_all_even_squares() -> None:
    assert even_squares_list([1, 2, 3, 4, 5, 6]) == [4, 16, 36]


def test_even_squares_generator_produces_same_values_as_list_version() -> None:
    numbers = [1, 2, 3, 4, 5, 6]
    assert list(even_squares_generator(numbers)) == even_squares_list(numbers)


def test_even_squares_generator_is_consumed_once() -> None:
    stream = even_squares_generator([2, 4])
    assert list(stream) == [4, 16]
    assert list(stream) == []


def test_first_n_values_reads_partial_stream() -> None:
    stream = even_squares_generator([1, 2, 3, 4, 5, 6])
    assert first_n_values(stream, 2) == [4, 16]
    assert list(stream) == [36]


def test_first_n_values_handles_short_stream() -> None:
    stream = even_squares_generator([1, 3, 5])
    assert first_n_values(stream, 3) == []
