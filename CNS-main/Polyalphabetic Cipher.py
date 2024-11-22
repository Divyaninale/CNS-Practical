def generate_vigenere_table():
    table = []
    for i in range(26):
        row = [(chr((j + i) % 26 + 65)) for j in range(26)]
        table.append(row)
    return table

def polyalphabetic_encrypt(text, key):
    text = text.upper().replace(" ", "")  # Remove spaces and convert to uppercase
    key = key.upper()
    vigenere_table = generate_vigenere_table()
    encrypted_text = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            row = ord(key[key_index]) - 65
            col = ord(char) - 65
            encrypted_text += vigenere_table[row][col]
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_text += char  # Non-alphabet characters remain unchanged
    return encrypted_text

def polyalphabetic_decrypt(cipher_text, key):
    cipher_text = cipher_text.upper().replace(" ", "")  # Remove spaces and convert to uppercase
    key = key.upper()
    vigenere_table = generate_vigenere_table()
    decrypted_text = ""
    key_index = 0

    for char in cipher_text:
        if char.isalpha():
            row = ord(key[key_index]) - 65
            for col in range(26):
                if vigenere_table[row][col] == char:
                    decrypted_text += chr(col + 65)
                    break
            key_index = (key_index + 1) % len(key)
        else:
            decrypted_text += char  # Non-alphabet characters remain unchanged
    return decrypted_text

# Example usage
if __name__ == "__main__":
    text = input("Enter the text to encrypt: ")
    key = input("Enter the key: ")
    
    encrypted = polyalphabetic_encrypt(text, key)
    print(f"Encrypted text: {encrypted}")
    
    decrypted = polyalphabetic_decrypt(encrypted, key)
    print(f"Decrypted text: {decrypted}")
