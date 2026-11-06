from data_separater import separate_data
from ngrams.base_trigram_algorithm import count_transitions, calculate_probabilities


def calculate_next_token_probability(
        raw_probabilities: dict[tuple[str, str], dict[str, float]],
        context: tuple[str, str], next_token: str) -> float:

    if context not in raw_probabilities.keys():
        return 0

    if next_token not in raw_probabilities[context].keys():
        return 0

    return raw_probabilities[context][next_token]


def calculate_full_context_probabilities(
        raw_probabilities: dict[tuple[str, str], dict[str, float]],
        raw_context: str) -> dict[tuple[str, str], dict[str, float]]:

    sentences: list[str] = ("<start> <start> " + raw_context + " <end>").lower().split()
    tokens_probabilities: dict[tuple[str, str], dict[str, float]] = dict()

    for i in range(len(sentences) - 2):
        context: tuple[str, str] = (sentences[i], sentences[i + 1])
        next_token: str = sentences[i + 2]
        tokens_probabilities[context] = {next_token: calculate_next_token_probability(raw_probabilities, context, next_token)}

    return tokens_probabilities


if __name__ == '__main__':
    user_input: list[str] = ["Кот ест рыбу.", "Кот ест корм.", "Пёс ест мясо.", "Пёс ест корм."]

    training_data, test_data = separate_data(user_input)
    transitions: dict[tuple[str, str], dict[str, int]] = count_transitions(training_data)
    probabilities: dict[tuple[str, str], dict[str, float]] = calculate_probabilities(transitions)

    print(f"Probabilities: {probabilities}")
    print(f"Next Token Probabilities: {calculate_full_context_probabilities(probabilities, training_data[-1])}")
    print(f"Next Token Probabilities: {calculate_full_context_probabilities(probabilities, test_data[-1])}")
