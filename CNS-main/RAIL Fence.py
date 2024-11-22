# Function to encrypt a message using Rail Fence Cipher
def rail_fence_encrypt(message, key):
    # Remove spaces and convert to uppercase
    message = message.replace(" ", "").upper()

    # Create a 2D array to represent the rail fence
    rail = [['' for _ in range(len(message))] for _ in range(key)]
    
    # Determine the direction (down or up)
    direction_down = False
    row = 0

    # Place the characters in the rail pattern
    for i in range(len(message)):
        rail[row][i] = message[i]

        # Change direction if at the top or bottom rail
        if row == 0 or row == key - 1:
            direction_down = not direction_down

        # Move to the next row
        row += 1 if direction_down else -1

    # Collect the characters from the rail to form the encrypted message
    encrypted_message = ''
    for r in rail:
        encrypted_message += ''.join([char for char in r if char])

    return encrypted_message


# Function to decrypt a message using Rail Fence Cipher
def rail_fence_decrypt(encrypted_message, key):
    # Create a 2D array to represent the rail fence
    rail = [['' for _ in range(len(encrypted_message))] for _ in range(key)]
    
    # Mark the positions to be filled
    direction_down = None
    row, col = 0, 0

    for i in range(len(encrypted_message)):
        # Mark the current position
        rail[row][col] = '*'

        # Change direction if at the top or bottom rail
        if row == 0:
            direction_down = True
        elif row == key - 1:
            direction_down = False

        # Move to the next position
        row += 1 if direction_down else -1
        col += 1

    # Fill the rail with the encrypted message
    index = 0
    for i in range(key):
        for j in range(len(encrypted_message)):
            if rail[i][j] == '*' and index < len(encrypted_message):
                rail[i][j] = encrypted_message[index]
                index += 1

    # Read the message following the zigzag pattern
    decrypted_message = ''
    row, col = 0, 0
    for i in range(len(encrypted_message)):
        decrypted_message += rail[row][col]

        # Change direction if at the top or bottom rail
        if row == 0:
            direction_down = True
        elif row == key - 1:
            direction_down = False

        # Move to the next position
        row += 1 if direction_down else -1
        col += 1

    return decrypted_message


# Main function
def main():
    # Input message and key from the user
    message = input("Enter the message to be encrypted: ")
    key = int(input("Enter the number of rails (key): "))

    # Encrypt the message
    encrypted_message = rail_fence_encrypt(message, key)
    print(f"Encrypted Message: {encrypted_message}")

    # Decrypt the message
    decrypted_message = rail_fence_decrypt(encrypted_message, key)
    print(f"Decrypted Message: {decrypted_message}")


if __name__ == "__main__":
    main()
