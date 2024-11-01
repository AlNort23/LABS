def vigenere_index(plaintext_letter, keyword_letter):
    plaintext_index = ord(plaintext_letter.upper()) - ord('A')
    keyword_index = ord(keyword_letter.upper()) - ord('A')
    cipher_index = (plaintext_index + keyword_index) % 26
    cipher_letter = chr(cipher_index + ord('A'))
    return cipher_index, cipher_letter


def vigenere_decrypt_index(ciphertext_letter, keyword_letter):
    ciphertext_index = ord(ciphertext_letter.upper()) - ord('A')
    keyword_index = ord(keyword_letter.upper()) - ord('A')
    plaintext_index = (ciphertext_index - keyword_index) % 26
    plaintext_letter = chr(plaintext_index + ord('A'))
    return plaintext_index, plaintext_letter


def encrypt_vigenere(plaintext, keyword):
    ciphertext = ""
    keyword_length = len(keyword)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            _, letter = vigenere_index(char, keyword[i % keyword_length])
            ciphertext += letter
        else:
            ciphertext += char
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    plaintext = ""
    keyword_length = len(keyword)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            _, letter = vigenere_decrypt_index(char, keyword[i % keyword_length])
            plaintext += letter
        else:
            plaintext += char
    return plaintext


def process_text():
    mode = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()
    text = input("Enter the text to process: ")
    key = input("Enter the key: ")

    if mode == 'e':
        result = encrypt_vigenere(text, key)
        print(f"Encrypted text: {result}")
    elif mode == 'd':
        result = decrypt_vigenere(text, key)
        print(f"Decrypted text: {result}")
    else:
        print("Invalid mode. Please enter 'e' or 'd'.")


process_text()