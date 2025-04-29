def f(n):
    z = bin(n)[2:]

    s = sum(map(int, list(z)))

    z += str(s % 2)

    s += s % 2

    z += str(s % 2)

    return int(z, 2)

for n in range(1, 1000):
    if f(n) > 253:
        print(n)
        break
