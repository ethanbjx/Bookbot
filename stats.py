import sys

def process_book(book_path):
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    char_freq = count_chars(text)
    sorted_char = sorted(char_freq.items(), key=sort_on, reverse=True)

    for char, count in sorted_char:
        print(f"{char}: {count}")

    print("============= END ===============")

def get_book_text(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        sys.exit(1)

def get_num_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char != " ":
            char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_on(item):
    return item[1]

