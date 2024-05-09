P = '100011011'

inverseMatrix = [
0x0E,0x0B,0x0D,0x09,
0x09,0x0E,0x0B,0x0D,
0x0D,0x09,0x0E,0x0B,
0x0B,0x0D,0x09,0x0E]

def add(A, B):
  C = ''
  for i in range(len(A)):
    if A[i] == B[i]:
      C += '0'
    else:
      C += '1'
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

cipher = 0xba75f47a84a48d32e88d060e1b407d5d

cipher = bin(cipher)[2:].zfill(128)
text = ""
for i in range(len(cipher)): # convert cipher and keys to binary strings "11111111 000000000 etc."
    if(i != 0 and i%8 == 0):
        text += " " + cipher[i]
    else:
        text += cipher[i]
cipher = text
text = ""

def InvMixCol(cipher):
  c = list(cipher.split(" "))
  b = []
  for i in range(0,4):
    b[i] = add(add(mod(multiply(c[i],format(inverseMatrix[0], "08b"))),mod(multiply(c[i],format(inverseMatrix[1], "08b")))),add(mod(multiply(c[i],format(inverseMatrix[2], "08b"))),mod(multiply(c[i],format(inverseMatrix[3], "08b")))))
  for i in range(4,8):
    b[i] = add(add(mod(multiply(c[i],format(inverseMatrix[4], "08b"))),mod(multiply(c[i],format(inverseMatrix[5], "08b")))),add(mod(multiply(c[i],format(inverseMatrix[6], "08b"))),mod(multiply(c[8],format(inverseMatrix[7], "08b")))))
  for i in range(8,12):
    b[i] = add(add(mod(multiply(c[i],format(inverseMatrix[8], "08b"))),mod(multiply(c[i],format(inverseMatrix[9], "08b")))),add(mod(multiply(c[i],format(inverseMatrix[10], "08b"))),mod(multiply(c[i],format(inverseMatrix[11], "08b")))))
  for i in range(12,16):
    b[i] = add(add(mod(multiply(c[i],format(inverseMatrix[12], "08b"))),mod(multiply(c[i],format(inverseMatrix[13], "08b")))),add(mod(multiply(c[i],format(inverseMatrix[14], "08b"))),mod(multiply(c[i],format(inverseMatrix[15], "08b")))))
  result = ""
  for i in range(len(b)):
    result += b[i] + " "
  result = result.rstrip() # gets rid of trailing space
  return result
result = InvMixCol(cipher)
r = list(result.split(" "))
text = ""
for i in range(len(r)):
    text += format(int(r[i],2), "02x")
print(text)