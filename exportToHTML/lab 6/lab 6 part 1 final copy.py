def vigenere_sq():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    print(f"{'':2}", end='')
    for letter in alphabet:
        print(f"{letter:2}", end='')
    print()

    for i, row_letter in enumerate(alphabet):
        print(f"{row_letter:2}", end='')
        for j in range(26):
            cell_letter = alphabet[(i + j) % 26]
            print(f"{cell_letter:2}", end='')
        print()


vigenere_sq()