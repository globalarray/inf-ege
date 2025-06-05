def f(x, y):
    if x < y:
        return 0
    elif x == y:
        return 1
    r = f(x - int(str(x)[0]), y)
    lstChr = int(str(x)[-1])

    if lstChr != 0:
        r += f(x - lstChr, y)
    else:
        r += f(x - 2, y)
    r += f(x // 2, y)

    return r
print(f(47, 40) * f(40, 18) * f(18, 14))
