import tkinter as tk
from tkinter import ttk
from RSA import RSA_encryption, RSA_decryption
from AES import AES_encryption, AES_decryption

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Crypto Group Project")
        self.geometry("400x400")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (StartPage, RSAPage, AESPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)



        label = tk.Label(self, text="Choose one of the cryptosystems below:", font=("Arial", 18))
        label.pack(pady=10, padx= 5)

        rsa_button = tk.Button(self, text="RSA", height= 2, width=8, command=lambda: controller.show_frame(RSAPage))
        rsa_button.pack(pady=10)

        aes_button = tk.Button(self, text="AES", height= 2, width=8,command=lambda: controller.show_frame(AESPage))
        aes_button.pack(pady=10)

        members = tk.Label(self, text="By: Oumar MBALLO \n Ndeye Anta MBAYE \n Dustin RILEY", font=("Arial", 14))
        members.pack(pady=20)

class RSAPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="RSA Encryption/Decryption", font=("Arial", 16))
        label.pack(pady=10)

        self.key_size_var = tk.StringVar()
        key_size_label = tk.Label(self, text="Select Key Size:")
        key_size_label.pack()
        key_size_menu = ttk.Combobox(self, textvariable=self.key_size_var, values=["1024", "2048", "4096"])
        key_size_menu.pack()

        self.message_entry = tk.Entry(self, width=30)
        self.message_entry.pack(pady=10)

        encrypt_button = tk.Button(self, text="Encryption", command=lambda: self.select_operation("encrypt"))
        encrypt_button.pack()

        decrypt_button = tk.Button(self, text="Decryption", command=lambda: self.select_operation("decrypt"))
        decrypt_button.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

        self.controller = controller

    def select_operation(self, operation):
        key_size = int(self.key_size_var.get())
        message = self.message_entry.get()

        if operation == "encrypt":
            result = RSA_encryption(message, key_size)
        elif operation == "decrypt":
            result = RSA_decryption(message, key_size)

        self.result_label.config(text=result)

class AESPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="AES Encryption/Decryption", font=("Arial", 16))
        label.pack(pady=10)

        encrypt_button = tk.Button(self, text="Encryption", command=lambda: self.select_operation("encrypt"))
        encrypt_button.pack()

        decrypt_button = tk.Button(self, text="Decryption", command=lambda: self.select_operation("decrypt"))
        decrypt_button.pack()

        self.key_size_var = tk.StringVar()
        key_size_label = tk.Label(self, text="Select Key Size:")
        key_size_label.pack()
        key_size_menu = ttk.Combobox(self, textvariable=self.key_size_var, values=["128", "192", "256"])
        key_size_menu.pack()

        self.message_entry = tk.Entry(self, width=30)
        self.message_entry.pack(pady=10)

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

        self.controller = controller

    def select_operation(self, operation):
        key_size = int(self.key_size_var.get())
        message = self.message_entry.get()

        if operation == "encrypt":
            result = aes_encrypt(message, key_size)
        elif operation == "decrypt":
            result = aes_decrypt(message, key_size)

        self.result_label.config(text=result)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
