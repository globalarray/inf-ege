def f(x, p):
    if p == 2 and (x <= 87):
        return 1
    elif p == 2 and (x > 87):
        return 0
    elif p < 2 and (x <= 87):
        return 0
    if p % 2 == 0:
        return f(x - 2, p + 1) and f(x // 2, p + 1)
    return f(x - 2, p + 1) or f(x // 2, p + 1)

for s in range(89, 1000):
    if f(s, 0) == 1:
        print(s)
        break
