def contains_duplicate_slow(numbers: list[int]) -> bool:
    for index, number in enumerate(numbers):
        if number in numbers[index + 1:]:
            return True
    return False


def dedupe_preserve_order_slow(items: list[int]) -> list[int]:
    result = []

    for item in items:
        if item not in result:
            result.append(item)

    return result


def repeated_sort_slow(values: list[int]) -> int:
    total = 0

    for _ in range(100):
        sorted_values = sorted(values)
        total += sorted_values[0] if sorted_values else 0

    return total


def build_string_slow(words: list[str]) -> str:
    result = ""

    for word in words:
        result += word + ","

    return result


def repeated_computation_slow(values: list[int]) -> list[int]:
    result = []

    for value in values:
        maximum = max(values) if values else 0
        result.append(value + maximum)

    return result


def count_members_slow(
    values: list[int],
    allowed: list[int],
) -> int:
    count = 0

    for value in values:
        if value in allowed:
            count += 1

    return count