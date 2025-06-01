def to5(n):
    r = ""

    lowerZero = n < 0

    n = abs(n)

    while n > 0:
        r += str(n % 5)
        n //= 5
    r = r[::-1]

    if lowerZero:
        r = "-" + r
    return r

def f(n):
    z = to5(n)

    if int(z[-1]) % 2 == 0:
        z += "2"
    else:
        z = "2" + z + "3"
    return int(z, 5)

n = []

for i in range(1, 10000):
    v = f(i)

    if v < 1000:
        n.append(i)
print(max(n))
