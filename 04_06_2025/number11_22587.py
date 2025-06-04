from math import ceil

for i in range(1, 30000):
    pwd = ceil((7 * 25) / 8)
    if (pwd + 30) * i > 1 * 1024 * 1024:
        break
print(i-1)
