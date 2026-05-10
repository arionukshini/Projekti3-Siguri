from py_compile import main

from hill_cipher import encrypt
from decrypt_utils import decrypt, is_invertible

def choose_matrix():
    print("\n KONFIGURIMI I MATRICËS ")
    print("Shtyp 0 per matrice AUTOMATIKE (për fillestare)")
    print("Shtyp 2, 3, ose 4 per ta shkruar MANUALISHT")
    
    choice = input("Zgjedhja juaj: ")

    if choice == "0":
        print("\nÇfarë rangu deshiron per matricen automatike?")
        rang = input("Zgjedh (2, 3, ose 4): ")
        if rang == "2":
            return [[3, 3], [2, 5]]
        elif rang == "3":
            return [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
        elif rang == "4":
            return [[1, 0, 2, 1], [3, 1, 0, 2], [2, 1, 1, 0], [1, 2, 3, 1]]
        else:
            print("Gabim: Rang i panjohur. Po kthehem ne menu.")
            return None

    
    try:
        n = int(choice)
        if n not in [2, 3, 4]:
            print("Gabim: Rangu duhet të jetë 2, 3, ose 4.")
            return None

        matrix = []
        print(f"Shënoni {n*n} elementet rresht për rresht:")
        for i in range(n):
            while True:
                row_input = input(f"Rreshti {i+1} (sheno {n} numra me hapesire): ")
                row = [int(x) for x in row_input.split()]
                if len(row) == n:
                    matrix.append(row)
                    break
                else:
                    print(f"Gabim: Duhet t'i shënoni saktesisht {n} numra.")
        return matrix
    except ValueError:
        print("Gabim: Ju lutem shenoni numra te plote.")
        return None

def main():
    while True:
        print("\n HILL CIPHER MENU ")
        print("1. Encrypt ")
        print("2. Decrypt ")
        print("3. Exit ")

        option = input("Zgjedh opsionin: ")

        if option in ["1", "2"]:
            key_matrix = choose_matrix()
            
            if key_matrix is None:
                continue

            if not is_invertible(key_matrix):
                print("\n GABIM: Matrica nuk eshte e invertueshme ne Modulo 26.")
                print("Provo opsionin '0' për nje matrice qe funksionon.")
                continue

            if option == "1":
                text = input("Shkruaj plaintextin: ")
                result = encrypt(text, key_matrix)
                print("\n Encrypted:", result)
            elif option == "2":
                text = input("Shkruaj ciphertextin: ")
                result = decrypt(text, key_matrix)
                print("\n Decrypted:", result)

        elif option == "3":
            print("Programi u mbyll. Tung")
            break
        else:
            print("Opsion i pavlefshëm. Provo perseri.")

if __name__ == "__main__":
    main()