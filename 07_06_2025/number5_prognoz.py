def to3(n):
    r = ""

    lowerZero = n < 0

    n = abs(n)

    while n > 0:
        r += str(n % 3)
        n //= 3
    r = r[::-1]

    if lowerZero:
        r = "-" + r
    return r

def f(n):
    z = to3(n)

    if n % 3 == 0:
        z += z[-2:]
    else:
        z += to3((n % 3) * 5)
    return int(z, 3)
for n in range(1, 1000):
    if f(n) >= 290:
        print(n)
        break
