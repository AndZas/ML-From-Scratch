from backoff import *


class TransitionsDict(dict):
    def add(self, n: int, key: tuple, word: str, value: float) -> None:
        if n not in self:
            self[n] = {key: {word: value}}
            return

        if key not in self[n]:
            self[n][key] = {word: value}
            return

        self[n][key] = dict([(k, v) for k, v in self[n][key].items()] + [(word, value)])


def smooth(probabilities: dict[int, dict[tuple[str, ...], dict[str, float]]], lower_limit: float = 1e-10) \
        -> dict[int, dict[tuple[str, ...], dict[str, float]]]:
    smoothed: TransitionsDict = TransitionsDict()

    for n in probabilities.keys():
        words: set[str] = set([j for i in probabilities[n].values() for j in list(i.keys())] +
                              [j for i in probabilities[n].keys() for j in i])
        words.discard("<start>")

        for key in probabilities[n].keys():
            ratio: float = 1 / (1 + lower_limit * (len(words) - len(probabilities[n][key].keys())))

            for word in words:
                if word in probabilities[n][key].keys():
                    smoothed.add(n, key, word, probabilities[n][key][word] * ratio)
                    continue

                smoothed.add(n, key, word, lower_limit * ratio)

    return smoothed


if __name__ == "__main__":
    setup(3)
    user_input: list[str] = ["кот ест рыбу", "кот ест корм", "пёс ест мясо", "пёс ест корм"]
    result: dict[int, dict[tuple[str, ...], dict[str, float]]] = init(user_input)
    result: dict[int, dict[tuple[str, ...], dict[str, float]]] = smooth(result, lower_limit=1e-2)
    print(result)
    result: str = generate_text(result)
    print(result)
