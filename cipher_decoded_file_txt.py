import cipher_decoded_message

#**************************************************************** Cipher txt file
def cipher_txt(input_file, output_file, e, n):
    
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
        
    ciphertext = cipher_decoded_message.rsa_cipher(content, e, n)

    with open(output_file, 'w', encoding='utf-8') as file:
        for char_code in ciphertext:
            file.write(str(char_code) + ' ')
    print(f"Archivo TXT cifrado se guarda en {output_file}")

def decipher_txt(input_file, output_file, d, n):
    with open(input_file, 'r', encoding='utf-8') as file:
        ciphertext = file.read().split()
        ciphertext = [int(code) for code in ciphertext]

    decoded_message = cipher_decoded_message.rsa_decoded(ciphertext, d, n)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(decoded_message)
    print(f"Archivo TXT descifrado se guarda en {output_file}")