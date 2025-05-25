import math

def f(x, y):
    if x < y or x == 24:
        return 0
    elif x == y:
        return 1
    r = f(x - 1, y) + f(int(math.sqrt(x)), y)

    if x > 9:
        st = str(x)
        r += f(int(st[:len(st)-1]), y)
    return r
print(f(602, 7))
