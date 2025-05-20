from math import sqrt

def divs(n):
    r = []

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            r.append(i)
            r.append(n // i)
    r.sort()

    return r

def m(n):
    d = list(filter(lambda x: len(divs(x)) == 0, divs(n)))

    if len(d) < 2:
        return 0

    return d[0] + d[-1]

start = 23_600_001
k = 0

while True:
    md = m(start)

    if md % 213 == 171:
        print(start, md)

        k += 1

        if k == 6: break

    start += 1
