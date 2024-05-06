cipher = "Hello World"
cipher = " ".join(format(ord(c),"b") for c in cipher)
subKey = "11110000 00001111"
subKey = " ".join(format(ord(c),"b") for c in subKey)
c = list(cipher.split(" "))
s = list(subKey.split(" "))
x = []
for i in range(0,2):
    print(c[i])
    print(s[i])
    x.append(f'{int(c[i],2) ^ int(s[i],2):08b}')
print(x[1])
