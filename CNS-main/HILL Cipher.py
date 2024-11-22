# Function to encrypt a message using Hill Cipher
def hill_cipher_encrypt(message, key_matrix):
    # Convert message to uppercase and remove spaces
    message = message.upper().replace(" ", "")
    
    # Ensure the message length is a multiple of the key matrix size
    key_size = len(key_matrix)
    while len(message) % key_size != 0:
        message += 'X'  # Padding with 'X'
    
    # Convert message to numerical values (A=0, B=1, ..., Z=25)
    message_vector = [ord(char) - 65 for char in message]
    
    # Encrypt message block by block
    encrypted_message = ""
    for i in range(0, len(message_vector), key_size):
        block = message_vector[i:i+key_size]
        encrypted_block = [
            sum(key_matrix[row][col] * block[col] for col in range(key_size)) % 26
            for row in range(key_size)
        ]
        encrypted_message += ''.join(chr(num + 65) for num in encrypted_block)
    
    return encrypted_message

# Function to find the modular inverse of a number
def modular_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse for {a} under modulo {m}")

# Function to calculate the inverse of a 2x2 or 3x3 key matrix modulo 26
def matrix_mod_inverse(key_matrix, mod=26):
    n = len(key_matrix)
    if n == 2:
        # For 2x2 matrix: [[a, b], [c, d]]
        a, b = key_matrix[0]
        c, d = key_matrix[1]
        det = (a * d - b * c) % mod
        det_inv = modular_inverse(det, mod)
        # Inverse matrix
        inv_matrix = [
            [(d * det_inv) % mod, (-b * det_inv) % mod],
            [(-c * det_inv) % mod, (a * det_inv) % mod]
        ]
    elif n == 3:
        # For 3x3 matrix
        det = (
            key_matrix[0][0] * (key_matrix[1][1] * key_matrix[2][2] - key_matrix[1][2] * key_matrix[2][1]) -
            key_matrix[0][1] * (key_matrix[1][0] * key_matrix[2][2] - key_matrix[1][2] * key_matrix[2][0]) +
            key_matrix[0][2] * (key_matrix[1][0] * key_matrix[2][1] - key_matrix[1][1] * key_matrix[2][0])
        ) % mod
        det_inv = modular_inverse(det, mod)
        # Cofactor matrix
        cofactors = [
            [
                ((key_matrix[1][1] * key_matrix[2][2] - key_matrix[1][2] * key_matrix[2][1]) * det_inv) % mod,
                ((key_matrix[0][2] * key_matrix[2][1] - key_matrix[0][1] * key_matrix[2][2]) * det_inv) % mod,
                ((key_matrix[0][1] * key_matrix[1][2] - key_matrix[0][2] * key_matrix[1][1]) * det_inv) % mod,
            ],
            [
                ((key_matrix[1][2] * key_matrix[2][0] - key_matrix[1][0] * key_matrix[2][2]) * det_inv) % mod,
                ((key_matrix[0][0] * key_matrix[2][2] - key_matrix[0][2] * key_matrix[2][0]) * det_inv) % mod,
                ((key_matrix[0][2] * key_matrix[1][0] - key_matrix[0][0] * key_matrix[1][2]) * det_inv) % mod,
            ],
            [
                ((key_matrix[1][0] * key_matrix[2][1] - key_matrix[1][1] * key_matrix[2][0]) * det_inv) % mod,
                ((key_matrix[0][1] * key_matrix[2][0] - key_matrix[0][0] * key_matrix[2][1]) * det_inv) % mod,
                ((key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]) * det_inv) % mod,
            ],
        ]
        # Transpose of cofactor matrix
        inv_matrix = [[cofactors[j][i] % mod for j in range(n)] for i in range(n)]
    else:
        raise ValueError("Only 2x2 and 3x3 matrices are supported")
    return inv_matrix

# Function to decrypt a message using Hill Cipher
def hill_cipher_decrypt(encrypted_message, key_matrix):
    # Find the inverse key matrix modulo 26
    key_matrix_inv = matrix_mod_inverse(key_matrix, 26)
    
    # Convert encrypted message to numerical values
    encrypted_vector = [ord(char) - 65 for char in encrypted_message]
    
    # Decrypt message block by block
    key_size = len(key_matrix)
    decrypted_message = ""
    for i in range(0, len(encrypted_vector), key_size):
        block = encrypted_vector[i:i+key_size]
        decrypted_block = [
            sum(key_matrix_inv[row][col] * block[col] for col in range(key_size)) % 26
            for row in range(key_size)
        ]
        decrypted_message += ''.join(chr(num + 65) for num in decrypted_block)
    
    return decrypted_message.rstrip('X')  # Remove padding

# Main function
def main():
    # Define the key matrix (must be square and invertible modulo 26)
    key_matrix = [
        [6, 24, 1],
        [13, 16, 10],
        [20, 17, 15]
    ]
    
    # Input message
    message = "HELLO"
    
    # Encrypt the message
    encrypted_message = hill_cipher_encrypt(message, key_matrix)
    print(f"Encrypted Message: {encrypted_message}")
    
    # Decrypt the message
    decrypted_message = hill_cipher_decrypt(encrypted_message, key_matrix)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
