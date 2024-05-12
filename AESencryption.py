AESSBox = [
[0x63,0x7C,0x77,0x7B,0xF2,0x6B,0x6F,0xC5,0x30,0x01,0x67,0x2B,0xFE,0xD7,0xAB,0x76],
[0xCA,0x82,0xC9,0x7D,0xFA,0x59,0x47,0xF0,0xAD,0xD4,0xA2,0xAF,0x9C,0xA4,0x72,0xC0],
[0xB7,0xFD,0x93,0x26,0x36,0x3F,0xF7,0xCC,0x34,0xA5,0xE5,0xF1,0x71,0xD8,0x31,0x15],
[0x04,0xC7,0x23,0xC3,0x18,0x96,0x05,0x9A,0x07,0x12,0x80,0xE2,0xEB,0x27,0xB2,0x75],
[0x09,0x83,0x2C,0x1A,0x1B,0x6E,0x5A,0xA0,0x52,0x3B,0xD6,0xB3,0x29,0xE3,0x2F,0x84],
[0x53,0xD1,0x00,0xED,0x20,0xFC,0xB1,0x5B,0x6A,0xCB,0xBE,0x39,0x4A,0x4C,0x58,0xCF],
[0xD0,0xEF,0xAA,0xFB,0x43,0x4D,0x33,0x85,0x45,0xF9,0x02,0x7F,0x50,0x3C,0x9F,0xA8],
[0x51,0xA3,0x40,0x8F,0x92,0x9D,0x38,0xF5,0xBC,0xB6,0xDA,0x21,0x10,0xFF,0xF3,0xD2],
[0xCD,0x0C,0x13,0xEC,0x5F,0x97,0x44,0x17,0xC4,0xA7,0x7E,0x3D,0x64,0x5D,0x19,0x73],
[0x60,0x81,0x4F,0xDC,0x22,0x2A,0x90,0x88,0x46,0xEE,0xB8,0x14,0xDE,0x5E,0x0B,0xDB],
[0xE0,0x32,0x3A,0x0A,0x49,0x06,0x24,0x5C,0xC2,0xD3,0xAC,0x62,0x91,0x95,0xE4,0x79],
[0xE7,0xC8,0x37,0x6D,0x8D,0xD5,0x4E,0xA9,0x6C,0x56,0xF4,0xEA,0x65,0x7A,0xAE,0x08],
[0xBA,0x78,0x25,0x2E,0x1C,0xA6,0xB4,0xC6,0xE8,0xDD,0x74,0x1F,0x4B,0xBD,0x8B,0x8A],
[0x70,0x3E,0xB5,0x66,0x48,0x03,0xF6,0x0E,0x61,0x35,0x57,0xB9,0x86,0xC1,0x1D,0x9E],
[0xE1,0xF8,0x98,0x11,0x69,0xD9,0x8E,0x94,0x9B,0x1E,0x87,0xE9,0xCE,0x55,0x28,0xDF],
[0x8C,0xA1,0x89,0x0D,0xBF,0xE6,0x42,0x68,0x41,0x99,0x2D,0x0F,0xB0,0x54,0xBB,0x16]]

def add(A, B):
    while len(A) > len(B):
        B = '0' + B
    while len(B) > len(A):
        A = '0' + A
    C = ''
    for i in range(len(A)):
        if A[i] == B[i]:
            C += '0'
        else:
            C += '1'
    # get rid of zeros in front of C
    i = 0
    while i < len(C) and C[i] == '0':
        i += 1
    if i == len(C): # all 0s
        C = '0'
    else:
        C = C[i:]
    return C

# mult polynomials
def multiply(A, B):
  C = '0' # result
  for i in range(len(B)-1, -1, -1):
    if B[i] == '1':
      C = add(C, A)
    A = A + '0'
  return C

# mult then mod
def mod(A):
    result = A
    while len(result) >= len(P):
        left = add(result[:len(P)], P)
        right = result[len(P):]
        result = left + right
    result = str(result).zfill(8)
    return result

mixMatrix = [
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03, 0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02]
]

P = '100011011'

rc = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1B,0x36]
def g(z,round_num):
  v = [z[i:i+2] for i in range(0,len(z),2)]
  v.append(v[0]) # rotate left
  del v[0]
  result = ""
  for i in range(0,4):
      x = int(v[i][0],16)
      y = int(v[i][1],16)
      if(i==0):
          v[i] = AESSBox[x][y] ^ rc[round_num]
      else:
          v[i] = AESSBox[x][y]
      result += format(v[i],"02x")
  result = int(result,16)
  return result


