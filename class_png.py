from PIL import Image
from Class_RSA import RSA

# Incluye el formato JPG y PNG
class PNG(RSA):
    def __init__(self, max, public_key, private_key):
        super().__init__(max)
        self.public_key = public_key
        self.private_key = private_key

    def encrypt_png(self, input_image, output_image):
        image = Image.open(input_image)
        pixels = list(image.getdata())
        print(image.size)
        # print(list(image.getdata()))  #: RGBA (255,255,255,255) ||  RGB (255,255,255)
        encrypted_pixels = []

        for pixel in pixels:
            encrypted_pixel = tuple(pow(value, self.public_key[0], self.public_key[1]) for value in pixel)
            encrypted_pixels.append(encrypted_pixel)
        
        # print(encrypted_pixels = []) : (255,255,255,255)
        encrypted_image = Image.new(image.mode, image.size)
        encrypted_image.putdata(encrypted_pixels)
        encrypted_image.save(output_image
        )
        print(f"Imagen cifrada se guarda en:  '{output_image}'")

    def decrypt_png(self, input_image, output_image
    ):
        encrypted_image = Image.open(input_image)
        encrypted_pixels = list(encrypted_image.getdata())
        decrypted_pixels = []

        for encrypted_pixel in encrypted_pixels:
            decrypted_pixel = tuple(pow(value, self.private_key[0], self.private_key[1]) for value in encrypted_pixel)
            decrypted_pixels.append(decrypted_pixel)

        decrypted_image = Image.new(encrypted_image.mode, encrypted_image.size)
        decrypted_image.putdata(decrypted_pixels)
        decrypted_image.save(output_image)
        print(f"Imagen descifrada se guarda en: '{output_image}'")

    def print_rsa_keys(self):
        print(f"Public key (e, n): {self.public_key}")
        print(f"Private key (d, n): {self.private_key}")
