from math import ceil

for i in range(1, 512):
    k = ceil((119 * i)/8)

    if k * 125_300 >= 23 * 1024 * 1024:
        break
print((2**(i-1))+1)
