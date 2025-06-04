from re import *
from fnmatch import fnmatch

"""for n in range(0, 10**9, 13):
    if fullmatch(r'24[02468]*68[39]35', str(n)):
        print(n, n // 13)
# слишком легкий способ."""

print("====================")

limitN = int("24" + "9" * max([i for i in range(30) if int("24" + ("9" * i)) <= 10**9]))

for n in range(0, 10**9, 13):
    nStr = str(n)
    d = int(nStr[0:2])

    if d < 24:
        continue

    if n > limitN:
        break

    if fnmatch(nStr, "24*68?35"):
        suit1 = True

        sixIdx = 0

        for idx in range(2, len(nStr)):
            if nStr[idx] + nStr[idx+1] == '68' and (len(nStr) - (idx+1)) == 4:
                sixIdx = idx
                break
            if nStr[idx] not in "02468":
                suit1 = False
                break
        if not suit1:
            continue

        if nStr[sixIdx+2] not in "39":
            continue

        print(n, n // 13)
