import tkinter as tk
import sys
import logging
import random
import secrets

#Import common functions
try:
    from commonFunctions import *
    logging.debug("File imported successfully.")
except ModuleNotFoundError:
    print("File is missing!")
    logging.critical("File is missing!")
    sys.exit()

#Display project menu
def project_menu():
    #Print menu
    logging.info("Printing the menu...")
    print("Crypto group project")
    print("Choose one of the cryptosystems below:")
    print("1. AES")
    print("2. RSA")
    print("0. Quit")
    logging.debug("Menu printed!")
    choice = input(">> ")
    if (choice.isdecimal()):
        if (int(choice) >= 0 and int(choice) < 3):
            logging.debug("Valid option!")
            return int(choice)
    else:
        print("The option chosen is not valid, please try again.")
        logging.debug("Invalid option!")


#Display AES menu
def AES_menu():
    return 1


#Display RSA menu
def RSA_menu():
    return 1



#Function for RSA encryption
def RSA_encryption(x,n,e):
    logging.debug("Encryption RSA: x=%d, n=%d, e=%d" % (x, n, e))
    y = fast_raise_power_book(x, e, n)
    print("Result from RSA encryption: y=" )
    return y


def key_generation(p,q):
    print(p,q)
    n = p*q
    phi = (p-1)*(q-1)
    e=3
    print("gcd= ",my_eea(e, phi))
    while my_eea(e, phi) != 1 and e <= (phi-1):
        e += 3
    return n, e, inverse(e, phi)

def RSA_decryption(y,d,n):
   print(y,n,d)
   x = str(fast_raise_power_book(y,d,n))
   print("Result from RSA decryption: x=" + x)
   return x


x = int(input())
p = int(input())
q = int(input())
n,e,d = key_generation(p,q)
print(n,e,d)
cipher = RSA_encryption(x,n,e)
RSA_decryption(cipher, d,n)



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

# hex 0xFF, binary 0b10101



# AES decryption uses the same key
# does all the layers in reverse order and reverses the internals
# last round of AES doesnt do MixCol
# So first round of AES doesnt do invMixCol

# compute Key Schedule first then use them in reverse order

def AES_decrypt():
    return 1
    # Show AES decryption page

    # # Prompt user to enter cipher text & private key
    # label1 = customtkinter.CTkLabel(master=aesDecryption, text="Enter cipher text: ", font=("Verdana", 18))
    # label1.pack(pady=20, padx=50)
    # entry1 = customtkinter.CTkEntry(aesDecryption)
    # entry1.pack(pady=20, padx=20)
    # label2 = customtkinter.CTkLabel(master=aesDecryption, text="Enter d: ", font=("Verdana", 18))
    # label2.pack(pady=20, padx=50)
    # entry2 = customtkinter.CTkEntry(aesDecryption)
    # entry2.pack(pady=20, padx=20)
    # print(AES_decryption(entry1.get(), entry2.get()))


def AES_encrypt():
    return 1
    # Show AES encryption page
    # show_page(aesEncryption)
    # Hide previous pages
    # hide_page(aesPage)
    # hide_page(aesDecryption)


    # Prompt user to enter plain text & private key
    # label1 = customtkinter.CTkLabel(master=aesEncryption, text="Enter plain text: ", font=("Verdana", 18))
    # label1.pack(pady=20, padx=50)
    # entry1 = customtkinter.CTkEntry(aesEncryption)
    # entry1.pack(pady=20, padx=20)
    # label2 = customtkinter.CTkLabel(master=aesEncryption, text="Enter d: ", font=("Verdana", 18))
    # label2.pack(pady=20, padx=50)
    # entry2 = customtkinter.CTkEntry(aesEncryption)
    # entry2.pack(pady=20, padx=20)

def AES_encryption(plain_text, key):
    # Convert plaintext to binary and pad if needed
    plain_bytes = [ord(c) for c in plain_text]
    while len(plain_bytes) % 16 != 0:
        plain_bytes.append(0)

    # Key Schedule implementation required
    key_schedule = KeySchedule(key)

    # Initial KeyAddition round (key whitening)
    state = KeyAddition(plain_bytes, key_schedule, 0)

    # Perform rounds based on key length
    num_rounds = 10 if len(key) == 16 else 12 if len(key) == 24 else 14

    for round_num in range(1, num_rounds):
        state = ByteSub(state)
        state = ShiftRow(state)
        state = MixCol(state)
        state = KeyAddition(state, key_schedule, round_num)

    # Final round (without MixCol)
    state = ByteSub(state)
    state = ShiftRow(state)
    state = KeyAddition(state, key_schedule, num_rounds)



def AES_decryption(cipher, key):
    # if cipher is text convert it to binary string
    cipher = " ".join(format(ord(c),"b") for c in cipher)
    keySchedule = list(KeySchedule(key)) # should return an array of each subkey
    keySchedule.reverse() # could also just loop thru backwards
    for i in range(len(keySchedule)-1): # keySchedule length is the # of rounds +1
      if(i==0): # first decryption round doesn't MixCol()
          cipher = KeyAddition(cipher, keySchedule[i])
          cipher = InvShiftRows(cipher)
          cipher = InvByteSub(cipher)
      cipher = KeyAddition(cipher, keySchedule[i])
      cipher = InvMixCol(cipher)
      cipher = InvShiftRows(cipher)
      cipher = InvByteSub(cipher)
    cipher = KeyAddition(cipher, keySchedule[len(keySchedule)-1])
    # convert cipher back to text
    cipher = "".join(chr(int(c,2)) for c in cipher.split(" "))
    return cipher


