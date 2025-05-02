def f(x, m):
    if x >= 128:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(x + 2, m - 1), f(x + 5, m - 1), f(x * 2, m - 1)]

    return any(h) if m % 2 != 0 else all(h)

print("19)", [i for i in range(2, 127) if f(i, 2)])
print("20)", [i for i in range(2, 127) if not(f(i, 1)) and f(i, 3)])
print("21)", [i for i in range(1, 67) if not(f(i, 2)) and f(i, 4)])
