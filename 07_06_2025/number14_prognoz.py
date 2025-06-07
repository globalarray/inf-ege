def to5(n):
    r = ""

    n = abs(n)

    while n > 0:
        r += str(n % 5)
        n //= 5
    return r[::-1]

for x in range(1, 1000):
    v = to5((5**2024)-(5**1005)+(25**650)+3*(5**9)-x)

    if v.count('4') == 300:
        print(x)
        break
