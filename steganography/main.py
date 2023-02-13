import numpy as np
from PIL import Image
import tkinter as tk




def Encode(src, message, dest):

    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n

    message += "$t3g0"
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)

    if req_pixels > total_pixels:
        print("ERROR: Uzun dosya formatına ihtiyac var")

    else:
        index=0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1

        array=array.reshape(height, width, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(dest)
        print("Resim şifreleme başarılı")
def Decode(src):

    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    message = ""
    for i in range(len(hidden_bits)):
        if message[-5:] == "$t3g0":
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    if "$t3g0" in message:
        print("Gizlenen Mesaj:", message[:-5])
    else:
        print("Gizlenen Mesaj Yok")


def Stego():


    print("Şifrelemeye Hoşgeldiniz")
    print("1: Şifrele")
    print("2: Şifre Çöz")
    func=input()





    if func == '1':
        print("Resim dosyasını giriniz (uzantısı ile birlikte)")
        src = input()

        print("Gizlenecek Mesajı giriniz")
        message = input()

        print("Mesaj gizlenmiş resmin ismini giriniz(uzantısı ile birlikte)")
        dest = input()


        print("Şifreleniyor...")
        Encode(src, message, dest)

    elif func == '2':
        print("Şifrelenmiş resim dosyasını giriniz(uzantısı ile birlikte)")
        src = input()
        print("Şifre çöz")
        Decode(src)

    else:
        print("ERROR: Invalid option chosen")





if __name__ == "__main__":
    Stego()



