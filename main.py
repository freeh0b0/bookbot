from stats import *

def main():
    file_text = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(file_text)
    print(f"{num_words} words found in the document")
    char_count = get_char_count(file_text)
    print(char_count)

main()
