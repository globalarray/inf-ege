def to4(n):
    r = ""

    while n > 0:
        r += str((n % 4))

        n //= 4
    return r[::-1]

r = []

for x in range(1, 3001):
    s = to4((4**210)+(4**110)-x)

    r.append([s.count('0'), x])

for x, y in r:
    if x == 105:
        print(y)
