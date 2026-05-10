from math import gcd

from hill_cipher import (
    sanitize_text,
    chunk_text,
    text_to_numbers,
    numbers_to_text,
    multiply_matrix_block
)
ALPHABET_SIZE = 26

def mod_inverse(a, m):
    a = a % m

    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def determinant_2x2(matrix):
    return (
        matrix[0][0] * matrix[1][1]
        - matrix[0][1] * matrix[1][0]
    )

def determinant_3x3(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]

    d = matrix[1][0]
    e = matrix[1][1]
    f = matrix[1][2]

    g = matrix[2][0]
    h = matrix[2][1]
    i = matrix[2][2]

    determinant = (
        a * (e * i - f * h)
        - b * (d * i - f * g)
        + c * (d * h - e * g)
    )
    return determinant

def get_minor(matrix, row, col):
    minor = []

    for i in range(len(matrix)):
        if i == row:
            continue

        current_row = []

        for j in range(len(matrix)):
            if j == col:
                continue

            current_row.append(matrix[i][j])

        minor.append(current_row)
    return minor

def determinant_4x4(matrix):
    determinant = 0

    for col in range(4):
        sign = (-1) ** col

        minor = get_minor(matrix, 0, col)

        determinant += (
            sign
            * matrix[0][col]
            * determinant_3x3(minor)
        )

    return determinant

def get_determinant(matrix):
    size = len(matrix)

    if size == 2:
        return determinant_2x2(matrix)
    elif size == 3:
        return determinant_3x3(matrix)
    elif size == 4:
        return determinant_4x4(matrix)
    else:
        raise ValueError("Matrix size must be between 2 and 4")
    
def is_invertible(matrix):
    determinant = get_determinant(matrix)

    determinant = determinant % ALPHABET_SIZE
    return gcd(determinant, ALPHABET_SIZE) == 1

def transpose(matrix):
    size = len(matrix)

    transposed = []

    for i in range(size):
        row = []

        for j in range(size):
            row.append(matrix[j][i])

        transposed.append(row)
    return transposed

def cofactor_matrix(matrix):
    size = len(matrix)

    cofactors = []

    for row in range(size):
        cofactor_row = []

        for col in range(size):
            minor = get_minor(matrix, row, col)

            if size == 2:
                minor_det = minor[0][0]

            elif size == 3:
                minor_det = determinant_2x2(minor)

            elif size == 4:
                minor_det = determinant_3x3(minor)

            sign = (-1) ** (row + col)

            cofactor_row.append(sign * minor_det)

        cofactors.append(cofactor_row)
    return cofactors

def inverse_matrix(matrix):
    determinant = get_determinant(matrix)

    determinant = determinant % ALPHABET_SIZE

    determinant_inverse = mod_inverse(
        determinant,
        ALPHABET_SIZE
    )

    if determinant_inverse is None:
        raise ValueError("Matrix is not invertible")

    cofactors = cofactor_matrix(matrix)

    adjugate = transpose(cofactors)

    inverse = []

    for row in adjugate:
        inverse_row = []

        for value in row:
            inverse_value = (
                value * determinant_inverse
            ) % ALPHABET_SIZE

            inverse_row.append(inverse_value)

        inverse.append(inverse_row)
    return inverse

def decrypt(ciphertext, key_matrix):
    if not is_invertible(key_matrix):
        raise ValueError("Key matrix is not invertible")

    inverse_key = inverse_matrix(key_matrix)

    clean_text = sanitize_text(ciphertext)

    block_size = len(key_matrix)

    blocks = chunk_text(clean_text, block_size)

    decrypted_text = ""

    for block in blocks:
        block_numbers = text_to_numbers(block)

        decrypted_numbers = multiply_matrix_block(
            inverse_key,
            block_numbers
        )

        decrypted_block = numbers_to_text(
            decrypted_numbers
        )

        decrypted_text += decrypted_block
    return decrypted_text