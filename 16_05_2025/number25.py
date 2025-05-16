from math import sqrt

def s(n):
    divs = []

    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            divs.append(i)
            divs.append(n // i)

    sm = [x for x in divs if x % 2 == 0]

    if len(sm) == 0:
        return 0

    return sum(sm)

for i in range(1204300, 1204381):
    v = s(i)

    if v != 0 and v % 10 == 0:
        print(i, v)
