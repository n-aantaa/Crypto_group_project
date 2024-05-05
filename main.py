import sys
import logging
import random
import customtkinter

try:
    from commonFunctions import *
    logging.debug("File imported successfully.")
except ModuleNotFoundError:
    print("File is missing!")
    logging.critical("File is missing!")
    sys.exit()

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.geometry("1024x1024")

# frame = customtkinter.CTkFrame(master=root)
# frame.pack(pady=20, padx=60, fill="both", expand=True)
#


def project_menu():
    # label = customtkinter.CTkLabel(master=frame, text="Crypto Group Project", font=("Helvetica", 24))
    # label.pack(pady=20, padx=30)
    # button1 = customtkinter.CTkButton(master=frame, text="AES", font=("Helvetica", 24), command=AES_menu)
    # button1.pack(pady=20, padx=20)
    # button2 = customtkinter.CTkButton(master=frame, text="RSA", font=("Helvetica", 24), command=RSA_menu)
    # button2.pack(pady=20, padx=20)
    return 1

def AES_menu():
    # Functionality for AES menu
    print("AES Menu selected")

def RSA_menu():
    # Functionality for RSA menu
    # button1 = customtkinter.CTkButton(master=frame, text="RSA Encryption", font=("Helvetica", 24), command=RSA_encryption)
    # button1.pack(pady=20, padx=20)
    # button2 = customtkinter.CTkButton(master=frame, text="RSA Decryption", font=("Helvetica", 24), command=RSA_decryption)
    # button2.pack(pady=20, padx=20)
    return 1

def RSA_encryption():
    # Functionality for RSA encryption
    n = int(input("Enter n: "))
    e = int(input("Enter e: "))
    x = int(input("Enter plaintext: "))
    y = fast_raise_power_book(x, e, n)
    print("Encrypted:", y)

def key_generation(p,q):
    n = p*q
    phi = (p-1)*(q-1)
    e = random.randint(1, phi - 1)
    while my_eea(e, phi) != 1:
        e = random.randint(1, phi-1)
    return inverse(e, phi)

def RSA_decryption():
    # Functionality for RSA decryption
    d= key_generation(34,40)
    y = int(input("Enter ciphertext: "))
    n = int(input("Enter n: "))
    x = fast_raise_power_book(y, d, n)
    print("Decrypted:", x)



# project_menu()
# root.mainloop()
