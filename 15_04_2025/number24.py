f = open("24.txt", 'r').read()

r = 0

for i in range(len(f)-1):
    aCnt = 0

    if f[i] == 'A':
        aCnt += 1
    for j in range(i+1, len(f)):
        if f[j] == 'A':
            aCnt += 1
        if aCnt > 1:
            r = max(r, (j - i))
            break
print(r)
