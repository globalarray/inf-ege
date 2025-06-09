from math import ceil, log2

for x in range(1, 1000):
    per_one = ceil((ceil(log2(132))*18)/8) + x

    if per_one * 2000 > 100 * 1024:
        break
print(x-1)
