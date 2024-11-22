def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            shift_base = 65 if char.isupper() else 97  # Uppercase or lowercase ASCII base
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

# Example usage
if __name__ == "__main__":
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))
    
    encrypted = caesar_cipher_encrypt(text, shift)
    print(f"Encrypted text: {encrypted}")
    
    decrypted = caesar_cipher_decrypt(encrypted, shift)
    print(f"Decrypted text: {decrypted}")
