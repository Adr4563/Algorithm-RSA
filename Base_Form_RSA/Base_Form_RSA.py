import random
import math

def is_prime(num):    
    if num < 2 or num % 2 == 0:
        return False
    if num == 2:
        return True
    
    for d in range(3, int(math.sqrt(num)) + 1):
        if num % d == 0:
            return False
    return True

def generate_prime(max):
    while True:
        num = random.randint(1, max)
        if is_prime(num):
            return num
        
def generate_different_primes(max):
    p,q = generate_prime(max), generate_prime(max)
    # Asegurarse de que p y q son diferentes
    while p == q:
        q = generate_prime(max)
    return p, q
        
# Generate Priveeet        
def mod_inverse(e, phi_n):
    for d in range(3, phi_n):
        if (d * e) % phi_n == 1:
            return d
    raise ValueError("mod_inverse doesn't exist")

def generate_public_key(phi_n):
    # Citar Código:*
    e = random.randint(3, phi_n - 1)
    while math.gcd(e, phi_n) != 1:
        e = random.randint(3, phi_n - 1)
    return e

def rsa_encrypt(message, e, n):
        ciphertext = []
        for char in message:
            #Characters ASCII
            char_code = ord(char)
            encrypted_char = pow(char_code, e, n)
            ciphertext.append(encrypted_char)

        return ciphertext

def rsa_decrypt(ciphertext, d, n):
    decipher_text = []
    for encrypted_char in ciphertext:
        dechipher_char_code = pow(encrypted_char, d, n)
        decrypted_char = chr(dechipher_char_code)
        decipher_text.append(decrypted_char)
            
    return "".join(decipher_text)


def main():
    max = int(input("Ingrese el valor máximo para el rango: "))
    p, q = generate_different_primes(max)
    
    # Calculate n and phi_n     
    n = p * q
    phi_n = (p - 1) * (q - 1)
    print("phi_n: ",phi_n)
    
    # Public Key
    e = generate_public_key(phi_n)
    print(e)
    
    # Private Key
    d = mod_inverse(e, phi_n)
    
    # Results
    print("Public key (e, n):", e)
    print("Private key (d, n):", d)
    print("n:", n)
    print("phi_n:", phi_n)
    print("p:", p)
    print("q:", q)
    
    message = "1234"
    # Public Key & n
    ciphertext = rsa_encrypt(message,e,n)
    print(ciphertext)   
    
    # Private Key & n
    decipher_text  = rsa_decrypt(ciphertext, d, n)
    print(decipher_text)  

main()