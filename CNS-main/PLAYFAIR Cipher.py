def generate_playfair_matrix(key):
    key = key.upper().replace("J", "I")  # Replace 'J' with 'I'
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    used_chars = set()

    # Add the key to the matrix
    for char in key:
        if char not in used_chars and char.isalpha():
            matrix.append(char)
            used_chars.add(char)

    # Fill the matrix with the rest of the alphabet
    for char in alphabet:
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)

    # Reshape into 5x5 grid
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def preprocess_text(text):
    text = text.upper().replace("J", "I")  # Replace 'J' with 'I'
    processed_text = ""
    i = 0

    # Process text into pairs
    while i < len(text):
        char1 = text[i]
        if i + 1 < len(text):
            char2 = text[i + 1]
        else:
            char2 = "X"  # Pad with 'X' if last character is single

        if char1 == char2:
            processed_text += char1 + "X"
            i += 1
        else:
            processed_text += char1 + char2
            i += 2

    if len(processed_text) % 2 != 0:
        processed_text += "X"  # Ensure pairs by padding
    return processed_text

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def playfair_encrypt(text, matrix):
    encrypted_text = ""
    text = preprocess_text(text)

    for i in range(0, len(text), 2):
        char1, char2 = text[i], text[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        # Same row
        if row1 == row2:
            encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        # Same column
        elif col1 == col2:
            encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        # Rectangle
        else:
            encrypted_text += matrix[row1][col2] + matrix[row2][col1]

    return encrypted_text

def playfair_decrypt(text, matrix):
    decrypted_text = ""
    for i in range(0, len(text), 2):
        char1, char2 = text[i], text[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        # Same row
        if row1 == row2:
            decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        # Same column
        elif col1 == col2:
            decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        # Rectangle
        else:
            decrypted_text += matrix[row1][col2] + matrix[row2][col1]

    return decrypted_text

# Example usage
if __name__ == "__main__":
    key = "ldrp"
    matrix = generate_playfair_matrix(key)
    print("Playfair Matrix:")
    for row in matrix:
        print(" ".join(row))

    plaintext = input("Enter the plaintext: ")
    encrypted_text = playfair_encrypt(plaintext, matrix)
    print(f"Encrypted text: {encrypted_text}")

    decrypted_text = playfair_decrypt(encrypted_text, matrix)
    print(f"Decrypted text: {decrypted_text}")
