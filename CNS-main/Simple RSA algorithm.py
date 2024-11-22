# Function to compute the greatest common divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to compute the modular inverse using the Extended Euclidean Algorithm
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Function to generate RSA keys
def generate_rsa_keys():
    # Small prime numbers
    p = 61
    q = 53
    
    # Calculate n = p * q
    n = p * q
    
    # Euler's totient function phi(n) = (p-1) * (q-1)
    phi_n = (p - 1) * (q - 1)
    
    # Choose e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    e = 17  # Commonly used value for e
    
    # Compute d such that d * e ≡ 1 (mod phi(n))
    d = mod_inverse(e, phi_n)
    
    # Public key (e, n) and Private key (d, n)
    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key

# Function to encrypt a message using RSA
def encrypt_message(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Function to decrypt a message using RSA
def decrypt_message(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

# Main function to demonstrate RSA encryption and decryption
def main():
    # Generate RSA keys
    public_key, private_key = generate_rsa_keys()
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")
    
    # Take a message from the user to encrypt
    message = input("Enter a message to encrypt: ")
    
    # Encrypt the message
    encrypted_message = encrypt_message(message, public_key)
    print(f"Encrypted Message: {encrypted_message}")
    
    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message, private_key)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
