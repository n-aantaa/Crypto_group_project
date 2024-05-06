def inverse(r0,r1):
  s0=1
  s1=0
  t0=0
  t1=1

  rs = r1
  while r1 != 0:
    r=r0%r1
    q = r0//r1
    s = s0-q *s1
    t=t0-q*t1
    s0=s1
    s1=s
    t0=t1
    t1=t
    r0=r1
    r1=r
  return (s0+rs)%rs


def fast_raise_power_book(x,n,p):
  nb=bin(n)[2:]
  result=1
  for i in range(len(nb)):
    result= (result* result)%p
    if nb[i] == '1':
      result = (result * x) % p
  return result


def my_eea(r0,r1):
  #Initialize data
  s0=1
  s1=0
  t0=0
  t1=1

  while(r1!=0):
    r= r0 % r1
    q = r0//r1
    s = s0 - q*s1
    t= t0 - q*t1

    #Update r, s, t
    r0=r1
    r1=r
    s0=s1
    s1=s
    t0=t1
    t1=t

  return r0, s0, t0

#add polynomials together
def add(A, B):
  # make sure A, B have the same length
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
  return result

# AES Sbox from Table 4.3
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

# inverse AES Sbox from Table 4.4
inverseAESSBox = [
[0x52,0x09,0x6A,0xD5,0x30,0x36,0xA5,0x38,0xBF,0x40,0xA3,0x9E,0x81,0xF3,0xD7,0xFB],
[0x7C,0xE3,0x39,0x82,0x9B,0x2F,0xFF,0x87,0x34,0x8E,0x43,0x44,0xC4,0xDE,0xE9,0xCB],
[0x54,0x7B,0x94,0x32,0xA6,0xC2,0x23,0x3D,0xEE,0x4C,0x95,0x0B,0x42,0xFA,0xC3,0x4E],
[0x08,0x2E,0xA1,0x66,0x28,0xD9,0x24,0xB2,0x76,0x5B,0xA2,0x49,0x6D,0x8B,0xD1,0x25],
[0x72,0xF8,0xF6,0x64,0x86,0x68,0x98,0x16,0xD4,0xA4,0x5C,0xCC,0x5D,0x65,0xB6,0x92],
[0x6C,0x70,0x48,0x50,0xFD,0xED,0xB9,0xDA,0x5E,0x15,0x46,0x57,0xA7,0x8D,0x9D,0x84],
[0x90,0xD8,0xAB,0x00,0x8C,0xBC,0xD3,0x0A,0xF7,0xE4,0x58,0x05,0xB8,0xB3,0x45,0x06],
[0xD0,0x2C,0x1E,0x8F,0xCA,0x3F,0x0F,0x02,0xC1,0xAF,0xBD,0x03,0x01,0x13,0x8A,0x6B],
[0x3A,0x91,0x11,0x41,0x4F,0x67,0xDC,0xEA,0x97,0xF2,0xCF,0xCE,0xF0,0xB4,0xE6,0x73],
[0x96,0xAC,0x74,0x22,0xE7,0xAD,0x35,0x85,0xE2,0xF9,0x37,0xE8,0x1C,0x75,0xDF,0x6E],
[0x47,0xF1,0x1A,0x71,0x1D,0x29,0xC5,0x89,0x6F,0xB7,0x62,0x0E,0xAA,0x18,0xBE,0x1B],
[0xFC,0x56,0x3E,0x4B,0xC6,0xD2,0x79,0x20,0x9A,0xDB,0xC0,0xFE,0x78,0xCD,0x5A,0xF4],
[0x1F,0xDD,0xA8,0x33,0x88,0x07,0xC7,0x31,0xB1,0x12,0x10,0x59,0x27,0x80,0xEC,0x5F],
[0x60,0x51,0x7F,0xA9,0x19,0xB5,0x4A,0x0D,0x2D,0xE5,0x7A,0x9F,0x93,0xC9,0x9C,0xEF],
[0xA0,0xE0,0x3B,0x4D,0xAE,0x2A,0xF5,0xB0,0xC8,0xEB,0xBB,0x3C,0x83,0x53,0x99,0x61],
[0x17,0x2B,0x04,0x7E,0xBA,0x77,0xD6,0x26,0xE1,0x69,0x14,0x63,0x55,0x21,0x0C,0x7D]]

# AES irreducible polynomial
# P(x)= x^8 + x^4 + x^3 + x + 1 = 100011011
P = '100011011'

inverseMatrix = [
0x0E,0x0B,0x0D,0x09,
0x09,0x0E,0x0B,0x0D,
0x0D,0x09,0x0E,0x0B,
0x0B,0x0D,0x09,0x0E]

keyScheduleIter = 0

def KeySchedule(key):
  key = "".join(key.split())
  keyArray = []
  keyArray.append(key) # key 0
  w = []
  word = ""
  for i in len(key): # splits key with no spaces into 32bits chunks
    word += key[i]
    if(i % 32 == 31):
      w.append(word) # add 32 bit chunk to array
      word = ""
  for i in range(0,11): # 11 keys in 128bit
    keyScheduleIter = i
    w.append(int(w[i*4]) ^ int(g(w[(i+1)*4 - 1]))) # i.e. i=0 -> w[4] = w[0] XOR g(w[3])
    w.append(int(w[(i+1)*4]) ^ int(w[i+1])) # w[5] = w[4] XOR w[1]
    w.append(int(w[(i+1)*4 + 1]) ^ int(w[i+2])) # w[6] = w[5] XOR w[2]
    w.append(int(w[(i+1)*4 + 2]) ^ int(w[i+3])) # w[7] = w[6] XOR w[3]
    for i in range((i+1)*4,len(w)):
      word += w[i]
    keyArray.append(word)
    word = ""
  return keyArray
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

