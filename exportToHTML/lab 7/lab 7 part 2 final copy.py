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

    return ''.join(cipher_text)

alphabet = string.ascii_uppercase
key = 'FULL SEND'
plaintext = 'TWINKLE TWINKLE LITTLE STAR'

encrypted_text = encrypt_vigenere(key, plaintext, alphabet)
print(f"Plaintext: {plaintext}")
print(f"Key: {key}")
print(f"Encrypted: {encrypted_text}")