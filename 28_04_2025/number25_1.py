def divs(n):
    r = []

    for i in range(2, int((n ** 0.5)) + 1):
        if n % i == 0:
            r.append(i)
            r.append(n // i)
    return r

def get_m(n):
    r = divs(n)

    if len(r) < 2:
        return 0

    d = [v for v in r if len(divs(v)) == 0]

    if len(d) < 2:
        return 0

    return max(d) + min(d)

start = 1_200_000
k = 0

while True:
    m = get_m(start)

    if m > 2000 and str(m)[-1] == '8':
        print([start, m])
        k += 1

    if k == 5:
        break
    start += 1
