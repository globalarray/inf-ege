g = {}

def f(n):
    if n <= 1: return 1

    if n in g:
        return g[n]
    g[n] = n + f(n - 3)

    return g[n]

for x in range(16026):
    f(x)

print(f(16025) - f(16021))
