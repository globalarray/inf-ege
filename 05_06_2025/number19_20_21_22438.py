def f(x, m):
    if x <= 23:
        return m % 2 == 0
    if m == 0: return 0

    h = [f(x - 3, m - 1), f(x // 2 + (x % 2), m -1)]

    return any(h) if m % 2 != 0 else all(h)

print([s for s in range(24, 100) if f(s, 2)])
print([s for s in range(24, 100) if not(f(s, 1)) and f(s, 3)])
print([s for s in range(24, 1000) if not(f(s, 2)) and f(s, 4)])
