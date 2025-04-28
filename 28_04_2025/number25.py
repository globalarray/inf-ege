def divs(n):
    r = []

    for i in range(2, int((n ** 0.5)) + 1):
        if n % i == 0:
            r.append(n // i)
            r.append(i)

    return sum(r)

start = 500_000
k = 0

while True:
    v = divs(start)

    if str(v)[-1] == '9':
        print([start, v])
        k += 1

    if k == 5:
        break

    start += 1
