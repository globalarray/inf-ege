def to4(n):
    z = ""

    lessZero = n < 0

    if lessZero:
        n = abs(n)

    while n > 0:
        z += str(n % 4)
        n //= 4
    if lessZero:
        return "-" + z[::-1]
    return z[::-1]

r = dict()

for x in range(1, 10000000):
    v = to4((4**8)+(4**5)-x)

    if v.count('0') == 8:
        r[x] = len(v.replace("-", "", -1))
print([x for x, y in r.items() if y == min(r.values())])
