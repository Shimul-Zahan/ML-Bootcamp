def encrypt_transposition_cipher(text, key):
    """
    Transposition Cipher এনক্রিপশন ফাংশন
    :param text: এনক্রিপ্ট করতে হবে এমন প্লেইনটেক্সট
    :param key: কটি কলাম থাকবে তা নির্ধারণ করে
    :return: এনক্রিপ্ট হওয়া সিফারটেক্সট
    """
    text = text.replace(" ", "")  # স্পেস মুছে ফেলা
    cipher_text = [''] * key
    
    print(cipher_text)

    for col in range(key):
        pointer = col
        while pointer < len(text):
            cipher_text[col] += text[pointer]
            pointer += key
            print(cipher_text)

    return ''.join(cipher_text)

# উদাহরণ ব্যবহার:
plaintext = "HELLO WORLD"
key = 4
cipher_text = encrypt_transposition_cipher(plaintext, key)
print("Encrypted Text:", cipher_text)
