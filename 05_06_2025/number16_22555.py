import sys

sys.set_int_max_str_digits(10**6)

g = {}
def f(n):
    if n > 80000:
        return 100

    if n in g:
        return g[n]

    g[n] = f(n + 1) * n

    return g[n]


for n in range(80000-1, 0, -1):
    f(n)

print((int(str(g[50])[:-2]) + g[53])/g[55])
