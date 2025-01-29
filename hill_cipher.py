import numpy as np

# Convert letters to numbers (A=0, B=1, ..., Z=25)
def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text]

# Convert numbers to letters
def numbers_to_text(numbers):
    return ''.join(chr(num + ord('A')) for num in numbers)

# Encryption function
def encrypt(plain_text, key_matrix):
    n = len(key_matrix)
    
    # Ensure plaintext length is a multiple of n by padding with 'X'
    while len(plain_text) % n != 0:
        plain_text += 'X'
    
    # Convert plaintext to numbers
    text_vector = text_to_numbers(plain_text)
    
    # Split into blocks of size n
    text_blocks = [text_vector[i:i + n] for i in range(0, len(text_vector), n)]
    
    encrypted_text = []
    
    for block in text_blocks:
        result = np.dot(key_matrix, block) % 26  # Matrix multiplication mod 26
        encrypted_text.extend(result)
    
    return numbers_to_text(encrypted_text)

# Find modular inverse of matrix mod 26
def mod_inverse_matrix(matrix, mod=26):
    determinant = int(round(np.linalg.det(matrix)))  # Determinant of matrix
    determinant_inv = pow(determinant, -1, mod)  # Modular inverse of determinant
    
    matrix_mod_inv = (determinant_inv * np.round(determinant * np.linalg.inv(matrix)).astype(int)) % mod
    return matrix_mod_inv

# Decryption function
def decrypt(cipher_text, key_matrix):
    n = len(key_matrix)
    cipher_vector = text_to_numbers(cipher_text)
    
    # Split into blocks
    cipher_blocks = [cipher_vector[i:i + n] for i in range(0, len(cipher_vector), n)]
    
    # Compute inverse key matrix
    inverse_key_matrix = mod_inverse_matrix(key_matrix)
    
    decrypted_text = []
    
    for block in cipher_blocks:
        result = np.dot(inverse_key_matrix, block) % 26
        decrypted_text.extend(result)
    
    return numbers_to_text(decrypted_text)

# Example usage
key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])  # 3x3 Key Matrix
plaintext = "ACT"

cipher_text = encrypt(plaintext, key_matrix)
decrypted_text = decrypt(cipher_text, key_matrix)

print(f"Plaintext: {plaintext}")
print(f"Encrypted: {cipher_text}")
print(f"Decrypted: {decrypted_text}")
