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


# AES irreducible polynomial
# P(x)= x^8 + x^4 + x^3 + x + 1 = 100011011

# add/sub = A + B mod p
# multiplication A * B mod P(x)
# inversion A * A^-1 = 1 mod P(x) use my_eea()

# key length 128/192/256
# number of rounds depends on key length
# 128 -> 10
# 192 -> 12
# 256 -> 14

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
