f = open("24.txt", 'r').read()

def isSuitableChar(c):
    return c.isdigit() or c in "AB"

tempLen = 0
maxLen = 0

for i in range(len(f)-1):
    exp = f[i]

    if not isSuitableChar(exp) or exp == '0':
        continue

    for j in range(i+1, len(f)):
        if not isSuitableChar(f[j]):
            break

        exp += f[j]

        if int(exp, 12) % 2 == 0:
            maxLen = max(maxLen, len(exp))
print(maxLen)
