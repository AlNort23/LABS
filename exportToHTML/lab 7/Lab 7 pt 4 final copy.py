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
        key = input("Enter encryption key: ")
        plaintext = input("Enter message to encrypt: ")
        encrypted = encrypt_vigenere(key, plaintext, alphabet)
        print(f"Encrypted text: {encrypted}")

    elif choice == '2':
        key = input("Enter decryption key: ")
        ciphertext = input("Enter text to decrypt: ")
        decrypted = decrypt_vigenere(key, ciphertext, alphabet)
        print(f"Decrypted text: {decrypted}")

    elif choice == '3':
        # Changed variable name to search_key for clarity
        search_key = input("Enter key to dump (or 'all' for all messages): ")
        # Remove spaces and convert to uppercase using string methods (Ch 8.5)
        search_key = ''.join(char for char in search_key if char != ' ').upper()
        if search_key == 'ALL':  # Now comparing uppercase to uppercase
            for stored_key, message in encrypted_messages:
                print(f"Key: {stored_key}, Message: {message}")
        else:
            matches = [msg for k, msg in encrypted_messages if k == search_key]
            if matches:
                for message in matches:
                    print(f"Message: {message}")
            else:
                print("No messages found with that key.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")