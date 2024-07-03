def rsa_cipher(message, e, n):
        ciphertext = []
        for char in message:
            # Characters ASCII
            char_code = ord(char)
            encrypted_char = pow(char_code, e, n)
            ciphertext.append(encrypted_char)

        return ciphertext

def rsa_decoded(ciphertext, d, n):
    decoded_text = []
    for encrypted_char in ciphertext:
        decipher_char_code = pow(encrypted_char, d, n)
        decipher_char = chr(decipher_char_code)
        decoded_text.append(decipher_char)            
    return "".join(decoded_text)
