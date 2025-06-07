from math import isqrt

def is_simple(n):
    if n < 2:
        return False
    if n == 2: return True

    if n % 2 == 0: return False

    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def get_simple_divs(n):
    d = []

    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            divs = [i, n // i]

            if divs[0] == divs[1]:
                divs = divs[1:]
            for dl in divs:
                if is_simple(dl):
                    d.append(dl)
    return d

def m(n):
    dls = get_simple_divs(n)

    if len(dls) == 0:
        return 0

    return max(dls) + min(dls)

start = 1_101_001

k = 0

while k != 5:
    mn = m(start)

    if mn > 13000 and str(mn)[-2:] == '26':
        print(start, mn)
        k += 1
    start += 1
