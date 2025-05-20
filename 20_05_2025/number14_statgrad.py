digits = "qwertyuiopasdfghjklzxcvbnm,./+-)(*&^%"

def to40(n):
    if n == 0: return "0"

    r = ""

    lowerZero = n < 0

    n = abs(n)

    while n > 0:
        v = n % 40

        if v > 9:
            v = digits[v - 10]
        r += str(v)

        n //= 40
    r = r[::-1]

    if lowerZero:
        r = "-" + r
    return r

def from40(n):
    r = 0

    for idx, c in enumerate(str(n)[::-1]):
        if not c.isdigit():
            v = digits.index(c) + 10
        else:
            v = int(c)
        r += v * (40 ** idx)
    return r

for x in range(1, 40):
    val = from40("57" + to40(x) + "692" + to40(x) + "19")

    if val % 39 == 0:
        print(x * x)
