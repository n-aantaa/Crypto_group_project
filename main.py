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

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.geometry("1024x1024")


#Hide page frame
def hide_page(page):
    page.pack_forget()
#Show page frame
def show_page(page):
    page.tkraise()


def project_menu():
    show_page(home)
    label = customtkinter.CTkLabel(master=home, text="Crypto Group Project", font=("Verdana", 24))
    label.pack(pady=20, padx=50)
    option = customtkinter.CTkLabel(master=home, text="Choose one cryptosystem below:", font=("Verdana", 18))
    option.pack(pady=20, padx=30)
    button1 = customtkinter.CTkButton(master=home, text="AES", font=("Helvetica", 20), command=AES_menu)
    button1.pack(pady=20, padx=20)
    button2 = customtkinter.CTkButton(master=home, text="RSA", font=("Helvetica", 20), command=RSA_menu)
    button2.pack(pady=20, padx=20)
    members = customtkinter.CTkLabel(master=home, text="By: Oumar MBALLO\nNdeye Anta MBAYE\nDustin RILEY",
                                     font=("Verdana", 12))
    members.pack(pady=20, padx=30)


def AES_menu():
    # show_page(rsaPage)
    hide_page(home)
    show_page(aesPage)
    # Functionality for RSA menu
    button1 = customtkinter.CTkButton(master=aesPage, text="AES Encryption", font=("Helvetica", 24),
                                      command=RSA_encryption)
    button1.pack(pady=20, padx=20)
    button2 = customtkinter.CTkButton(master=aesPage, text="AES Decryption", font=("Helvetica", 24),
                                      command=RSA_decryption)
    button2.pack(pady=20, padx=20)


def RSA_menu():
    # show_page(rsaPage)
    hide_page(home)
    show_page(rsaPage)
    # Functionality for RSA menu
    button1 = customtkinter.CTkButton(master=rsaPage, text="RSA Encryption", font=("Helvetica", 24), command=RSA_encryption)
    button1.pack(pady=20, padx=20)
    button2 = customtkinter.CTkButton(master=rsaPage, text="RSA Decryption", font=("Helvetica", 24), command=RSA_decryption)
    button2.pack(pady=20, padx=20)


def RSA_encryption():
    hide_page(rsaPage)
    hide_page(rsaDecryption)
    hide_page(aesPage)
    hide_page(aesEncryption)
    hide_page(aesDecryption)

    show_page(rsaEncryption)
    # Prompt user to enter cipher text & public key
    label1 = customtkinter.CTkLabel(master=rsaEncryption, text="Enter plaintext: ", font=("Verdana", 18))
    label1.pack(pady=20, padx=50)
    entry1 = customtkinter.CTkEntry(rsaEncryption)
    entry1.pack(pady=20, padx=20)
    label2 = customtkinter.CTkLabel(master=rsaEncryption, text="Enter n: ", font=("Verdana", 18))
    label2.pack(pady=20, padx=50)
    entry2 = customtkinter.CTkEntry(rsaEncryption)
    entry2.pack(pady=20, padx=20)
    label3 = customtkinter.CTkLabel(master=rsaEncryption, text="Enter e: ", font=("Verdana", 18))
    label3.pack(pady=20, padx=50)
    entry3 = customtkinter.CTkEntry(rsaEncryption)
    entry3.pack(pady=20, padx=20)

    # Create label to display the result

    def rsaEncryptProcess():
        x = int(entry1.get())
        n = int(entry2.get())
        e = int(entry3.get())
        y = str(fast_raise_power_book(x, e, n))
        return "Encrypted result: "+ y


    decrypt_button = customtkinter.CTkButton(master=rsaEncryption, text="Encrypt", font=("Verdana", 18),
                                             command=rsaEncryptProcess)
    decrypt_button.pack(pady=20)
    result_label = customtkinter.CTkLabel(master=rsaEncryption, text=y, font=("Verdana", 18))
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
    hide_page(rsaPage)
    hide_page(rsaEncryption)
    show_page(rsaDecryption)
    # Prompt user to enter cipher text & private key
    label1 = customtkinter.CTkLabel(master=rsaDecryption, text="Enter cipher text: ", font=("Verdana", 18))
    label1.pack(pady=20, padx=50)
    entry1 = customtkinter.CTkEntry(rsaDecryption)
    entry1.pack(pady=20, padx=20)
    label2 = customtkinter.CTkLabel(master=rsaDecryption, text="Enter d: ", font=("Verdana", 18))
    label2.pack(pady=20, padx=50)
    entry2 = customtkinter.CTkEntry(rsaDecryption)
    entry2.pack(pady=20, padx=20)
    label3 = customtkinter.CTkLabel(master=rsaDecryption, text="Enter n: ", font=("Verdana", 18))
    label3.pack(pady=20, padx=50)
    entry3 = customtkinter.CTkEntry(rsaDecryption)
    entry3.pack(pady=20, padx=20)

    # Functionality for RSA decryption
    def rsaDecryptProcess():
        y = int(entry1.get())
        d = int(entry2.get())
        n = int(entry3.get())
        x = fast_raise_power_book(y, d, n)
        return x
    decrypt_button = customtkinter.CTkButton(master=rsaDecryption, text="Decrypt", font=("Verdana", 18), command=rsaDecryptProcess)
    decrypt_button.pack(pady=20)
    # Create label to display the result
    result_label = customtkinter.CTkLabel(master=rsaDecryption, text="", font=("Verdana", 18))
    result_label.pack(pady=20)




