def pure_function(values: list[int]) -> int:
    return sum(values)


def file_io_case(value: str) -> None:
    with open("output.txt", "w") as file:
        file.write(value)


def global_mutation_case(value: int) -> int:
    global GLOBAL_VALUE

    GLOBAL_VALUE = value

    return GLOBAL_VALUE


def network_case(url: str):
    import requests

    return requests.get(url).text


class Counter:
    def __init__(self):
        self.value = 0

    def mutate_self_case(self) -> int:
        self.value += 1
        return self.value

def hidden_side_effect_case(value: int) -> int:
    return helper_with_side_effect(value)


def helper_with_side_effect(value: int) -> int:
    with open("hidden.txt", "w") as file:
        file.write(str(value))

    return value