import random


def count_frequency(sentences: list[str]) -> dict[str, int]:
    transitions: dict[str, int] = {}

    for sentence in sentences:
        text: list[str] = (sentence + " <end>").lower().split()

        for word in text:
            if word not in transitions:
                transitions[word] = 1
                continue

            transitions[word] += 1

    return transitions


def calculate_probabilities(transitions: dict[str, int]) -> dict[str, float]:
    probabilities: dict[str, float] = {}
    sum_counts: int = sum(transitions.values())

    for word, count in transitions.items():
        probabilities[word] = count / sum_counts

    return probabilities


def generate_text(probabilities: dict[str, float], steps: int = 3) -> str:
    text: str = ""

    for _ in range(steps):
        last_word: str = random.choices(list(probabilities.keys()), weights=list(probabilities.values()))[0]

        if last_word == "<end>":
            return text[1:]

        text += " " + last_word

    return text[1:]


if __name__ == "__main__":
    user_input: list[str] = ["кот ест рыбу", "кот ест корм", "пёс ест мясо", "пёс ест корм"]
    result: dict[str, int] = count_frequency(user_input)
    print(result)
    result: dict[str, float] = calculate_probabilities(result)
    print(result)
    result: str = generate_text(result, steps=10)
    print(result)
