def f(z, v):
    if z > v:
        return 0
    elif z == v:
        return 1
    return f(z + 2, v) + f(z + 5, v)
print(f(1, 20))
