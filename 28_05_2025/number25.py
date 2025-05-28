from math import sqrt

def divs(n):
    r = []

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            r.append(i)
            r.append(n // i)
    return r

def f(n):
    return sum(list(filter(lambda x: len(divs(x)) == 0, divs(n))))

start = 32_500_000
k = 0

while True:
    v = f(start)

    if v != 0 and v % 145 == 0:
        print(start, v)
        k += 1

        if k == 7:
            break
    start += 1
