import random

def generate_key(length):
    return [random.randint(0, 255) for _ in range(length)]

def encrypt(plain_text, key):
    # Plaintext -> binary or byte
    plain_bytes = plain_text.encode()
    # transform to XOR
    cipher_bytes = [plain_bytes[i] ^ key[i] for i in range(len(plain_bytes))]
    return cipher_bytes

def decrypt(cipher_bytes, key):
    
    # transform to XOR
    
    plain_bytes = [cipher_bytes[i] ^ key[i] for i in range(len(cipher_bytes))]
    return bytes(plain_bytes).decode()

# Example usage
message = "HELLO"
key = generate_key(len(message))
cipher = encrypt(message, key)
decrypted_message = decrypt(cipher, key)

print("Original Message:", message)
print("Encryption Key:", key)
print("Cipher Text:", cipher)
print("Decrypted Message:", decrypted_message)
