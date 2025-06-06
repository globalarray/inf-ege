def f(x, y, h):
    if x > y or h.count('*') > 2:
        return 0
    elif x == y:
        return 1
    return f(x + 1, y, h+"+") + f(x + 2, y, h+"+") + f(x * 2, y, h+"*")
print(f(2, 12, ""))
