def divs(n):
    dels = []

    for i in range(2, round((n**0.5)) + 1):
        if n % i == 0:
            dels.append(i)
            dels.append(n // i)
    minSuitable = 10**10
    for d in dels:
        if str(d)[-1] == '7' and (d != 7 and d != n):
            minSuitable = min(minSuitable, d)
    if minSuitable == 10**10:
        return False
    return minSuitable

i = 600_000

k = 0

while True:
    v = divs(i)

    if v:
        print(i, v)
        k += 1
    if k == 5:
        break
    i += 1
