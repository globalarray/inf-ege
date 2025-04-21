def f(x, p):
    if x >= 128:
        return p % 2 == 0
    if p == 0:
        return 0
    h = [f(x + 2, p-1), f(x + 5, p-1), f(x * 2, p-1)]

    return all(h) if p%2==0 else any(h)
print(19, [s for s in range(2, 127) if f(s, 2)])
print(20, [s for s in range(2, 127) if not(f(s, 1)) and f(s, 3)])
print(21, [s for s in range(2, 127) if not(f(s, 2)) and f(s, 4)])
