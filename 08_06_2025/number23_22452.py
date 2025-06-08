def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    return f(x + 2, y) + f(x + 4, y) + f(x * 2, y)
print(((f(12, 22) * f(22, 38))+(f(12, 24) * f(24, 38)))-(2 * f(12, 22) * f(22, 24) * f(24, 38)))
