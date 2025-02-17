def f(x, p):
    if p == 2 and x > 41:
        return 1
    elif p == 2 and x < 41:
        return 0
    elif p < 2 and x > 41:
        return 0
    else:
        if p % 2:
            return f(x + 1, p + 1) or f(x + 2, p + 1) or f(x * 2, p + 1)
        else:
            return f(x + 1, p + 1) or f(x + 2, p + 1) or f(x * 2, p + 1)
for j in range(1, 42):
    if f(j, 0) == 1:
        print(j)
        break
