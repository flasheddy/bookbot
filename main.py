import sys

from stats import chars_dict_to_sorted_list, get_char_counts, get_word_count


def get_book_text(path: str) -> str:
    with open(path, "r") as f:
        return f.read()


def print_report(path: str, word_count: int, sorted_char_counts: list[tuple[str, int]]) -> None:
    header_lns = [
        "============ BOOKBOT ============",
        f"Analyzing book found at {path}..."
    ]

    word_count_lns = [
        "----------- Word Count ----------",
        f"Found {word_count} total words"
    ]

    sorted_alpha_lns = [f"{char}: {count}" for char, count in sorted_char_counts if char.isalpha()]
    char_count_lns = [
        "--------- Character Count -------",
    ] + sorted_alpha_lns

    end_lns = ["============= END ==============="]

    report_lns = header_lns + word_count_lns + char_count_lns + end_lns
    print("\n".join(report_lns))


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_counts = get_char_counts(text)
    sorted_char_counts = chars_dict_to_sorted_list(char_counts)

    print_report(book_path, word_count, sorted_char_counts)


main()
