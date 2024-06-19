from PIL import Image
from Class_RSA import RSA

# Incluye el formato JPG / PNG
class PNG(RSA):
    def __init__(self, max, public_key, private_key):
        super().__init__(max)
        self.public_key = public_key
        self.private_key = private_key

    def encrypt_png(self, input_image, output_image):
        image = Image.open(input_image)
        pixels = list(image.getdata())
        # print(pixels)     : [(255,255,255),....]
        # print(image.size) : RGBA (255,255,255,255) ||  RGB (255,255,255)
        cipher_pixels = []

        for pixel in pixels:
            list_pixel = [] 
            for value in pixel:
                cipher_value = pow(value, self.public_key[0], self.public_key[1]) # 
                list_pixel .append(cipher_value)
            cipher_pixels.append(tuple(list_pixel )) # Primer segmento de pixeles de la fila n
            #  Calculatar el cipher_value
            #  Public key = 659447
            #  Example: (255,100,255) => (255**Public-Key[0]) mod public_key[1]
            #  (255,100,255) => (255**6) mod 5
            #  (255,100,255) => (100**6) mod 5
        
        # print(cipher_pixels) : [(255,255,255,255)......]
        new_image = Image.new(image.mode, image.size)
        new_image.putdata(cipher_pixels)
        new_image.save(output_image)
        
        print(f"Imagen cifrada se guarda en:  '{output_image}'")

    def decrypt_png(self, input_image, output_image):
        cipher_image = Image.open(input_image)
        cipher_pixels = list(cipher_image.getdata())
        decoded_pixels = []

        for pixel in cipher_pixels:
            decoded_pixel = tuple(pow(value, self.private_key[0], self.private_key[1]) for value in pixel)
            decoded_pixels.append(decoded_pixel)

        new_image = Image.new(cipher_image.mode, cipher_image.size)
        new_image.putdata(decoded_pixels)
        new_image.save(output_image)
        print(f"Imagen descifrada se guarda en: '{output_image}'")

    def print_rsa_keys(self):
        print(f"Public key (e, n): {self.public_key}")
        print(f"Private key (d, n): {self.private_key}")
