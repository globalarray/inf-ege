def f(y, e):
    return ((y & 103 == 0) and (y & 94 != 0)) <= (y & e != 0)

for a in range(1000):
    if all([f(x, a) for x in range(1, 1000)]):
        print(a)
        break
