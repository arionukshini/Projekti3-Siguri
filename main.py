from hill_cipher import encrypt
from decrypt_utils import decrypt, is_invertible

def choose_matrix():
    print("\nZgjedh rangun e matrices:")
    print("1. Matrix 2x2")
    print("2. Matrix 3x3")
    print("3. Matrix 4x4")

    choice = input("Zgjedh: ")

    if choice == "1":
        return [
            [3, 3],
            [2, 5]
        ]

    elif choice == "2":
        return [
            [6, 24, 1],
            [13, 16, 10],
            [20, 17, 15]
        ]

    elif choice == "3":
        return [
            [1, 0, 2, 1],
            [3, 1, 0, 2],
            [2, 1, 1, 0],
            [1, 2, 3, 1]
        ]

    else:
        print("Opsion i pavlefshem!")
        return None


while True:
    print("\n--- HILL CIPHER MENU ---")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    option = input("Zgjedh opsionin: ")

    if option == "1":

        key_matrix = choose_matrix()

        if key_matrix is None:
            continue

        if not is_invertible(key_matrix):
            print("Matrixa nuk eshte e invertueshme!")
            continue

        text = input("Shkruaj plaintext: ")

        encrypted_text = encrypt(text, key_matrix)

        print("Encrypted:", encrypted_text)

    elif option == "2":

        key_matrix = choose_matrix()

        if key_matrix is None:
            continue

        if not is_invertible(key_matrix):
            print("Matrixa nuk eshte e invertueshme!")
            continue

        text = input("Shkruaj ciphertext: ")

        decrypted_text = decrypt(text, key_matrix)

        print("Decrypted:", decrypted_text)

    elif option == "3":
        print("Programi u mbyll.")
        break
