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

P = '100011011'
inverseMatrix = [
0x0E,0x0B,0x0D,0x09,
0x09,0x0E,0x0B,0x0D,
0x0D,0x09,0x0E,0x0B,
0x0B,0x0D,0x09,0x0E]
print()
