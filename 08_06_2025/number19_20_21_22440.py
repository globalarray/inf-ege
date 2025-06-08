def f(x, y, m):
    if x+y <= 212:
        return m % 2 == 0
    if m == 0: return 0

    h = [f(x - 2, y, m - 1), f(x, y - 2, m - 1), f(x // 2, y, m - 1), f(x, y // 2, m - 1)]

    return any(h) if m % 2 != 0 else all(h)
#print(max([s for s in range(103, 1000) if f(s, 110, 2)])) #411

print([s for s in range(103, 1000) if not(f(s, 110, 1)) and f(s, 110, 3)])
print([s for s in range(103, 1000) if not(f(s, 110, 2)) and f(s, 110, 4)])
