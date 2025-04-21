def to3(n):
    r = ""

    while n > 0:
        r += str(n % 3)
        n //= 3
    return r[::-1]

def f(n):
    trVal = to3(n)

    if n % 3 == 0:
        trVal += trVal[-2] + trVal[-1]
    else:
        trVal += to3((n % 3) * 3)

    return int(trVal, 3)

r = 0

for i in range(1, 1000):
    v = f(i)
    if v < 151:
        r = i
print(r)