# key length 128/192/256
# number of rounds depends on key length
# 128 -> 10
# 192 -> 12
# 256 -> 14
# add/sub = A + B mod p
# multiplication A * B mod P(x)
# inversion A * A^-1 = 1 mod P(x) use my_eea()
# AES encrypts all bits in 1 round
# Fig 4.2 in book (High level view)
# 1 round looks like Fig 4.3
# Each round has 4 layers (turn into functions for coding I think)
# 1 ByteSub (confusion)
# 2 ShiftRow (diffusion)
# 3 MixCol (diffusion)
# 4 Key addition ()
# last round does not have the MixCol layer
# At the beginning of AES and at the very end the subKey is added
# called "key whitening"


# Inside the layers

# ByteSub() recieves key
# split key into bytes (8bits)
# A[][][][] [][][][] [][][][] [][][][]
#  S S S S  S S S S  S S S S  S S S S straight down
# B[][][][] [][][][] [][][][] [][][][]
# all S() same
# python has built in hex() function to convert values to hex -> 0xFF
# Table 4.3 need to copy the S table as 2d array
# Example Ai -> hex C2₁₆ = C,2 = (x,y) -> look up x,y in table
# S(Ai) -> hex -> spit out STableArray[x][y]

# ShiftRow()
# B[0][1][2][3] [4][5][6][7] [8][9][10][11] [12][13][14][15]
# move the 8bit bytes around
# C[0][5][10][15] [4][9][14][3] [8][13][2][7] [12][1][6][11]
# [0 4 8 12] to     [0 4 8 12] no change
# [1 5 9 13] to     [5 9 13 1] left shift 1
# [2 6 10 14] to    [10 14 2 6] left shift 2
# [3 7 11 15] to    [15 3 7 11] left shift 3

# MixCol() matrix multiplication
# C[][][][] [][][][] [][][][] [][][][]
# matrix multiply within 32bit sections
# C[      ] [      ] [      ] [      ]
# D[][][][] [][][][] [][][][] [][][][]
#
# D₀    [02 03 01 01]   C₀
# D₁ =  [01 02 03 01] * C₅
# D₂    [01 01 02 03]   C₁₀
# D₃    [03 01 01 02]   C₁₅
# hex 8 bits   01 = 00000001 or 1, 02 = 00000010 or x, 03 = 00000011 or x+1
# D₀ = 02*C₀ + 03*C₅ + 01*C₁₀ + 01*C₁₅
#  * is GF(2^8) mult    + is GF(2^8) add

