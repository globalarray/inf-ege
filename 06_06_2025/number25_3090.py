from functools import lru_cache
from math import sqrt

@lru_cache(None)
def is_simple(n):
    if n < 2 or (n % 2 == 0 and n != 2):
        return False

    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def divs(n):
    simpleDel = []
    chetDel = []

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            dels = [i, n // i]

            if dels[0] == dels[1]:
                dels = dels[1:]

            for d in dels:
                if d % 2 == 0:
                    chetDel.append(d)
                    continue
                if is_simple(d):
                    simpleDel.append(d)
    return chetDel, simpleDel


def m(n):
    d = divs(n)

    if len(d[0]) != len(d[1]):
        return -1

    return abs(sum(d[1]) - sum(d[0]))

start = 100_000_000
k = 0

while True:
    mn = m(start)

    if mn != -1:
        print(start, mn)
        k += 1

        if k==5: break
    start += 1
