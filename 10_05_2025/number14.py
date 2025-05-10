digits = "qwertyuiopasdfghjklzxcvbnm"

digs = []

for c in digits:
    digs.append([int(c, 36), c])
alph = "".join([y for x, y in sorted(digs, key=lambda item: item[0])])

def to35(n):
    if n == 0: return "0"

    r = ""

    lowerZero = n < 0

    n = abs(n)

    while n > 0:
        v = n % 35

        if v > 10:
            v = alph[v - 10]
        r += str(v)

        n //= 35
    r = r[::-1]

    if lowerZero:
        r = "-" + r
    return r



for x in range(36):
    z = int("6" + to35(x) + "qr" + to35(x), 35) + int(to35(x) + "59sh", 35) + int("ph" + to35(x) + "69yw", 35)

    zStr = str(z)

    numCnts = [[zStr.count(a), a] for a in zStr]

    nums = [int(y) for x, y in numCnts if x == max(numCnts)[0]]

    y = max(nums) ** 2
    if z % y == 0:
        print(z // y)