# KeyAddition() XOR keys 8bit bytes to MixCols 8bit bytes result
# D[][][][] [][][][] [][][][] [][][][]
# XOR straight down
# E[][][][] [][][][] [][][][] [][][][]

# Key Schedule
# key = k₀ ... K₁₅
# K is 8bits byte of key
# W[i] = W[0] ... W[43]
# W[i] is 32bits word
# [][][][] [][][][] [][][][] [][][][] Ki each 8bits
# [ W[0] ] [ W[1] ] [ W[2] ] [ W[3] ] W[i] each 32bits
# g()XOR  -> XOR  ->  XOR  ->  XOR
# [ W[4] ] [ W[5] ] [ W[6] ] [ W[7] ] W[i] each 32bits
# g(W[3]) XOR W[0] = W[4]
# W[4] XOR W[1] = W[5]
# W[5] XOR W[2] = W[6]
# W[6] XOR W[3] = W[7]

# g() inner workings
# [V₀][V₁][V₂][V₃] rotate left
# [V₁][V₂][V₃][V₀]
#  S   S   S   S
# only S([V₁]) gets XORd with RC[i] result
# g() result = [ W[4] ]

# Round Coefficient 1,...,10
# RC[i] =
# RC[1]= x0 =(00000001)2
# RC[2]= x1 =(00000010)2
# RC[3]= x2 =(00000100)2
# ...
# RC[10]= x9 =(00110110)2.

# hex 0xFF, binary 0b10101



# AES decryption uses the same key
# does all the layers in reverse order and reverses the internals
# last round of AES doesnt do MixCol
# So first round of AES doesnt do invMixCol

# compute Key Schedule first then use them in reverse order

def AES_decrypt():
    show_page(aesDecryption)
def AES_encrypt():
    show_page(aesEncryption)
def AES_decryption(cipher, key):
    # if cipher is text convert it to binary string
    cipher = " ".join(format(ord(c),"b") for c in cipher)
    keySchedule = KeySchedule(key) # should return an array of each subkey
    keySchedule.reverse() # could also just loop thru backwards
    for i in len(keyShedule)-1: # keySchedule length is the # of rounds +1
      if(i==0): # first decryption round doesn't MixCol()
          cipher = KeyAddition(cipher, keySchedule[i])
          cipher = InvShiftRows(cipher)
          cipher = InvByteSub(cipher)
      cipher = KeyAddition(cipher, keySchedule[i])
      cipher = InvMixCol(cipher)
      cipher = InvShiftRows(cipher)
      cipher = InvByteSub(cipher)
    cipher = KeyAddition(cipher, keySchedule[len(keyShedule)-1])
    # convert cipher back to text
    cipher = "".join(chr(int(c,2)) for c in cipher.split(" "))
    return cipher


home = customtkinter.CTkFrame(master=root)
home.pack(pady=80, padx=60, fill="both", expand=True)

#RSA frames
rsaPage = customtkinter.CTkFrame(master = root)
rsaPage.pack(pady=80, padx=60, fill="both", expand=True)
rsaEncryption = customtkinter.CTkFrame(master= root)
rsaEncryption.pack(pady=80, padx=60, fill="both", expand=True)
rsaDecryption = customtkinter.CTkFrame(master= root)
rsaDecryption.pack(pady=80, padx=60, fill="both", expand=True)

#AES frames
aesPage = customtkinter.CTkFrame(master= root)
aesPage.pack(pady=80, padx=60, fill="both", expand=True)
aesEncryption = customtkinter.CTkFrame(master= root)
aesEncryption.pack(pady=80, padx=60, fill="both", expand=True)
aesDecryption = customtkinter.CTkFrame(master= root)
aesDecryption.pack(pady=80, padx=60, fill="both", expand=True)



project_menu()
root.mainloop()
