from Crypto.Cipher import AES, DES # type: ignore
from Crypto.Random import get_random_bytes # type: ignore

def pad_message(msg, block_size):
    return msg + (block_size - len(msg) % block_size) * b' '

def aes_encrypt_decrypt():
    key = get_random_bytes(16)
    iv = get_random_bytes(16)  # AES block size is 16 bytes
    message = input("Enter message for AES encryption: ").encode()
    message = pad_message(message, 16)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(message)
    print("AES Encrypted:", encrypted)

    decipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = decipher.decrypt(encrypted).strip()
    print("AES Decrypted:", decrypted.decode())

def des_encrypt_decrypt():
    key = get_random_bytes(8)
    iv = get_random_bytes(8)  # DES block size is 8 bytes
    message = input("Enter message for DES encryption: ").encode()
    message = pad_message(message, 8)

    cipher = DES.new(key, DES.MODE_CBC, iv)
    encrypted = cipher.encrypt(message)
    print("DES Encrypted:", encrypted)

    decipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted = decipher.decrypt(encrypted).strip()
    print("DES Decrypted:", decrypted.decode())

aes_encrypt_decrypt()
des_encrypt_decrypt()
