import sys
from stats import *

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        file_text = get_book_text(file_path)
    except FileNotFoundError:
        print("File could not be found")
        sys.exit(1)
    except IsADirectoryError:
        print("Path points to a directory")
        sys.exit(1)
    except Exception as e:
        print("Unexpected Error:", e)
        sys.exit(1)

    word_count = get_num_words(file_text)
    char_count = get_char_count(file_text)
    sorted_count = get_sorted_count(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for c in sorted_count:
        if c["char"].isalpha():     #c is a dictionary with keys "char" and "num"
            char = c["char"]
            num = c["num"]
            print(f"{char}: {num}")

    print("============= END ===============")

main()
