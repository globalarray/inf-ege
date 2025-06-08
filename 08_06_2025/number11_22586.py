from math import ceil

for x in range(1, 1000):
    per_one = ceil((9 * x)/8)

    if 2500 * per_one > 61 * 1024:
        break
print(x)
