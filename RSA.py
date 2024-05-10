import sys
import logging
import random
import math
import secrets


#Import common functions
try:
    from commonFunctions import *
    logging.debug("File imported successfully.")
except ModuleNotFoundError:
    print("File is missing!")
    logging.critical("File is missing!")
    sys.exit()


#Function for RSA encryption
def RSA_encryption(message, key_size):
    x= convert_to_number(message)
    if n == "":
        key= key_generation(key_size)
    y = hex(fast_raise_power_book(x, e, n)).lstrip("0x")
    print("Result from RSA encryption: y=",y)
    return y

def key_generation(length):
    l = int(length)//4
    #Generate p and q and calculate n
    global n
    global e
    global d
    p= secrets.randbits(l)
    q= secrets.randbits(l)
    n = p*q
    phi = (p-1)*(q-1)
    e = random.randint(2, phi - 1)
    while math.gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    d= inverse(e, phi)
    return n

def RSA_decryption(message, key_size):
    if n == "":
        key= key_generation(key_size)
    y = convert_to_number(message)
    x = convert_to_string(fast_raise_power_book(y,d,n))#need to fix hex result
    print("Result from RSA decryption: x=", x)
    return x

n = ""
e = ""
d = ""

