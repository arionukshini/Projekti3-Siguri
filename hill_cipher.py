ALPHABET_SIZE = 26
PADDING_CHAR = "X"


def sanitize_text(text):
    cleaned = ""
    for char in text.upper():
        if char.isalpha():
            cleaned += char
    return cleaned


def chunk_text(text, size):
    while len(text) % size != 0:
        text += PADDING_CHAR

    chunks = []
    for i in range(0, len(text), size):
        chunks.append(text[i:i + size])

    return chunks


def text_to_numbers(block):
    numbers = []
    for char in block:
        numbers.append(ord(char) - ord("A"))
    return numbers


def numbers_to_text(numbers):
    text = ""
    for num in numbers:
        text += chr(num + ord("A"))
    return text


def multiply_matrix_block(matrix, block_numbers):
    result = []

    for row in matrix:
        total = 0
        for i in range(len(row)):
            total += row[i] * block_numbers[i]
        result.append(total % ALPHABET_SIZE)

    return result


def encrypt(plaintext, key_matrix):
    clean_text = sanitize_text(plaintext)
    block_size = len(key_matrix)
    blocks = chunk_text(clean_text, block_size)

    encrypted_text = ""

    for block in blocks:
        block_numbers = text_to_numbers(block)
        encrypted_numbers = multiply_matrix_block(key_matrix, block_numbers)
        encrypted_block = numbers_to_text(encrypted_numbers)
        encrypted_text += encrypted_block

    return encrypted_text