def g(word):
  wa = ""
  v = []
  for i in range(len(word)): # splits word with no spaces into 8bits chunks
    wa += word[i]
    if(i % 8 == 7):
      v.append(wa) # add 8 bit chunk to array
      wa = ""
  v.append(v[0]) # rotate left
  del v[0]
  result = ""
  for i in range(len(v)):
    xy = hex(int(v[i],2))
    x = int(xy[2],16)
    y = int(xy[3],16)
    result += f'{AESSBox[x][y]:08b}'
    if(i==0):
      result = int(result) ^ rc[keyScheduleIter]
  return result
# [V₀][V₁][V₂][V₃] rotate left
# [V₁][V₂][V₃][V₀]
#  S   S   S   S
# only S([V₁]) gets XORd with RC[i] result
# g() result = [ W[4] ]
rc = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1B,0x36]
# Round Coefficient 1,...,10
# RC[i] =
# RC[1]= x0 =(00000001)2
# RC[2]= x1 =(00000010)2
# RC[3]= x2 =(00000100)2
# ...
# RC[10]= x9 =(00110110)2.

def KeyAddition(cipher, subKey):
  c = list(cipher.split(" "))
  s = list(subKey.split(" "))
  x = []
  for i in len(c):
    x.append(f'{int(c[i],2) ^ int(s[i],2):08b}') # XOR needs binary ints then string format result save to x
  result = ""
  for i in x:
    result += x[i] + " "
  result = result.rstrip() # gets rid of trailing space
  return result
# KeyAddition() XOR keys 8bit bytes to MixCols 8bit bytes result
# D[][][][] [][][][] [][][][] [][][][]
# XOR straight down
# E[][][][] [][][][] [][][][] [][][][]

def InvMixCol(cipher):
  c = list(cipher.split(" "))
  b = []
  for i in range(0,4):
    b[i] = add(add(mod(multiply(c[i],f'{inverseMatrix[0]:08b}')),mod(multiply(c[i],f'{inverseMatrix[1]:08b}'))),add(mod(multiply(c[i],f'{inverseMatrix[2]:08b}')),mod(multiply(c[i],f'{inverseMatrix[3]:08b}'))))
  for i in range(4,8):
    b[i] = add(add(mod(multiply(c[i],f'{inverseMatrix[4]:08b}')),mod(multiply(c[i],f'{inverseMatrix[5]:08b}'))),add(mod(multiply(c[i],f'{inverseMatrix[6]:08b}')),mod(multiply(c[8],f'{inverseMatrix[7]:08b}'))))
  for i in range(8,12):
    b[i] = add(add(mod(multiply(c[i],f'{inverseMatrix[8]:08b}')),mod(multiply(c[i],f'{inverseMatrix[9]:08b}'))),add(mod(multiply(c[i],f'{inverseMatrix[10]:08b}')),mod(multiply(c[i],f'{inverseMatrix[11]:08b}'))))
  for i in range(12,16):
    b[i] = add(add(mod(multiply(c[i],f'{inverseMatrix[12]:08b}')),mod(multiply(c[i],f'{inverseMatrix[13]:08b}'))),add(mod(multiply(c[i],f'{inverseMatrix[14]:08b}')),mod(multiply(c[i],f'{inverseMatrix[15]:08b}'))))
  result = ""
  for i in b:
    result += b[i] + " "
  result = result.rstrip() # gets rid of trailing space
  return result
# B0   0E 0B 0D 09   C0
# B1 = 09 0E 0B 0D * C1
# B2   0D 09 0E 0B   C2
# B3   0B 0D 09 0E   C3
# B₀ = 0E*C₀ + 0B*C₁ + 01*C₁₀ + 01*C₁₅
# Additions in the vector–matrix multiplication are bitwise XORs.

def InvShiftRows(cipher):
  l = list(cipher.split(" "))
  l.insert(4,l[7]) #insert pretty much right shifts once
  del l[8] # delete the original l[7] which is now l[8]
  l.insert(8,l[11]) # right shift twice
  l.insert(8,l[11])
  del l[12] # delete values shifted past row 3
  del l[12]
  l.insert(12,l[15]) # right shift 3 times
  l.insert(12,l[15])
  l.insert(12,l[15])
  del l[16] # delete values shifter past row 4
  del l[16]
  del l[16]
  result = ""
  for i in l:
    result += l[i] + " "
  result = result.rstrip() # gets rid of trailing space
  return result
# need to reverse all the indexes swap
# [0 4 8 12] to     [0 4 8 12] no change
# [1 5 9 13] to     [13 1 5 9] right shift 1
# [2 6 10 14] to    [10 14 2 6] right shift 2
# [3 7 11 15] to    [7 11 15 3] right shift 3

def InvByteSub(cipher):
  result = ""
  for c in cipher.split(" "):
    xy = hex(int(c,2))
    x = int(xy[2],16)
    y = int(xy[3],16)
    result += f'{inverseAESSBox[x][y]:08b}' + " "
  result = result.strip() # gets rid of trailing space
  return result
# apply each byte to inverseAESSBox