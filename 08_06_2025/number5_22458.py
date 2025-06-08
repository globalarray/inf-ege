def to3(n):
    r = ""
    n = abs(n)

    while n > 0:
        r += str(n % 3)
        n //= 3
    return r[::-1]

def f(n):
    z = to3(n)

    if n % 5 == 0:
        z += z[-2:]
    else:
        z += to3((n % 5) * 2)
    return int(z, 3)

r = 0

for n in range(1, 10000):
    v = f(n)

    if v < 514:
        r = max(r, v)
print(r)
