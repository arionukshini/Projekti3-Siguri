from hill_cipher import encrypt
from decrypt_utils import determinant_4x4

key_matrix = [
    [3, 3],
    [2, 5]
]

while True:
    print("\n--- HILL CIPHER MENU ---")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Zgjedh opsionin: ")

    if choice == "1":
        text = input("Shkruaj tekstin: ")
        print("Encrypted:", encrypt(text, key_matrix))

    elif choice == "2":
        text = input("Shkruaj ciphertext: ")
        print("Decrypted:", decrypt(text, key_matrix))

    elif choice == "3":
        break

    else:
        print("Opsion i pavlefshem!")