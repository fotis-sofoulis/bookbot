import sys
from stats import get_book_text, count_words, count_char, sorted_count_dict

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book = get_book_text(path)
    word_count = count_words(book)
    sorted_count_char = sorted_count_dict(count_char(book))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_count_char:
        value = item[1]
        if item[0].isalpha():
            print(f"{item[0]}: {value}")
    print("============= END ===============")

main()
