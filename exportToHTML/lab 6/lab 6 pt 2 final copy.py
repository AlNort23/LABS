def letter_to_index(letter, alphabet):
    return alphabet.index(letter.upper())

def index_to_letter(index, alphabet):
    return alphabet[index]

def vigenere_index(key_letter, plaintext_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    plaintext_index = letter_to_index(plaintext_letter, alphabet)
    cipher_index = (plaintext_index + key_index) % len(alphabet)
    return index_to_letter(cipher_index, alphabet)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 'FULL SEND'

print(f"Index of 'V': {letter_to_index('V', alphabet)}")
print(f"Letter at index 23: {index_to_letter(23, alphabet)}")
print(f"Encrypting 'X' with key 'F': {vigenere_index('F', 'X', alphabet)}")