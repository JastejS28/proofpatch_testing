def duplicate_name(value: int) -> int:
    return value * 2


class Example:
    def duplicate_name(self, value: int) -> int:
        return value * 3

def outer(value: int) -> int:
    def nested_target(number: int) -> int:
        return number * 2

    return nested_target(value)

async def async_target(value: int) -> int:
    return value * 2

def simple_decorator(function):
    return function


@simple_decorator
def decorated_target(value: int) -> int:
    return value * 2

def defaults_case(
    values: list[int],
    multiplier: int = 2,
) -> list[int]:
    return [
        value * multiplier
        for value in values
    ]

def keyword_only_case(
    values: list[int],
    *,
    reverse: bool = False,
) -> list[int]:
    return sorted(
        values,
        reverse=reverse,
    )

def annotated_case(
    values: list[int] | None,
) -> int | None:
    if values is None:
        return None

    return sum(values)

