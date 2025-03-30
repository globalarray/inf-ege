f = open("24_58328.txt", 'r').read()

mx = 0
tempLen = 0

for i in range(len(f)-1):
    if f[i] != f[i+1]:
        tempLen += 1
    else:
        mx = max(tempLen + 1, mx)
        tempLen = 0
print(mx)
