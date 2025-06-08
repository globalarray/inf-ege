g = {}

def f(n):
    if n < 180: return 24

    if n in g: return g[n]

    g[n] = f(n - 12) + 6

    return g[n]

for i in range(1, 80000):
    f(i)

print(sum(map(int, list(str(f(80000))))))
