from class_txt import Txt
from Class_RSA import RSA

def main():
    # Archivo 1
    maximo = int(input("Ingrese el valor máximo para el rango: "))
    rsa_instance = RSA(maximo)
    public_key, private_key = rsa_instance.get_public_key(), rsa_instance.get_private_key()
    txt_encryptor = Txt(maximo, public_key, private_key)
    txt_encryptor.encrypt_txt('./C_and_D_txt/archivo_html.txt', './C_and_D_txt/resultados/cifrado.txt')
    txt_encryptor.decripher_txt('./C_and_D_txt/resultados/cifrado.txt', './C_and_D_txt/resultados/descifrado.txt')
    txt_encryptor.print_rsa_keys()
    
    # Archivo 2
    # maximo2 = int(input("Ingrese el valor máximo para el rango del segundo archivo: "))
    # rsa_instance2 = RSA(maximo2)
    # public_key2, private_key2 = rsa_instance2.get_public_key(), rsa_instance2.get_private_key()
    # txt_encryptor2 = Txt(maximo2, public_key2, private_key2)
    # txt_encryptor2.encrypt_txt('./C_and_D_txt/resultados/archivo_html_2.txt', './C_and_D_txt/resultados/cifrado_2.txt')
    # txt_encryptor2.decripher_txt('./C_and_D_txt/resultados/cifrado_2.txt', './C_and_D_txt/resultados/descifrado_2.txt')
    # txt_encryptor2.print_rsa_keys()

main()