results = []

mLimit = 0
nLimit = 0

#поиск границы для M

while 2 ** mLimit < 400_000_000:
    mLimit += 1

#соответственно N

while 3 ** nLimit < 400_000_000:
    nLimit += 1

for m in range(2, mLimit, 2):
    for n in range(1, nLimit, 2):
        mult = (2**m) * (3**n)
        if 200_000_000 <= mult <= 400_000_000:
            results.append(mult)
results.sort()

print(results)
