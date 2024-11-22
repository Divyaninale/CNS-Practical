# Function to compute (base^exponent) % modulus using Python's built-in power function
def power_mod(base, exponent, modulus):
    return pow(base, exponent, modulus)

# Diffie-Hellman key exchange function
def diffie_hellman_key_exchange(p, g, a, b):
    # Alice computes A = g^a mod p
    A = power_mod(g, a, p)
    print(f"Alice's public key: {A}")

    # Bob computes B = g^b mod p
    B = power_mod(g, b, p)
    print(f"Bob's public key: {B}")

    # Alice computes the shared secret: s = B^a mod p
    shared_secret_alice = power_mod(B, a, p)
    print(f"Alice computes shared secret: {shared_secret_alice}")

    # Bob computes the shared secret: s = A^b mod p
    shared_secret_bob = power_mod(A, b, p)
    print(f"Bob computes shared secret: {shared_secret_bob}")

    # The shared secrets should be the same
    if shared_secret_alice == shared_secret_bob:
        print(f"Shared secret key successfully established: {shared_secret_alice}")
    else:
        print("Error: Shared secrets do not match")

# Main function to demonstrate the Diffie-Hellman key exchange
def main():
    # Taking input from the user for public parameters and private keys
    print("Enter the public parameters:")
    p = int(input("Enter prime number p: "))  # Prime number
    g = int(input("Enter base (primitive root) g: "))  # Base (primitive root)

    # Private keys of Alice and Bob
    a = int(input("Enter Alice's private key: "))  # Alice's private key
    b = int(input("Enter Bob's private key: "))  # Bob's private key

    print("\nDiffie-Hellman Key Exchange:")
    diffie_hellman_key_exchange(p, g, a, b)

if __name__ == "__main__":
    main()
