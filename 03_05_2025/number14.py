letters = "0123456789abcdefghijklmno"

def to25(n):
    r = ""

    while n > 0:
        v = n % 25

        if v > 9:
            v = letters[v - 10]
        r += str(v)

        n //= 25
    return r[::-1]

def to10(v):
    r = 0

    for idx, c in enumerate(v[::-1]):
        v = c
        if not c.isdigit():
            v = letters.index(c)
        r += int(v) * (25 ** idx)
    return r

cnt = 0

b = set()

for x in range(1, 25):
    xStrVal = str(x)
    if x > 9:
        xStrVal = letters[x]
    z = to10("8af7" + xStrVal + "11") + to10(xStrVal + "da87")

    for y in range(1, 101):
        if z % y == 0:
            b.add(y)
print(len(b))
