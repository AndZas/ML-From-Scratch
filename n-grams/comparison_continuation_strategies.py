from random import choice

import base_trigram_algorithm as tr


def choice_with_equal_chances(probabilities: dict[tuple[str, str], dict[str, float]], steps: int = 10) -> str:
    text: str = ""
    last_words: tuple[str, str] = ("<start>", "<start>")

    for _ in range(steps):
        last_word: str = choice(list(probabilities[last_words].keys()))

        if last_word == "<end>":
            return text[1:]

        last_words = (last_words[-1], last_word)
        text += " " + last_word

    return text[1:]


def choice_most_frequent(probabilities: dict[tuple[str, str], dict[str, float]], steps: int = 10) -> str:
    text: str = ""
    last_words: tuple[str, str] = ("<start>", "<start>")

    for _ in range(steps):
        maximum_probability: float = max(probabilities[last_words].values())
        values: list[str] = list()
        for k, v in probabilities[last_words].items():
            if v == maximum_probability:
                values.append(k)

        last_word: str = choice(list(values))

        if last_word == "<end>":
            return text[1:]

        last_words = (last_words[-1], last_word)
        text += " " + last_word

    return text[1:]


if __name__ == "__main__":
    user_input: list[str] = ["кот ест рыбу", "кот ест корм", "пёс ест мясо", "пёс ест корм", "кот ест рыбу", "пёс ест мясо"]
    transitions: dict[tuple[str, str], dict[str, int]] = tr.count_transitions(user_input)
    prob: dict[tuple[str, str], dict[str, float]] = tr.calculate_probabilities(transitions)
    result: str = tr.generate_text(prob)
    print(f"Weighted: {result}")
    result: str = choice_with_equal_chances(prob)
    print(f"Equal:    {result}")
    result: str = choice_most_frequent(prob)
    print(f"Frequent: {result}")
