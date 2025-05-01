f = open("24_21908.txt", 'r').read()

alphabet = "0123456789ABCD"

r = 0

for i in range(len(f)-1):
    if f[i] == '0':
        continue

    if f[i] not in alphabet:
        continue

    for j in range(i+1, len(f)):
        if f[j] not in alphabet:
            break

        z = f[i:(j+1)]

        if z[-1] in "02468AC":
            r = max(len(z), r)
print(r)
