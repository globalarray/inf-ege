def f(n):
    z = bin(n)[2:]

    s = sum(map(int, list(z)))

    if s % 4 == 0:
        z = "10" + z
    else:
        z = "11" + z
    if int(z) % 2 != 0:
        z += "0"
    else:
        z += "1"
    return int(z, 2)

v = []

for i in range(1, 1000):
    r = f(i)

    if r <= 250:
        v.append(i)
print(max(v))
