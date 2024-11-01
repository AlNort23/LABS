import string


def vigenere_sq():
    alphabet = string.ascii_uppercase

    print(' ', ' '.join(alphabet))

    square = [alphabet[i:] + alphabet[:i] for i in range(26)]
    for letter, row in zip(alphabet, square):
        print(letter, ' '.join(row))


vigenere_sq()