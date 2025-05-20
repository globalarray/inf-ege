def to3(n):
    r = ""

    lowerZero = n < 0

    n = abs(n)

    while n > 0:
        r += str(n % 3)
        n //= 3
    r = r[::-1]

    if lowerZero:
        return "-" + r
    return r

def f(n):
    z = to3(n)

    if n % 3 == 0:
        z += z[-2] + z[-1]
    else:
        z += to3((n % 3) * 5)
    return int(z, 3)

minR = 10**10

for i in range(1, 1000):
    v = f(i)

    if v > 133:
        minR = min(v, minR)
print(minR)
