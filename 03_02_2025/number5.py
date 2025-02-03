def f(n):
    sums = []

    for idx, k in enumerate(str(n)):
        if idx == len(str(n))-1:
            break
        sums.append(int(k) + int(str(n)[idx+1]))
    sums.sort()

    return int("".join(map(str, sums[-2:])))

res = 0

for j in range(10**3, 10**4):
    if f(j) == 1517:
        res = max(res, j)
print(res)
#https://inf-ege.sdamgia.ru/problem?id=10380
