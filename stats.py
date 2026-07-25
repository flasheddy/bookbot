def get_word_count(text: str) -> int:
    return len(text.split())


def get_char_counts(text: str) -> dict[str, int]:
    counts = {}

    lower_text = text.lower()
    for char in lower_text:
        counts[char] = counts.get(char, 0) + 1

    return counts


def sort_on(char_count: tuple[str, int]) -> int:
    return char_count[1]


def chars_dict_to_sorted_list(char_counts: dict[str, int]) -> list[tuple[str, int]]:
    char_count_list: list[tuple[str, int]] = []

    for char, count in char_counts.items():
        char_count_list.append((char, count))

    return sorted(char_count_list, reverse=True, key=sort_on)
