def f(x, m):
    if x <= 19:
        return m % 2 == 0
    if m == 0: return 0

    h = []

    if x % 2 == 0:
        h.append(f(x // 2, m - 1))
    if x % 3 == 0:
        h.append(f(x // 3, m - 1))
    if x % 3 != 0 and x % 2 != 0:
        h.append(f(x + 1, m - 1))
    h.append(f(x - 5, m - 1))

    return any(h) if m % 2 != 0 else all(h)

print([s for s in range(20, 100) if f(s, 2)])
print([s for s in range(20, 100) if not(f(s, 1)) and f(s, 3)])
print([s for s in range(20, 100) if not(f(s, 2)) and f(s, 4)])
