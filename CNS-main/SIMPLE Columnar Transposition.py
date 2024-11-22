# Function to encrypt a message using Columnar Transposition Cipher
def columnar_transposition_encrypt(message, key):
    # Remove spaces and convert to uppercase
    message = message.replace(" ", "").upper()

    # Calculate number of columns and rows
    num_columns = len(key)
    num_rows = len(message) // num_columns
    if len(message) % num_columns != 0:
        num_rows += 1
    
    # Add extra filler characters if necessary to make the grid complete
    filler = 'X'
    message = message.ljust(num_rows * num_columns, filler)
    
    # Create a 2D grid (matrix) to arrange the message characters in columns
    grid = []
    for i in range(num_rows):
        grid.append([message[i * num_columns + j] for j in range(num_columns)])

    # Create a list of characters sorted by key's column order
    encrypted_message = ''
    for i in sorted(range(len(key)), key=lambda x: key[x]):
        for j in range(num_rows):
            encrypted_message += grid[j][i]

    return encrypted_message


# Function to decrypt a message using Columnar Transposition Cipher
def columnar_transposition_decrypt(encrypted_message, key):
    # Calculate number of columns and rows
    num_columns = len(key)
    num_rows = len(encrypted_message) // num_columns

    # Create a grid to store the message
    grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]
    
    # Fill the grid with characters from the encrypted message
    index = 0
    for i in sorted(range(len(key)), key=lambda x: key[x]):
        for j in range(num_rows):
            grid[j][i] = encrypted_message[index]
            index += 1
    
    # Read the message row by row
    decrypted_message = ''.join(''.join(row) for row in grid)
    
    # Remove any filler characters (X) from the message
    return decrypted_message.rstrip('X')


# Main function
def main():
    # Input message and key from the user
    message = input("Enter the message to be encrypted: ")
    key = input("Enter the key (numeric or alphabetic order): ")

    # Encrypt the message
    encrypted_message = columnar_transposition_encrypt(message, key)
    print(f"Encrypted Message: {encrypted_message}")

    # Decrypt the message
    decrypted_message = columnar_transposition_decrypt(encrypted_message, key)
    print(f"Decrypted Message: {decrypted_message}")


if __name__ == "__main__":
    main()
