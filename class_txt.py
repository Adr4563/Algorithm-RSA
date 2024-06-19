from Class_RSA import RSA

class Txt(RSA):
    def init(self, maximo, public_key, private_key):
        super().init(maximo)
        self.public_key = public_key
        self.private_key = private_key

    def cipher_txt(self, input_file, output_file):
        with open(input_file, 'r', encoding='utf-8') as file:
            original_content = file.read()
            

        ciphertext = self.encrypt(original_content)

        with open(output_file, 'w', encoding='utf-8') as file:
            for char_code in ciphertext:
                file.write(str(char_code) + '\n')

    def decripher_txt(self, input_file, output_file):
        with open(input_file, 'r', encoding='utf-8') as file:
            ciphertext = []
            for line in file:
                ciphertext.append(int(line.strip()))

        decrypted_message = self.decrypt(ciphertext)

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(decrypted_message)
            
    def print_rsa_keys(self):
        print("Public key (e, n):", self.public_key[0])
        print("Private key (d, n):", self.private_key[0])