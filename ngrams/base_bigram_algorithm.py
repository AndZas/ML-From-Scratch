from random import choices


def count_transitions(sentences: list[str]) -> dict[str, dict[str, int]]:
    transitions: dict[str, dict[str, int]] = dict()

    for sentence in sentences:
        text: list[str] = ("<start> " + sentence + " <end>").lower().split()

        for i in range(len(text) - 1):
            word, next_word = text[i], text[i + 1]
            if word not in transitions:
                transitions[word] = {next_word: 1}

            else:
                if next_word not in transitions[word]:
                    transitions[word][next_word] = 1

                else:
                    transitions[word][next_word] += 1

    return transitions


def calculate_probabilities(raw_transitions: dict[str, dict[str, int]]) -> dict[str, dict[str, float]]:
    probabilities: dict[str, dict[str, float]] = dict()

    for word, transitions in raw_transitions.items():
        probabilities[word] = dict()

        for next_word, count in transitions.items():
            probabilities[word][next_word] = count / sum(transitions.values())

    return probabilities


def generate_text(probabilities: dict[str, dict[str, float]], first_word: str = "<start>", steps: int = 3) -> str:
    text: str = first_word if first_word != "<start>" else ""
    last_word: str = first_word

    for _ in range(steps):
        last_word = choices(list(probabilities[last_word].keys()), weights=list(probabilities[last_word].values()))[0]

        if last_word == "<end>":
            return text[1:]

        text += " " + last_word

    return text[1:]


if __name__ == "__main__":
    user_input: list[str] = ["кот ест рыбу", "кот ест корм", "пёс ест мясо", "пёс ест корм"]
    result: dict[str, dict[str, int]] = count_transitions(user_input)
    print(result)
    result: dict[str, dict[str, float]] = calculate_probabilities(result)
    print(result)
    user_input: str = input("Enter a start word: ")
    result: str = generate_text(result, user_input, 5)
    print(result)
