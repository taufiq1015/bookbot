import sys

from stats import count_words, get_book_text, count_char, dict_sort

def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    file = get_book_text(filepath)
    word_count = count_words(file)
    char_count = count_char(file)
    sorted_list_dict = dict_sort(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list_dict:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}\n")
        else:
            pass
    print("============= END ===============")

main()