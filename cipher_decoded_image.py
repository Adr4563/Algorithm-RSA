from PIL import Image
import csv
from datetime import datetime
import time
#**************************************************************** Path of files CSV
csv_file_cifrado = './C_and_D_png/files_csv/cifrado.csv'
csv_file_descifrado = './C_and_D_png/files_csv/descifrado.csv'


#**************************************************************** Image cipher (PNG/JPG)
def cipher_image(input_image, output_image, output_file,e,n):
    image = Image.open(input_image)
    pixels = list(image.getdata())
    # print(image.size)
    # print(pixels)     : [(255,255,255),....]
    # print(image.size) : RGBA (255,255,255,255) ||  RGB (255,255,255)
    cipher_pixels = []
    
    data = []
    for pixel in pixels:
        list_pixel = []
        timestamp_start = time.time()  
        for value in pixel:
            cipher_value = pow(value, e, n)
            # print(cipher_value)  
            list_pixel.append(cipher_value)
        timestamp_end = time.time()
        time_taken = (timestamp_end - timestamp_start)
        data.append([time_taken, pixel, tuple(list_pixel)])

            
        cipher_pixels.append(tuple(list_pixel )) 
        # Primer segmento de pixeles de la fila n
    #  Calcular el "cipher_value"
    #  Public key = 659447
    #  n = 230459
    #  Example: (255,100,255) => (255**659447) mod n
    #  (255,100,255) => (255**6) mod n
    #  (255,100,255) => (100**6) mod n
        
    # print(cipher_pixels) : [(255,255,255,255)......]
    new_image = Image.new(image.mode, image.size)
    new_image.putdata(cipher_pixels)
    # print(list(new_image.getdata()))
    new_image.save(output_image)     
    print(f"Imagen cifrada se guarda en:  '{output_image}'")
    
    new_image_pixels = list(new_image.getdata())
    # Agregar la nueva columna a los datos
    new_data = []
    for data1, new_pixel in zip(data, new_image_pixels):
        new_data.append(data1 + [new_pixel])
        
    # Data in txt
    with open(output_file, 'w') as file:
        for item in cipher_pixels:
            file.write(f"{item}\n")
       
    
    # Data to CSV
    with open(csv_file_cifrado, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["TimeStamp", "Pixel_Value", "Ciphered_Value","Image_Pixel_Value_"])
        writer.writerows(new_data)

    print(f"Datos de cifrado guardados en: '{csv_file_cifrado}'")

def decoded_image(input_image, input_file, output_image, d, n):
    # Correct form
    cipher_pixels_file = []
    with open(input_file, 'r') as file:
        for line in file:
            cipher_values =  line.strip().strip('()').split(', ')
            pixel = tuple(int(value) for value in cipher_values)
            cipher_pixels_file.append(pixel)
        # print(cipher_pixels_file)
    
    decoded_pixels_file = []
    data1 = []

    for pixel in cipher_pixels_file:
        list_pixel = []
        timestamp_start = time.time()
        for value in pixel:
            decoded_value = pow(value, d, n)
            list_pixel.append(decoded_value)
        timestamp_end = time.time()
        time_taken = (timestamp_end - timestamp_start)
        data1.append([time_taken, pixel, tuple(list_pixel)])
        decoded_pixels_file.append(tuple(list_pixel))
        
    # Wrong Form
    cipher_image = Image.open(input_image)
    cipher_pixels = list(cipher_image.getdata())
    decoded_pixels = []
    data = []
    
    for pixel in cipher_pixels:
        list_pixel = []
        timestamp_start = time.time()  
        for value in pixel:
            decoded_value = pow(value, d, n)
            list_pixel.append(decoded_value)
        timestamp_end = time.time()
        time_taken = (timestamp_end - timestamp_start)
        data.append([time_taken, pixel, tuple(list_pixel)])
        decoded_pixels.append(tuple(list_pixel))
        
    new_image = Image.new(cipher_image.mode, cipher_image.size)
    new_image.putdata(decoded_pixels_file)
    new_image.save(output_image)
    print(f"Imagen descifrada se guarda en: '{output_image}'")
    
    # Data to CSV
    with open(csv_file_descifrado, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["TimeStamp", "Ciphered_Value", "Pixel_Value"])
        writer.writerows(data1)
    
    print(f"Datos de descifrado guardados en: '{csv_file_descifrado}'")