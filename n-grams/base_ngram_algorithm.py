from random import choices

n: int = 3


def setup(ngram: int = 3):
    global n
    n = ngram


def count_transitions(sentences: list[str]) -> dict[tuple[str, ...], dict[str, int]]:
    transitions: dict[tuple[str, ...], dict[str, int]] = dict()

    for sentence in sentences:
        text: list[str] = ("<start> " * (n - 1) + sentence + " <end>").lower().split()

        for i in range(len(text) - n + 1):
            words, next_word = tuple([text[i + j] for j in range(n - 1)]), text[i + n - 1]
            if words not in transitions:
                transitions[words] = {next_word: 1}
                continue

            if next_word not in transitions[words]:
                transitions[words][next_word] = 1
                continue

            transitions[words][next_word] += 1

    return transitions


def calculate_probabilities(transitions: dict[tuple[str, ...], dict[str, int]]) -> dict[tuple[str, ...], dict[str, float]]:
    probabilities: dict[tuple[str, ...], dict[str, float]] = dict()

    for word, next_word_counts in transitions.items():
        probabilities[word] = dict()
        sum_counts: int = sum(next_word_counts.values())

        for next_word, count in next_word_counts.items():
            probabilities[word][next_word] = count / sum_counts

    return probabilities


def generate_text(probabilities: dict[tuple[str, ...], dict[str, float]], steps: int = 10) -> str:
    text: str = ""
    last_words: tuple[str, ...] = tuple(("<start> " * (n - 1)).split())

    for _ in range(steps):
        last_word: str = choices(list(probabilities[last_words].keys()), weights=list(probabilities[last_words].values()))[0]

        if last_word == "<end>":
            return text[1:]

        last_words = tuple(last_words[1:])
        if n >= 2:
            last_words += (last_word, )

        text += " " + last_word

    return text[1:]


if __name__ == "__main__":
    user_input: list[str] = ["кот ест рыбу кот ест корм", "пёс ест мясо пёс ест корм"]
    setup(4)
    result: dict[tuple[str, ...], dict[str, int]] = count_transitions(user_input)
    print(result)
    result: dict[tuple[str, ...], dict[str, float]] = calculate_probabilities(result)
    print(result)
    result: str = generate_text(result)
    print(result)