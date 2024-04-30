# import customtkinter
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
    return


def RSA_decryption():
    return

# customtkinter.set_appearance_mode("light")
# customtkinter.set_default_color_theme("dark-blue")




# root = customtkinter.CTk()
# root.geometry("500x500")
#
# def login():
#     print("test")
#
# frame = customtkinter.CTkFrame(master=root)
# frame.pack(pady=20, padx=60, fill="both", expand=True)
#
# label = customtkinter.CTkLabel(master=frame, text="Crypto Group Project", font=("Helvetica",24))
# label.pack(pady=20, padx=30)
#
# button1 = customtkinter.CTkButton(master=frame, text="AES", font=("Helvetica",24))
# button1.pack(pady=20, padx=20)
#
# root.mainloop()