def KeySchedule(key):
  key = format(key,"032x")
  keyArray = []
  keyArray.append(key) # key 0
  w = []
  word = ""
  for i in range(0,4): # break key into word size chunks w[0] to w[3]
      for j in range(i*8,(i+1)*8):
          word += key[j]
      w.append(word)
      word = ""
  for i in range(0,10): # 11 keys in 128bit and 1 already appended
      w.append(format(int(w[i*4],16) ^ g(w[(i+1)*4 - 1],i),"08x")) # i.e. i=0 -> w[4] = w[0] XOR g(w[3])
      w.append(format(int(w[(i+1)*4],16) ^ int(w[(i+1)*4 - 3],16),"08x")) # w[5] = w[4] XOR w[1]
      w.append(format(int(w[(i+1)*4 + 1],16) ^ int(w[(i+1)*4 - 2],16),"08x")) # w[6] = w[5] XOR w[2]
      w.append(format(int(w[(i+1)*4 + 2],16) ^ int(w[(i+1)*4 - 1],16),"08x")) # w[7] = w[6] XOR w[3]
      for j in range((i+1)*4,len(w)): # combine last 4 words into 1 key
          word += w[j]
      keyArray.append(word)
      word = ""
  return keyArray


def MixCol(cipher):
    c = list(cipher.split(" "))
    a = []
    for i in range(len(c)):
        c[i] = bin(int(c[i],16))[2:].zfill(8)
    cipher2d = []
    for i in range(4):  # the tower of power
        a.append(c[i])
    cipher2d.append(a)
    a = []
    for i in range(4,8):
        a.append(c[i])
    cipher2d.append(a)
    a = []
    for i in range(8,12):
        a.append(c[i])
    cipher2d.append(a)
    a = []
    for i in range(12,16):
        a.append(c[i])
    cipher2d.append(a)
    b = []
    m = []
    for i in range(len(c)): # for each byte
        for j in range(0,4):
            m.append(mod(multiply(cipher2d[i//4][j], format(mixMatrix[i%4][j], "08b"))))
        b.append(add(add(add(m[0],m[1]).zfill(8),m[2]).zfill(8),m[3]).zfill(8))
        m=[]
    result = ""
    for i in range(len(b)):
        b[i] = hex(int(b[i],2))[2:].zfill(2)
        result += b[i] + " "
    result = result.rstrip() # gets rid of trailing space
    return result


def ShiftRows(cipher):
    l = cipher.split(" ")
    # Perform left shifts on the rows
    # Row 1: No change
    # Row 2: Shift left by 1
    l[1], l[5], l[9], l[13] = l[5], l[9], l[13], l[1]
    # Row 3: Shift left by 2
    l[2], l[6], l[10], l[14] = l[10], l[14], l[2], l[6]
    # Row 4: Shift left by 3
    l[3], l[7], l[11], l[15] = l[15], l[3], l[7], l[11]

    result = " ".join(l)
    return result


def ByteSub(cipher):
    result = ""
    for c in cipher.split(" "):
        # Convert binary string to hexadecimal
        xy = hex(int(c,16))[2:].zfill(2)
        # Extract the row (x) and column (y) indices for the S-box
        x = int(xy[0], 16)  # Get the higher nibble for the row index
        y = int(xy[1], 16)  # Get the lower nibble for the column index
        # Apply the S-box substitution and convert the result back to binary
        result += format(AESSBox[x][y], "02x") + " "
    # Strip the trailing space from the final result string
    result = result.strip()
    return result

mixMatrix = [
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03, 0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02]
]


def KeyAddition(cipher, subKey):
    c = cipher.split(" ")
    s = subKey.split(" ")
    x = []
    for i in range(len(c)):
        # XOR the hex values directly, format the result back to hex with padding
        xor_result = int(c[i], 16) ^ int(s[i], 16)
        x.append(format(xor_result, "02x"))
    result = " ".join(x)
    return result



def AES_encryption(plain, key):
    cipher = plain
    cipher = hex(cipher)[2:].zfill(32) # conversion monstrosity to turn plain hex into "54 77 6f etc."
    cipher = [str(cipher)[i:i+2] for i in range(0,len(str(cipher)),2)]
    cipher = " ".join(cipher)
    key_schedule = KeySchedule(key)  # Generate all round keys
    for j in range(len(key_schedule)):
        key_schedule[j] = [key_schedule[j][i:i+2] for i in range(0,len(key_schedule[j]),2)] # conversion monstrosity to turn keys hex into "54 68 61 etc."
        key_schedule[j] = " ".join(key_schedule[j])
    cipher = KeyAddition(cipher, key_schedule[0]) # key whitening
    for i in range(10):  # Perform 10 rounds of AES operations
        cipher = ByteSub(cipher)  # Assuming ByteSub is corrected to handle hex strings
        cipher = ShiftRows(cipher)  # Assuming ShiftRows is corrected to handle hex strings
        if i < 9:  # Last round does not use MixColumns
            cipher = MixCol(cipher)
        cipher = KeyAddition(cipher, key_schedule[i+1])
    return cipher  # Returning hex string for simplicity, convert to string if needed

plain = 0x54776F204F6E65204E696E652054776F
key = 0x5468617473206D79204B756E67204675
print(AES_encryption(plain,key))