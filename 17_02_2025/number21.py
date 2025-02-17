def f(x, p):
    if (p == 2 or p == 4) and x > 41:
        return 1
    elif p == 4 and x < 42:
        return 0
    elif p < 4 and x > 41:
        return 0
    else:
        if p % 2 == 0:
            return f(x + 1, p + 1) and f(x + 2, p + 1) and f(x * 2, p + 1)
        else:
            return f(x + 1, p + 1) or f(x + 2, p + 1) or f(x * 2, p + 1)
for z in range(1, 42):
    if f(z, 0) == 1:
        print("Задача 21: ", z)
        break
