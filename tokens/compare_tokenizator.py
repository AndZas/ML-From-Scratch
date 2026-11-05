
def tokenize_by_words(sentences: list[str]) -> list[str]:
    tokens: list[str] = list()

    for sentence in sentences:
        for word in sentence.lower().split():
            tokens.append(word)

    return tokens


def tokenize_by_symbols(sentences: list[str]) -> list[str]:
    tokens: list[str] = list()

    for sentence in sentences:
        for symbol in sentence.lower():
            tokens.append(symbol)

    return tokens


if __name__ == "__main__":
    user_input: list[str] = ["Кот ест рыбу.", "Кот ест корм.", "Пёс ест мясо.", "Кота кормит пёс."]
    words_tokens: list[str] = tokenize_by_words(user_input)
    symbols_tokens: list[str] = tokenize_by_symbols(user_input)
    unic_words: set[str] = set(words_tokens)
    unic_symbols: set[str] = set(symbols_tokens)

    print(f"Tokenize by words ({len(unic_words)}/{len(words_tokens)}):\nDictionary: {words_tokens}\nUnic: {unic_words}")
    print(f"Tokenize by symbols ({len(unic_symbols)}/{len(symbols_tokens)}):\nDictionary: {symbols_tokens}\nUnic: {unic_symbols}")
