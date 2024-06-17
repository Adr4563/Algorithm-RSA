from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from PIL import Image
import os

# Clase para manejar el cifrado y descifrado AES
class AESHandler:
    def __init__(self, key):
        self.key = key

    def apply_padding(self, data):
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data) + padder.finalize()
        return padded_data

    def remove_padding(self, data):
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        unpadded_data = unpadder.update(data) + unpadder.finalize()
        return unpadded_data

    def encrypt(self, plaintext, mode, iv=None):
        if mode == modes.ECB:
            cipher = Cipher(algorithms.AES(self.key), mode(), backend=default_backend())
        else:
            cipher = Cipher(algorithms.AES(self.key), mode, backend=default_backend())
        
        encryptor = cipher.encryptor()
        padded_data = self.apply_padding(plaintext)
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        return iv + ciphertext if iv else ciphertext

    def decrypt(self, ciphertext, mode, iv=None):
        if mode == modes.ECB:
            cipher = Cipher(algorithms.AES(self.key), mode(), backend=default_backend())
        else:
            cipher = Cipher(algorithms.AES(self.key), mode, backend=default_backend())
        
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
        unpadded_data = self.remove_padding(decrypted_data)
        return unpadded_data

# Función para convertir imagen a bytes
def image_to_bytes(image_path):
    with open(image_path, 'rb') as image_file:
        return image_file.read()

# Función para convertir bytes a imagen
def bytes_to_image(image_bytes, output_path):
    with open(output_path, 'wb') as image_file:
        image_file.write(image_bytes)

def main():
    # Generar una clave AES de 256 bits
    key = os.urandom(32)
    aes_handler = AESHandler(key)

    # Cargar la imagen y convertirla a bytes
    image_path = 'starcraft.png'
    img_bytes = image_to_bytes(image_path)

    # IV para modos que lo requieran
    iv = os.urandom(16)

    # Modos de cifrado
    modes_dict = {
        'ECB': modes.ECB(),
        'CBC': modes.CBC(iv),
        'CFB': modes.CFB(iv),
    }

    for mode_name, mode in modes_dict.items():
        # Cifrar la imagen
        encrypted_img_bytes = aes_handler.encrypt(img_bytes, mode, iv if mode_name != 'ECB' else None)

        # Guardar la imagen cifrada
        ci_image_path = f'encrypted_image_{mode_name}.bin'
        with open(ci_image_path, 'wb') as file:
            file.write(encrypted_img_bytes)
        
        # Leer la imagen cifrada y descifrarla
        with open(ci_image_path, 'rb') as file:
            encrypted_img_bytes = file.read()
        
        decrypted_img_bytes = aes_handler.decrypt(encrypted_img_bytes, mode, iv if mode_name != 'ECB' else None)
        
        # Guardar la imagen descifrada
        de_image_path = f'decrypted_image_{mode_name}.png'
        bytes_to_image(decrypted_img_bytes, de_image_path)

        print(f'Imagen cifrada con {mode_name} guardada como {ci_image_path}')
        print(f'Imagen descifrada con {mode_name} guardada como {de_image_path}')

main()
