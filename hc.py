import numpy as np

def hill_cipher_encrypt(plaintext, key_matrix):
    plaintext = plaintext.upper().replace(" ", "")
    plaintext_numbers = [ord(char) - ord('A') for char in plaintext]
    padding_length = len(key_matrix) - (len(plaintext_numbers) % len(key_matrix))
    if padding_length != len(key_matrix):
        plaintext_numbers += [0] * padding_length
    plaintext_matrix = np.array(plaintext_numbers).reshape(-1, len(key_matrix))
    ciphertext_matrix = np.dot(plaintext_matrix, key_matrix) % 26
    ciphertext = ''.join([chr(int(num % 26) + ord('A')) for num in ciphertext_matrix.flatten()])
    return ciphertext

def hill_cipher_decrypt(ciphertext, key_matrix):
    determinant = int(np.round(np.linalg.det(key_matrix)))
    determinant_inverse = pow(determinant, -1, 26)
    key_matrix_inverse = np.round(determinant_inverse * np.linalg.inv(key_matrix) * determinant) % 26
    key_matrix_inverse = key_matrix_inverse.astype(int)
    ciphertext_numbers = [ord(char) - ord('A') for char in ciphertext]
    ciphertext_matrix = np.array(ciphertext_numbers).reshape(-1, len(key_matrix))
    plaintext_matrix = np.dot(ciphertext_matrix, key_matrix_inverse) % 26
    plaintext = ''.join([chr(int(num % 26) + ord('A')) for num in plaintext_matrix.flatten()])
    return plaintext

if __name__ == "__main__":
    key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
    plaintext = input("Give a text with three characters: ")
    ciphertext = hill_cipher_encrypt(plaintext, key_matrix)
    print(f"encrypted text: {ciphertext}")
    decrypted_text = hill_cipher_decrypt(ciphertext, key_matrix)
    print(f"decrypted text: {decrypted_text}")