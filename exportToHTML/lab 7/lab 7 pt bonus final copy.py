import string


def letter_to_index(letter, alphabet):
    return alphabet.index(letter.upper())


def index_to_letter(index, alphabet):
    return alphabet[index]


def vigenere_index(key_letter, plaintext_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    plaintext_index = letter_to_index(plaintext_letter, alphabet)
    cipher_index = (plaintext_index + key_index) % len(alphabet)
    return index_to_letter(cipher_index, alphabet)


def encrypt_vigenere(key, plaintext, alphabet):
    key = ''.join(char.upper() for char in key if char.isalpha())
    key_length = len(key)
    cipher_text = []

    for i, char in enumerate(plaintext):
        if char.upper() in alphabet:
            key_char = key[i % key_length]
            encrypted_char = vigenere_index(key_char, char, alphabet)
            cipher_text.append(encrypted_char)
        else:
            cipher_text.append(char)

    encrypted = ''.join(cipher_text)
    encrypted_messages.append((key, encrypted))
    return encrypted


def undo_vigenere_index(key_letter, cipher_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    cipher_index = letter_to_index(cipher_letter, alphabet)
    plain_index = (cipher_index - key_index) % len(alphabet)
    return index_to_letter(plain_index, alphabet)


def decrypt_vigenere(key, cipher_text, alphabet):
    key = ''.join(char.upper() for char in key if char.isalpha())
    key_length = len(key)
    plain_text = []

    for i, char in enumerate(cipher_text):
        if char.upper() in alphabet:
            key_char = key[i % key_length]
            decrypted_char = undo_vigenere_index(key_char, char, alphabet)
            plain_text.append(decrypted_char)
        else:
            plain_text.append(char)

    return ''.join(plain_text)


encrypted_messages = []
alphabet = string.ascii_uppercase

while True:
    print("\nVigenère Cipher Menu:")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Dump Encrypted Text")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        num_keys = int(input("How many encryption keys? "))
        keys = []
        for i in range(num_keys):
            key = input(f"Enter encryption key (letters and words only, no symbols)#{i + 1}: ")
            keys.append(key)

        key_index = 0
        while True:
            plaintext = input("Enter message to encrypt (or 'done' to return to menu): ")
            if plaintext.lower() == 'done':
                break

            current_key = keys[key_index]
            encrypted = encrypt_vigenere(current_key, plaintext, alphabet)
            print(f"Using key '{current_key}': {encrypted}")

            key_index = (key_index + 1) % num_keys

    elif choice == '2':
        key = input("Enter decryption key: ")
        ciphertext = input("Enter text to decrypt: ")
        decrypted = decrypt_vigenere(key, ciphertext, alphabet)
        print(f"Decrypted text: {decrypted}")

    elif choice == '3':
        print("\nDump options:")
        print("1. Show messages with keys")
        print("2. Show only encrypted messages")
        dump_choice = input("Enter choice (1-2): ")

        search_key = input("Enter the encryption key to dump specific encrypted messages (or 'all' for all messages): ")
        search_key = ''.join(char for char in search_key if char != ' ').upper()

        if search_key == 'ALL':
            if dump_choice == '1':
                for stored_key, message in encrypted_messages:
                    print(f"Key: {stored_key}, Message: {message}")
            elif dump_choice == '2':
                for _, message in encrypted_messages:
                    print(f"{message}")
            else:
                print("Invalid choice.")
        else:
            matches = [(k, msg) for k, msg in encrypted_messages if k == search_key]
            if matches:
                if dump_choice == '1':
                    for stored_key, message in matches:
                        print(f"Key: {stored_key}, Message: {message}")
                elif dump_choice == '2':
                    for _, message in matches:
                        print(f"Message: {message}")
                else:
                    print("Invalid choice.")
            else:
                print("No messages found with that key.")

    elif choice == '4':
        print("All Done!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")