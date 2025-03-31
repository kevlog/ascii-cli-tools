import os
import time
import re
import binascii
import pyfiglet
from unidecode import unidecode

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("1. ASCII to Text\n2. Text to ASCII\n3. Generate ASCII Art\n4. Unidecode (Unformat Text Unicode)\n5. Keluar")
    try:
        menu = int(input("Pilih menu : "))
        if menu == 1:
            ascii_hex = str(input("Masukkan ASCII : "))
            if not re.fullmatch(r'[0-9A-Fa-f]+', ascii_hex):
                print("Error: Input harus berupa karakter hex (0-9, A-F)!\a")
                time.sleep(1)
                continue
            if len(ascii_hex) % 2 != 0:
                print("Error: Panjang input harus genap!\a")
                time.sleep(1)
                continue
            try:    
                ascii_decode = bytes.fromhex(ascii_hex).decode("utf-8")
                print("Hasil : ", ascii_decode)
            except ValueError:
                print("Error: Format hex tidak valid atau bukan teks yang bisa di-decode!\a")
                time.sleep(1)

        elif menu == 2:
            text = str(input("Masukkan text : "))
            ascii_hex = binascii.hexlify(text.encode()).decode()
            print("Hasil : ", ascii_hex.upper())
        
        elif menu == 3:
            plain_text = str(input("Masukkan text : "))
            ascii_art = pyfiglet.figlet_format(plain_text)
            print(ascii_art)
        elif menu == 4:
            unicode_text = input("Masukkan unicode : ")
            ascii_text  = unidecode(unicode_text)
            print(ascii_text)
        elif menu == 5:
            print("Terima kasih.")
            time.sleep(1)
            break
        else:
            print("Inputan salah!\a")
            time.sleep(1)

    except ValueError:
        print("Inputan harus angka!\a")
    
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan oleh user. Bye!\a")
        break
    time.sleep(1)