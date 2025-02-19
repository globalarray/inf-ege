def f(x, y, p):
    if p == 3 and x + y >= 62:
        return 1
    elif p == 3 and x + y < 62:
        return 0
    elif p < 3 and x + y >= 62:
        return 0
    else:
        if p % 2:
            return f(x + 1, y, p + 1) and f(x, y + 1, p + 1) and f(x * 2, y, p + 1) and f(x, y * 2, p + 1)
        else:
            return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x * 2, y, p + 1) or f(x, y * 2, p + 1)
for j in range(1, 52):
    if f(10, j, 0) == 1:
        print(j)
