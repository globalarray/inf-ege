def to4(n):
    r = ""

    while n > 0:
        r += str(n % 4)
        n //= 4
    return r[::-1]

def f(n):
    z = list(to4(n))

    if sum(map(int, z)) % 3 == 0:
        for idx, c in enumerate(z):
            if c == '0':
                z[idx] = '2'
            elif c == '2':
                z[idx] = '0'
        z = list("32" + "".join(z))
    else:
        z = list("".join(z) + "33")

        z[1] = '1'
        z[2] = '0'
    return int("".join(z), 4)

r = []

for i in range(1, 10000):
    v = f(i)
    if v > 320:
        r.append([v, i])
print([i for v, i in r if v == min(r)[0]])
