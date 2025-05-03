f = open("24_16333.txt", 'r').read()

r = 0

for i in range(len(f)-1):
    if f[i].isdigit() == f[i+1].isdigit():
        continue

    for j in range(i+1, len(f)):
        if j == (i - 1):
            continue
        if f[j].isdigit() == f[j-1].isdigit():
            break
        l = len(f[i:j+1])

        r = max(r, l)
print(r)
