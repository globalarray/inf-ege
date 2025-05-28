from itertools import product

r = 0

for item in product("0123456789AB", repeat=5):
    if item[0] == '0':
        continue
    suit = 0

    for i in range(1, len(item)):
        n = int(item[i], 12)
        if int(item[i-1], 12) % 2 == n % 2 and n % 2 != 0:
            suit += 1

            if suit > 2:
                break
    if suit <= 2:
        r += 1
print(r)
