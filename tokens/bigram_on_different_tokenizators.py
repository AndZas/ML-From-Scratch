from random import choices


def count_transitions(sentences: list[str], by_words: bool = True) -> dict[str, dict[str, int]]:
    transitions: dict[str, dict[str, int]] = dict()

    for sentence in sentences:
        if by_words:
            text: list[str] = ("<start> " + sentence + " <end>").lower().split()
        else:
            text: str = "S" + sentence.lower() + "E"

        for i in range(len(text) - 1):
            token, next_token = text[i], text[i + 1]
            if token not in transitions:
                transitions[token] = {next_token: 1}
                continue

            if next_token not in transitions[token]:
                transitions[token][next_token] = 1
                continue

            transitions[token][next_token] += 1

    return transitions


def calculate_probabilities(raw_transitions: dict[str, dict[str, int]]) -> dict[str, dict[str, float]]:
    probabilities: dict[str, dict[str, float]] = dict()

    for token, transitions in raw_transitions.items():
        probabilities[token] = dict()

        for next_token, count in transitions.items():
            probabilities[token][next_token] = count / sum(transitions.values())

    return probabilities


def generate_text(probabilities: dict[str, dict[str, float]]) -> str:
    if len(list(probabilities.keys())[0]) > 1:
        last_token: str = "<start>"
        by_words: bool = True
    else:
        last_token: str = "S"
        by_words: bool = False

    text: str = ""

    while True:
        last_token = choices(list(probabilities[last_token].keys()), weights=list(probabilities[last_token].values()))[0]

        if last_token in ["<end>", "E"]:
            return text[1:] if by_words else text

        text += " " + last_token if by_words else last_token


if __name__ == "__main__":
    user_input: list[str] = ["Кот ест рыбу.", "Кот ест корм.", "Пёс ест мясо.", "Кота кормит пёс."]
    words_transitions: dict[str, dict[str, int]] = count_transitions(user_input)
    symbols_transitions: dict[str, dict[str, int]] = count_transitions(user_input, False)
    words_probabilities: dict[str, dict[str, float]] = calculate_probabilities(words_transitions)
    symbols_probabilities: dict[str, dict[str, float]] = calculate_probabilities(symbols_transitions)

    print(generate_text(words_probabilities))
    print(generate_text(symbols_probabilities))
