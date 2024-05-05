import customtkinter
import sys
import logging

try:
    from commonFunctions import *
    logging.debug("File imported successfully.")
except ModuleNotFoundError:
    print("File is missing!")
    logging.critical("File is missing!")
    sys.exit()



def RSA_encryption():
    print()
    n = int( input())
    e= int( input())
    x=int( input())
    y=fast_raise_power_book(x, e, n)
    return y


def RSA_decryption():
    d= int( input())
    y= int( input())
    n = int(input())
    x= fast_raise_power_book(y,d,n)
    return x


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")




root = customtkinter.CTk()
root.geometry("1024x1024")

def login():
    print("test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Crypto Group Project", font=("Helvetica",24))
label.pack(pady=20, padx=30)

button1 = customtkinter.CTkButton(master=frame, text="AES", font=("Helvetica",24), command=login())
button1.pack(pady=20, padx=20)

root.mainloop()
