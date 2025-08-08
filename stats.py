def get_book_text(file_path):
    with open(file_path) as f:
        file_text = f.read()
    return file_text

def get_num_words(file_text):
    words = file_text.split()
    return len(words)

def get_char_count(file_text):
    char_count = {}
    for char in file_text.lower():
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    return char_count       

def sort_on(items):
    return items["num"]

def get_sorted_count(char_count):
    chars = []
    for c in char_count:
        item = {}
        item["char"] = c
        item["num"] = char_count[c]
        chars.append(item)
    chars.sort(reverse=True, key=sort_on)

    return chars
