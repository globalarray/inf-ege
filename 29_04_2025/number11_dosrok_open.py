from math import ceil

for i in range(1, 512 + 1):
    s = round((246*i)/8)

    if s * 703569 <= 77 * 1024 * 1024:
        print(i)
#2**3
