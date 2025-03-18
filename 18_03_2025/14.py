defs = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'J': 17}

def toDec(expression, fr):
    r = 0

    for idx, c in enumerate(expression[::-1]):
        if c in defs:
            c = defs[c]
        else:
            c = int(c)

        r += int(c) * (fr**idx)
    return r

for x in range(18):
    v = str(x)

    if x > 10:
        v = list(defs.keys())[x - 11]

    e = toDec("2AB" + v, 12) + toDec(v + "8E", 17)

    if e % 27 == 0:
        print(e // 27)
