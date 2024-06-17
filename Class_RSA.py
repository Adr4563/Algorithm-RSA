import random
import math

class RSA:
    def __init__(self, maximo):
        self.maximo = maximo
        self.p, self.q = self.generate_different_primes()
        self.n = self.p * self.q
        self.phi_n = (self.p - 1) * (self.q - 1)
        # Public Key
        self.e = self.generate_public_key()
        # Private Key
        self.d = self.mod_inverse(self.e, self.phi_n)

    def is_prime(self, num):
        if num < 2 or num % 2 == 0:
            return False
        if num == 2:
            return True
        for d in range(3, int(math.sqrt(num)) + 1, 2):
            if num % d == 0:
                return False
        return True

    def generate_prime(self):
        while True:
            num = random.randint(1, self.maximo)
            if self.is_prime(num):
                return num

    def generate_different_primes(self):
        p, q = self.generate_prime(), self.generate_prime()
        while p == q:
            q = self.generate_prime()
        return p, q

    def mod_inverse(self, e, phi_n):
        for d in range(3, phi_n):
            if (d * e) % phi_n == 1:
                return d
        raise ValueError("mod_inverse doesn't exist")

    def generate_public_key(self):
        e = random.randint(3, self.phi_n - 1)
        while math.gcd(e, self.phi_n) != 1:
            e = random.randint(3, self.phi_n - 1)
        return e

    # Message
    def rsa_encrypt(self, message):
        ciphertext = []
        for char in message:
            # Characters ASCII
            char_code = ord(char)
            encrypted_char = pow(char_code, self.e, self.n)
            ciphertext.append(encrypted_char)

        return ciphertext

    def rsa_decrypt(self, ciphertext):
        decrypted_message = []
        for encrypted_char in ciphertext:
            decrypted_char_code = pow(encrypted_char, self.d, self.n)
            decrypted_char = chr(decrypted_char_code)
            decrypted_message.append(decrypted_char)
            
        return "".join(decrypted_message)

    # Methods
    def encrypt(self, message):
        ciphertext = self.rsa_encrypt(message)
        return ciphertext

    def decrypt(self, ciphertext):
        decrypted_message = self.rsa_decrypt(ciphertext)
        return decrypted_message
    
    def get_public_key(self):
        return self.e, self.n

    def get_private_key(self):
        return self.d, self.n