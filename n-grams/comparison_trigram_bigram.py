import base_bigram_algorithm as br
import base_trigram_algorithm as tr


def main() -> None:
    user_input: list[str] = ["кот ест рыбу", "кот ест корм", "пёс ест мясо", "пёс ест корм"]

    br_transitions = br.count_transitions(user_input)
    tr_transitions = tr.count_transitions(user_input)

    br_probabilities = br.calculate_probabilities(br_transitions)
    tr_probabilities = tr.calculate_probabilities(tr_transitions)

    br_generated_text = br.generate_text(br_probabilities)
    tr_generated_text = tr.generate_text(tr_probabilities)

    print(br_probabilities)
    print(tr_probabilities)

    print(br_generated_text)
    print(tr_generated_text)


if __name__ == "__main__":
    main()
