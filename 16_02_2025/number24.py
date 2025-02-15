f = open("24_16_02.txt", "r").read()

r = 0

tempLen = 0

#0 - гласная, 1 - согласная, 2 - сброс
state = 2

for c in f:
    isSogl = c in "CDF"

    if state == 2:
        if isSogl is False:
            continue
        state = int(isSogl)
        tempLen += 1
        continue
    elif state == 1:
        if isSogl is False:
            tempLen += 1
            r = max(tempLen, r)
            state = 0
            continue
    elif state == 0:
        if isSogl is True:
            tempLen += 1
            r = max(tempLen, r)
            state = 1
            continue
    tempLen = 0
    state = 2
print(r // 2)
