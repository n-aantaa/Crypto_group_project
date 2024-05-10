def KeyAddition(cipher, subKey):
  c = list(cipher.split(" "))
  s = list(subKey.split(" "))
  x = []
  for i in range(len(c)):
    x.append(format(int(c[i],2) ^ int(s[i],2), "08b")) # XOR needs binary ints then string format result save to x
  result = ""
  for i in range(len(x)):
    result += x[i] + " "
  result = result.rstrip() # gets rid of trailing space
  return result

cipher = 0x09668b78a2d19a65f0fce6c47b3b3089
cipher = bin(cipher)[2:].zfill(128)
text = ""
for i in range(len(cipher)): # convert cipher and keys to binary strings "11111111 000000000 etc."
    if(i != 0 and i%8 == 0):
        text += " " + cipher[i]
    else:
        text += cipher[i]
cipher = text
key = 0xBFE2BF904559FAB2A16480B4F7F1CBD8
key = bin(key)[2:].zfill(128)
text = ""
for i in range(len(key)): # convert cipher and keys to binary strings "11111111 000000000 etc."
    if(i != 0 and i%8 == 0):
        text += " " + key[i]
    else:
        text += key[i]
key = text

print(KeyAddition(cipher,key))