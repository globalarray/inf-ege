from math import sqrt

def divs(n):
    r = []

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            r.append(i)
            r.append(n // i)
    r.sort()

    return r

def f(n):
    d = list(filter(lambda x: str(x)[len(str(x))-3:len(str(x))] == "777", divs(n)))

    d.sort()

    for g in d:
        if len(divs(g)) == 0:
            return g
    return -1

start = 55_000_000
k = 0

while True:
    v = f(start)

    if v != -1:
        print(start, v)

        k += 1

        if k == 5:
            break
    start += 1
