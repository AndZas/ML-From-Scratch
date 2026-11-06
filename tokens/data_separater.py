def separate_data(sentences: list[str]) -> tuple[list[str], list[str]]:
    separated: int = max(len(sentences) // 4, 1)
    return sentences[:-separated], sentences[-separated:]


if __name__ == "__main__":
    user_input: list[str] = ["Кот ест рыбу.", "Кот ест корм.", "Пёс ест мясо.", "Пёс ест корм."]
    print(separate_data(user_input))
