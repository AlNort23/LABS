import os
import random
import json

HOW_MANY_BOOK = 3
LINE = 128
PAGE = 64
pages = {}
page_number = 0
line_window = {}
line_number = 0
char_window = []


def clean_line(line):
    return line.strip().replace('-', '') + ' '


def process_char(char):
    global char_window
    char_window.append(char)
    if len(char_window) == LINE:
        add_line()


def add_line():
    global char_window, line_number
    line_number += 1
    process_page(''.join(char_window), line_number)
    char_window.clear()


def process_page(line, line_num):
    global line_window, pages, page_number
    line_window[line_num] = line
    if len(line_window) == PAGE:
        add_page()


def add_page():
    global line_number, line_window, pages, page_number
    page_number += 1
    pages[page_number] = dict(line_window)
    line_window.clear()
    line_number = 0


def read_book(file_path):
    global char_window
    print(f"Processing book: {file_path}")
    with open(file_path, 'r', encoding='utf-8-sig') as fp:
        all_chars = []
        for line in fp:
            line = clean_line(line)
            if line.strip():
                all_chars.extend(list(line))

        random.shuffle(all_chars)

        for char in all_chars:
            process_char(char)

    if len(char_window) > 0:
        add_line()
    if len(line_window) > 0:
        add_page()


def process_books(*paths):
    print(f"\nStarting to process {len(paths)} books...\n")

    for path in paths:
        try:
            read_book(path)
        except FileNotFoundError:
            print(f"Error: Could not find file: {path}")
        except Exception as e:
            print(f"Error processing {path}: {str(e)}")

    print("\nProcessing complete!")
    print(f"Total pages: {len(pages)}")
    print(f"Total lines: {sum(len(page) for page in pages.values())}")


def generate_code_book():
    global pages
    code_book = {}
    reverse_book = {}
    for page, lines in pages.items():
        for num, line in lines.items():
            for pos, char in enumerate(line):
                position = f'{page}-{num}-{pos}'
                code_book.setdefault(char, []).append(position)
                reverse_book[position] = char
    return code_book, reverse_book


def save(file_path, book):
    with open(file_path, 'w') as fp:
        json.dump(book, fp)


def load(file_path, *key_books, reverse=False):
    if os.path.exists(file_path):
        with open(file_path, 'r') as fp:
            return json.load(fp)
    else:
        process_books(*key_books)
        code_book, reverse_book = generate_code_book()
        if reverse:
            save(file_path, reverse_book)
            return reverse_book
        else:
            save(file_path, code_book)
            return code_book


def encode_message(message, code_book):
    encoded = []
    for char in message.lower():
        if char in code_book:
            position = random.choice(code_book[char])
            encoded.append(position)
        else:
            print(f"Warning: Character '{char}' not found in codebook")
    return ' '.join(encoded)


def decode_message(encoded_message, reverse_book):
    decoded = []
    positions = encoded_message.split()
    for pos in positions:
        if pos in reverse_book:
            decoded.append(reverse_book[pos])
        else:
            print(f"Warning: Position '{pos}' not found in codebook")
    return ''.join(decoded)


def main():
    book_paths = []
    print(f"Please enter the paths for {HOW_MANY_BOOK} books:")

    for i in range(HOW_MANY_BOOK):
        path = input(f"Enter path for book {i + 1}: ")
        book_paths.append(path)

    codebook_path = "codebook.json"
    reverse_path = "reverse_codebook.json"

    code_book = load(codebook_path, *book_paths)
    reverse_book = load(reverse_path, *book_paths, reverse=True)

    print("\nCodebook loaded successfully!")
    print(f"Total unique characters: {len(code_book)}")

    while True:
        print("\nCipher Options:")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. View codebook")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            message = input("\nEnter message to encode: ")
            encoded = encode_message(message, code_book)
            print("\nEncoded message:")
            print(encoded)

        elif choice == '2':
            encoded = input("\nEnter encoded message: ")
            decoded = decode_message(encoded, reverse_book)
            print("\nDecoded message:")
            print(decoded)

        elif choice == '3':
            view = input("\nWould you like to view the codebook? (yes/no): ").lower()
            if view == 'yes':
                for char in sorted(code_book.keys()):
                    print(f"\nCharacter: '{char}'")
                    print(f"Occurrences: {len(code_book[char])}")
                    print(f"Sample positions: {' '.join(code_book[char][:5])}")

        elif choice == '4':
            print("\nExiting cipher program.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()