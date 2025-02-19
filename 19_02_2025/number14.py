def f(x, base):
    r = 0

    chrs = "ABC"

    for idx, c in enumerate(x[::-1]):
        idxInChrs = chrs.find(c)

        if idxInChrs != -1:
            r += int("1" + str(idxInChrs)) * (base ** idx)
            continue
        r += int(c) * (base ** idx)
    return r

for j in "0123456789ABC":
    s = f("28" + j + "2", 18) + f("93" + j + "5", 12)

    if s % 133 == 0:
        print(s // 133)
