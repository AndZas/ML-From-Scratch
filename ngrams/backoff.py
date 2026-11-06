from random import choices

import base_ngram_algorithm as nr


global_n: int = 3


def setup(n: int) -> None:
    global global_n
    global_n = n


def init(sentences: list[str], n: int = None) -> dict[int, dict[tuple[str, ...], dict[str, float]]]:
    probabilities: dict[int, dict[tuple[str, ...], dict[str, float]]] = {}
    n = n if n is not None else global_n

    for i in range(n, 0, -1):
        probabilities[i] = nr.calculate_probabilities(nr.count_transitions(sentences, i))

    return probabilities


def generate_text(probabilities: dict[int, dict[tuple[str, ...], dict[str, float]]], context: tuple[str, ...] = None, steps: int = 10, n: int = None) -> str:
    text: str = ""
    n = n if n is not None else global_n
    current_n: int = n
    last_words: tuple[str, ...] = tuple(("<start> " * (n - 1)).split()) if context is None else context

    for _ in range(steps):
        while last_words not in probabilities[current_n]:
            if len(last_words) < current_n:
                current_n -= 1

            if len(last_words) > current_n - 1:
                last_words = last_words[len(last_words) - current_n + 1:]

        last_word: str = choices(list(probabilities[current_n][last_words].keys()), weights=list(probabilities[current_n][last_words].values()))[0]
        current_n = n

        if last_word == "<end>":
            return text[1:]

        if len(last_words) >= n - 1:
            last_words = tuple(last_words[1:])

        if current_n >= 2:
            last_words += (last_word,)

        text += " " + last_word

    return text[1:]


if __name__ == "__main__":
    setup(5)
    user_input: list[str] = ["старый кот обычно ест рыбу утром у окна",
                             "молодой пёс обычно ест мясо вечером у дома",
                             "рыжий кот всегда ест корм утром после прогулки",
                             "чёрный пёс всегда ест корм вечером после прогулки"]
    result: dict[int, dict[tuple[str, ...], dict[str, float]]] = init(user_input)
    result: str = generate_text(result, context=("молодой", "пёс"))
    print(result)
