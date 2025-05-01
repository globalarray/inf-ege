def r(n):
    divs = []

    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            divs.append(i)
            divs.append(n // i)
    return sum(divs)

start = 500_000

k = 0

while True:
    v = r(start)

    if str(v)[-1] == '6':
        print([start, v])
        k += 1
    if k == 5:
        break
    start += 1
