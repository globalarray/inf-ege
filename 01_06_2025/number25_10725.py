from fnmatch import fnmatch
from math import sqrt

def divs(n):
    r = []

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            r.append(i)
            r.append(n // i)
    r.sort()

    return r

start = 65_001
k = 0

while k != 7:
    if not fnmatch(str(start), "6*97*5?"):
        start += 1
        continue

    d = [x for x in divs(start) if x % 2 == 0]

    if len(d) >= 4:
        print(start, sum(d))
        k += 1
    start += 1
