import base_unigram_algorithm as ur
import base_bigram_algorithm as br
import base_trigram_algorithm as tr


def main() -> None:
    user_input: list[str] = ["кот ест рыбу", "кот ест корм", "пёс ест мясо", "пёс ест корм"]

    ur_transitions = ur.count_frequency(user_input)
    br_transitions = br.count_transitions(user_input)
    tr_transitions = tr.count_transitions(user_input)

    ur_probabilities = ur.calculate_probabilities(ur_transitions)
    br_probabilities = br.calculate_probabilities(br_transitions)
    tr_probabilities = tr.calculate_probabilities(tr_transitions)

    ur_generated_text = ur.generate_text(ur_probabilities)
    br_generated_text = br.generate_text(br_probabilities)
    tr_generated_text = tr.generate_text(tr_probabilities)

    print(ur_probabilities)
    print(br_probabilities)
    print(tr_probabilities)

    print(ur_generated_text)
    print(br_generated_text)
    print(tr_generated_text)


if __name__ == "__main__":
    main()
