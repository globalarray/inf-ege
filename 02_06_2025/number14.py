letters = "qwertyuiopasdfghjklzxcvbnm"

srtd = []

for c in letters:
    srtd.append([int(c, 36), c])

srtd.sort()

srtd = [y for x,y in srtd]

def to29(n):
    r = ""

    lowerZero = n < 0

    n = abs(n)

    while n > 0:
        v = n % 29

        if v > 9:
            v = srtd[v - 10]
        r += str(v)

        n //= 29
    r = r[::-1]

    if lowerZero:
        r = "-" + r
    return r

for x in range(29):
    z = int("47" + to29(x) + "42696", 29) + int("8" + to29(x) + "22", 29)

    if z % 28 == 0:
        print(z//28)
