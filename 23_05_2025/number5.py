def to5(n):
    r = ""

    while n > 0:
        r += str(n % 5)
        n //= 5
    return r[::-1]

def f(n):
    z = to5(n)

    s = sum(map(int, list(z)))

    if s % 5 == 0:
        z = z.replace("0", "*").replace("1", "0").replace("*", "1") + "14"
    else:
        z = "44" + z[2:] + "33"
    return int(z, 5)

r = {}

minV = 10**10

for i in range(1, 1000):
    v = f(i)

    if v > 370:
        minV = min(v, minV)
        r[i] = v
print([(x, y) for x, y in r.items() if y == minV])
