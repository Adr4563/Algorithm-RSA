from class_png import PNG
from Class_RSA import RSA

def main():
    maximo = int(input("Ingrese el valor máximo para el rango: "))
    rsa_instance = RSA(maximo)
    public_key, private_key = rsa_instance.get_public_key(), rsa_instance.get_private_key()
    png_encryptor = PNG(maximo, public_key, private_key)
    
    # PNG, JPG
    png_encryptor.encrypt_png('./C_and_D_png/box.png', './C_and_D_png/resultados/cifrado.png')
    png_encryptor.decrypt_png('./C_and_D_png/resultados/cifrado.png', './C_and_D_png/resultados/descifrado.png')

    
    png_encryptor.print_rsa_keys()

if __name__ == "__main__":
    main()