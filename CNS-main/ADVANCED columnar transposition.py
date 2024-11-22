# Function to encrypt a message using Advanced Columnar Transposition Cipher
def advanced_columnar_transposition_encrypt(message, key):
    # Remove spaces and convert to uppercase
    message = message.replace(" ", "").upper()

    # Calculate the number of columns and rows
    num_columns = len(key)
    num_rows = len(message) // num_columns
    if len(message) % num_columns != 0:
        num_rows += 1

    # Add extra filler characters if necessary to complete the grid
    filler = 'X'
    message = message.ljust(num_rows * num_columns, filler)

    # Create a 2D grid (matrix) to arrange the message characters in columns
    grid = []
    for i in range(num_rows):
        grid.append([message[i * num_columns + j] for j in range(num_columns)])

    # Create a list of column numbers based on the key's alphabetical order
    sorted_key = sorted(enumerate(key), key=lambda x: x[1])
    column_order = [x[0] for x in sorted_key]

    # Read the grid column by column according to the sorted key
    encrypted_message = ''
    for col in column_order:
        for row in range(num_rows):
            encrypted_message += grid[row][col]

    return encrypted_message


# Function to decrypt a message using Advanced Columnar Transposition Cipher
def advanced_columnar_transposition_decrypt(encrypted_message, key):
    # Calculate the number of columns and rows
    num_columns = len(key)
    num_rows = len(encrypted_message) // num_columns

    # Create a grid to store the message
    grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]
    
    # Create a list of column numbers based on the key's alphabetical order
    sorted_key = sorted(enumerate(key), key=lambda x: x[1])
    column_order = [x[0] for x in sorted_key]

    # Fill the grid with the encrypted message in column order
    index = 0
    for col in column_order:
        for row in range(num_rows):
            grid[row][col] = encrypted_message[index]
            index += 1

    # Read the grid row by row to retrieve the original message
    decrypted_message = ''.join(''.join(row) for row in grid)

    # Remove any filler characters (X) from the decrypted message
    return decrypted_message.rstrip('X')


# Main function
def main():
    # Input message and key from the user
    message = input("Enter the message to be encrypted: ")
    key = input("Enter the key (alphabetic or numeric): ")

    # Encrypt the message
    encrypted_message = advanced_columnar_transposition_encrypt(message, key)
    print(f"Encrypted Message: {encrypted_message}")

    # Decrypt the message
    decrypted_message = advanced_columnar_transposition_decrypt(encrypted_message, key)
    print(f"Decrypted Message: {decrypted_message}")


if __name__ == "__main__":
    main()
