def f(x, y):
    if x > y or x == 56:
        return 0
    elif x == y:
        return 1
    return f(x + 3, y) + f(x + 7, y) + f(x * 3, y)

print(f(12, 40) * f(40, 72) * f(72, 89))
