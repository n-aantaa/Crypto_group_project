def add(A, B):
  C = ''
  for i in range(len(A)):
    if A[i] == B[i]:
      C += '0'
    else:
      C += '1'
  return C

def multiply(A, B):
  C = '0' # result
  for i in range(len(B)-1, -1, -1):
    if B[i] == '1':
      C = add(C, A)
    A = A + '0'
  return C

print(multiply("11111111","10000000"))
