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
rsaPage = customtkinter.CTkFrame(master=root)
rsaPage.pack(pady=80, padx=60, fill="both", expand=True)

rsaEncryption = customtkinter.CTkFrame(master=root)
rsaEncryption.pack(pady=80, padx=60, fill="both", expand=True)
rsaDecryption = customtkinter.CTkFrame(master=root)
rsaDecryption.pack(pady=80, padx=60, fill="both", expand=True)

# Show page frame
def show_page(page):
    page.tkraise()

# Hide page frame
def hide_page(page):
    page.pack_forget()

def project_menu():
    show_page(home)
    label = customtkinter.CTkLabel(master=home, text="Crypto Group Project", font=("Verdana", 24))
    label.pack(pady=20, padx=50)
    option = customtkinter.CTkLabel(master=home, text="Choose one cryptosystem below:", font=("Verdana", 18))
    option.pack(pady=20, padx=30)
    button1 = customtkinter.CTkButton(master=home, text="AES", font=("Helvetica", 20), command=AES_menu)
    button1.pack(pady=20, padx=20)
    button2 = customtkinter.CTkButton(master=home, text="RSA", font=("Helvetica", 20), command= RSA_menu)
    button2.pack(pady=20, padx=20)
    members = customtkinter.CTkLabel(master=home, text="By: Oumar MBALLO\nNdeye Anta MBAYE\nDustin RILEY", font=("Verdana", 12))
    members.pack(pady=20, padx=30)

def AES_menu():
    # Functionality for AES menu
    print("AES Menu selected")
    return ""

def RSA_menu():
    hide_page(home)
    show_page(rsaPage)
    # Functionality for RSA menu
    print("RSA Menu selected")
    button1 = customtkinter.CTkButton(master=rsaPage, text="RSA Encryption", font=("Verdana", 24), command=RSA_encryption)
    button1.pack(pady=20, padx=20)
    button2 = customtkinter.CTkButton(master=rsaPage, text="RSA Decryption", font=("Verdana", 24), command=RSA_decryption)
    button2.pack(pady=20, padx=20)
    homeButton = customtkinter.CTkButton(master=rsaPage, text="Home page", font=("Verdana", 24), command=project_menu)
    homeButton.pack(pady=20, padx=20)

def RSA_encryption():
    # Hide previous pages
    hide_page(rsaPage)
    show_page(rsaEncryption)
    # Prompt user to enter plaintext & public key
    label1 = customtkinter.CTkLabel(master=rsaEncryption, text="Enter plaintext (x): ", font=("Verdana", 18))
    label1.pack(pady=20, padx=50)
    entry1 = customtkinter.CTkEntry(rsaEncryption, placeholder_text="x")
    entry1.pack(pady=20, padx=20)
    label2 = customtkinter.CTkLabel(master=rsaEncryption, text="Enter n (public key modulus): ", font=("Verdana", 18))
    label2.pack(pady=20, padx=50)
    entry2 = customtkinter.CTkEntry(rsaEncryption, placeholder_text="n")
    entry2.pack(pady=20, padx=20)
    label3 = customtkinter.CTkLabel(master=rsaEncryption, text="Enter e (public key exponent): ", font=("Verdana", 18))
    label3.pack(pady=20, padx=50)
    entry3 = customtkinter.CTkEntry(rsaEncryption, placeholder_text="e")
    entry3.pack(pady=20, padx=20)

    def rsa_encrypt_process():
        try:
            x = int(entry1.get())
            n = int(entry2.get())
            e = int(entry3.get())
            y = fast_raise_power_book(x, e, n)
            result_label.config(text=f"Result: {y}")
        except ValueError:
            result_label.config(text="Invalid input! Please enter valid integers.")

    encrypt_button = customtkinter.CTkButton(master=rsaEncryption, text="Encrypt", font=("Verdana", 18), command=rsa_encrypt_process)
    encrypt_button.pack(pady=20)

    # Create label to display the result
    result_label = customtkinter.CTkLabel(master=rsaEncryption, text="", font=("Verdana", 18))
    result_label.pack(pady=20)

def key_generation(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while my_eea(e, phi) != 1 and e <= (phi - 1):
        e += 1
    return inverse(e, phi)

def RSA_decryption():
    # Hide previous pages
    hide_page(rsaPage)
    show_page(rsaDecryption)
    # Prompt user to enter ciphertext & private key
    label1 = customtkinter.CTkLabel(master=rsaDecryption, text="Enter ciphertext (y): ", font=("Verdana", 18))
    label1.pack(pady=20, padx=50)
    entry1 = customtkinter.CTkEntry(rsaDecryption, placeholder_text="y")
    entry1.pack(pady=20, padx=20)
    label2 = customtkinter.CTkLabel(master=rsaDecryption, text="Enter d (private key exponent): ", font=("Verdana", 18))
    label2.pack(pady=20, padx=50)
    entry2 = customtkinter.CTkEntry(rsaDecryption, placeholder_text="d")
    entry2.pack(pady=20, padx=20)
    label3 = customtkinter.CTkLabel(master=rsaDecryption, text="Enter n (public key modulus): ", font=("Verdana", 18))
    label3.pack(pady=20, padx=50)
    entry3 = customtkinter.CTkEntry(rsaDecryption, placeholder_text="n")
    entry3.pack(pady=20, padx=20)

    def rsa_decrypt_process():
        try:
            y = int(entry1.get())
            d = int(entry2.get())
            n = int(entry3.get())
            x = fast_raise_power_book(y, d, n)
            result_label.config(text=f"Result: {x}")
        except ValueError:
            result_label.config(text="Invalid input! Please enter valid integers.")

    decrypt_button = customtkinter.CTkButton(master=rsaDecryption, text="Decrypt", font=("Verdana", 18), command=rsa_decrypt_process)
    decrypt_button.pack(pady=20)

    # Create label to display the result
    result_label = customtkinter.CTkLabel(master=rsaDecryption, text="", font=("Verdana", 18))
    result_label.pack(pady=20)


project_menu()
root.mainloop()
