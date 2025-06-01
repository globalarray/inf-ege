letters = "qwertyuiopasdfghjklzxcvbnm"

sortd = []

for c in letters:
    sortd.append([int(c, 36), c])
sortd.sort()

sortd = [y for x,y in sortd]

def to19(n):
    r = ""

    lowerZero = n < 0

    n = abs(n)

    while n > 0:
        v = n % 19

        if v > 9:
            v = sortd[v - 10]
        r += str(v)

        n //= 19
    r = r[::-1]

    if lowerZero:
        r = "-" + r
    return r

for x in range(19):
    s = int("98" + to19(x) + "79641", 19) + int("36" + to19(x) + "14", 19) + int("73" + to19(x) + "4", 19)

    if s % 18 == 0:
        print(s // 18)
