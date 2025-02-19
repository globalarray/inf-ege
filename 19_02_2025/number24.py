f = open("24_19.txt", 'r').read()

r = 0

tempLen = 0

for c in f:
    if c == 'B':
        tempLen += 1
    else:
        if tempLen != 0:
            r = max(tempLen, r)
            tempLen = 0
if tempLen != 0:
    r = max(r, tempLen)

print(r)
