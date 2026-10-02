from optimization_cases import (
    build_string_slow,
    contains_duplicate_slow,
    count_members_slow,
    dedupe_preserve_order_slow,
    repeated_computation_slow,
    repeated_sort_slow,
)


def test_contains_duplicate_true():
    assert contains_duplicate_slow(
        [1, 2, 3, 2]
    ) is True


def test_contains_duplicate_false():
    assert contains_duplicate_slow(
        [1, 2, 3, 4]
    ) is False


def test_contains_duplicate_empty():
    assert contains_duplicate_slow([]) is False


def test_dedupe_preserves_order():
    assert dedupe_preserve_order_slow(
        [3, 1, 3, 2, 1]
    ) == [3, 1, 2]


def test_repeated_sort_empty():
    assert repeated_sort_slow([]) == 0


def test_build_string():
    assert build_string_slow(
        ["a", "b"]
    ) == "a,b,"


def test_repeated_computation():
    assert repeated_computation_slow(
        [1, 2, 3]
    ) == [4, 5, 6]


def test_count_members():
    assert count_members_slow(
        [1, 2, 3, 4],
        [2, 4],
    ) == 2