#граница для M

mLimit = 0

while True:
    if 2**mLimit <= 600_000_000:
        mLimit += 1
    else:
        break

nLimit = 0

while True:
    if 3**nLimit <= 600_000_000:
        nLimit += 1
    else:
        break

for m in range(2, mLimit, 2):
    for n in range(1, nLimit, 2):
        v = (2**m) * (3**n)
        if 400_000_000 <= v <= 600_000_000:
            print(v)
