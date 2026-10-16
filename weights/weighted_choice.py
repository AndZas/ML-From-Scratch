from random import random


def choices(population: list[str], weights: list[float]) -> str | None:
    last_weight: float = 0.0
    choice: float = random()

    for i in range(len(weights)):
        real_weight: float = weights[i] / sum(weights) + last_weight
        if choice < real_weight:
            return population[i]

        last_weight = real_weight

    return None


if __name__ == "__main__":
    result: str | None = choices(["кот", "сидит", "на", "диване"], [0.1, 0.25, 0.125, 0.125])
    print(result)
