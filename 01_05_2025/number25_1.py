from fnmatch import fnmatch

d = int("16", 31)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to31(n):
    r = ""

    while n > 0:
        v = n % 31

        if v > 9:
            r += alphabet[v - 10]
        else:
            r += str(v)

        n //= 31
    return r[::-1]

k = 0

for i in range(9760*(10**6), 9761*(10**6)):
    if fnmatch(to31(i), "AUT?MN*"):
        if i % d == 0:
            print([i, i // d])
            k += 1

            if k == 5:
                break
