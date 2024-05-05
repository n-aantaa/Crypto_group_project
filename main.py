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

home = customtkinter.CTkFrame(master=root)
home.pack(pady=80, padx=60, fill="both", expand=True)

aesPage = customtkinter.CTkFrame(master= root)
aesPage.pack(pady=80, padx=60, fill="both", expand=True)
aesEncryption = customtkinter.CTkFrame(master= root)
aesEncryption.pack(pady=80, padx=60, fill="both", expand=True)
aesDecryption = customtkinter.CTkFrame(master= root)
aesDecryption.pack(pady=80, padx=60, fill="both", expand=True)

rsaPage = customtkinter.CTkFrame(master= root)
rsaPage.pack(pady=80, padx=60, fill="both", expand=True)
rsaEncryption = customtkinter.CTkFrame(master= root)
rsaEncryption.pack(pady=80, padx=60, fill="both", expand=True)
rsaDecryption = customtkinter.CTkFrame(master= root)
rsaDecryption.pack(pady=80, padx=60, fill="both", expand=True)


#Hide page frame
def hide_page(page):
    page.pack_forget()
#Show page frame
def show_page(page):
    # hide_page(home)
    # hide_page(rsaPage)
    # hide_page(rsaEncryption)
    # hide_page(rsaDecryption)
    # hide_page(aesPage)
    # hide_page(aesEncryption)
    # hide_page(aesDecryption)
    page.tkraise()


def project_menu():
    label = customtkinter.CTkLabel(master=frame, text="Crypto Group Project", font=("Helvetica", 24))
    label.pack(pady=20, padx=30)
    button1 = customtkinter.CTkButton(master=frame, text="AES", font=("Helvetica", 24), command=AES_menu)
    button1.pack(pady=20, padx=20)
    button2 = customtkinter.CTkButton(master=frame, text="RSA", font=("Helvetica", 24), command=RSA_menu)
    button2.pack(pady=20, padx=20)

def AES_menu():
    # Functionality for AES menu
    print("AES Menu selected")

def RSA_menu():
    # Functionality for RSA menu
    button1 = customtkinter.CTkButton(master=frame, text="RSA Encryption", font=("Helvetica", 24), command=RSA_encryption)
    button1.pack(pady=20, padx=20)
    button2 = customtkinter.CTkButton(master=frame, text="RSA Decryption", font=("Helvetica", 24), command=RSA_decryption)
    button2.pack(pady=20, padx=20)

def RSA_encryption():
    show_page(rsaEncryption)
    # Prompt user to enter cipher text & public key
    label1 = customtkinter.CTkLabel(master=rsaEncryption, text="Enter plaintext: ", font=("Verdana", 18))
    label1.pack(pady=20, padx=50)
    entry1 = customtkinter.CTkEntry(rsaEncryption, placeholder_text="x")
    entry1.pack(pady=20, padx=20)
    label2 = customtkinter.CTkLabel(master=rsaEncryption, text="Enter n: ", font=("Verdana", 18))
    label2.pack(pady=20, padx=50)
    entry2 = customtkinter.CTkEntry(rsaEncryption, placeholder_text="n")
    entry2.pack(pady=20, padx=20)
    label3 = customtkinter.CTkLabel(master=rsaEncryption, text="Enter e: ", font=("Verdana", 18))
    label3.pack(pady=20, padx=50)
    entry3 = customtkinter.CTkEntry(rsaEncryption, placeholder_text="e")
    entry3.pack(pady=20, padx=20)

    def rsaEncryptProcess():
        x = int(entry1.get())
        n = int(entry2.get())
        e = int(entry3.get())
        y = fast_raise_power_book(x, e, n)
        return y

    encrypt_button = customtkinter.CTkButton(master=rsaEncryption, text="Encrypt", font=("Verdana", 18), command=rsaEncryptProcess)
    encrypt_button.pack(pady=20)

    # Create label to display the result
    result_label = customtkinter.CTkLabel(master=rsaEncryption, text="", font=("Verdana", 18))
    result_label.pack(pady=20)

def key_generation(p,q):
    n = p*q
    phi = (p-1)*(q-1)
    e = 2
    while my_eea(e, phi) != 1 and e <= (phi-1):
        e += 1
    return inverse(e, phi)

def RSA_decryption():
    # Hide previous pages
    show_page(rsaDecryption)
    # Prompt user to enter cipher text & public key
    label1 = customtkinter.CTkLabel(master=rsaDecryption, text="Enter cipher text: ", font=("Verdana", 18))
    label1.pack(pady=20, padx=50)
    entry1 = customtkinter.CTkEntry(rsaDecryption, placeholder_text="y")
    entry1.pack(pady=20, padx=20)
    label2 = customtkinter.CTkLabel(master=rsaDecryption, text="Enter d: ", font=("Verdana", 18))
    label2.pack(pady=20, padx=50)
    entry2 = customtkinter.CTkEntry(rsaDecryption, placeholder_text="d")
    entry2.pack(pady=20, padx=20)
    label3 = customtkinter.CTkLabel(master=rsaDecryption, text="Enter d: ", font=("Verdana", 18))
    label3.pack(pady=20, padx=50)
    entry3 = customtkinter.CTkEntry(rsaDecryption, placeholder_text="n")
    entry3.pack(pady=20, padx=20)

    # Functionality for RSA decryption
    def rsaEncryptProcess():
        y = int(entry1.get())
        d = int(entry2.get())
        n = int(entry3.get())
        x = fast_raise_power_book(y, d, n)
        return x
    decrypt_button = customtkinter.CTkButton(master=rsaDecryption, text="Encrypt", font=("Verdana", 18), command=rsaEncryptProcess)
    decrypt_button.pack(pady=20)
    # Create label to display the result
    result_label = customtkinter.CTkLabel(master=rsaDecryption, text="", font=("Verdana", 18))
    result_label.pack(pady=20)


project_menu()
root.mainloop()