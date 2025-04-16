def to10(n):
    r = 0

    for idx, c in enumerate((str(n))[::-1]):
        r += int(c) * (21 ** idx)
    return r

for x in range(21):
    v = to10(int("82934" + str(x) + "2")) + to10(int("2924" + (str(x) * 2) + "7")) + to10(int("67564" + str(x) + "8"))

    if v % 20 == 0:
        print(v // 20)
        break
