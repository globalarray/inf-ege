def f(x,m):
    if x >= 21:
        return m % 2 == 0
    if m == 0: return 0

    h = [f(x + 1, m - 1), f(x * 2, m - 1)]

    return any(h) if m % 2 != 0 else all(h)

print(min([s for s in range(1, 21) if not(f(s, 1)) and f(s, 3)]))
print(min([s for s in range(1, 21) if not(f(s, 2)) and f(s, 4)]))
print(" ".join([str(e) for e in [s for s in range(1, 21) if not(f(s, 1)) and not(f(s, 3)) and f(s, 5)][:2]]))
