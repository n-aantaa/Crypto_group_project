import sys
import logging
import random
import math
import secrets
import rsa
from sympy import randprime



# Import common functions
try:
    from commonFunctions import *
    logging.debug("File imported successfully.")
except ModuleNotFoundError:
    print("File is missing!")
    logging.critical("File is missing!")
    sys.exit()

# Function for RSA encryption
def RSA_encryption(message, key_size):
    global n, e
    if n == 0:
        key_generation(key_size)
    x = int(convert_to_number(message))
    y = fast_raise_power_book(x, e, n)
    print("Result from RSA encryption: y=", y)
    return '\n'.join([str(y)[i:i+120] for i in range(0, len(str(y)), 120)])

def key_generation(length):
    global n, e, d
    l = int(length)
    lower_bound = 2 ** (l - 1)
    upper_bound = 2 ** l - 1
    # Generate p and q and calculate n
    p = randprime(lower_bound, upper_bound)
    q = randprime(lower_bound, upper_bound)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi - 1)
    while math.gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    d = inverse(e, phi)%phi
    return n

def RSA_decryption(message, key_size):
    global n, d
    if n == 0:
        key_generation(key_size)
    y = convert_to_number(message)
    print(y, d, n)
    x = fast_raise_power_book(y, d, n)
    print(y, d, n)
    print("Result from RSA encryption: x=", x)
    x= convert_to_string(x)
    return x

n = 0
e = 0
d = 0

