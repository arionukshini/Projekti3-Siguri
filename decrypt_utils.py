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