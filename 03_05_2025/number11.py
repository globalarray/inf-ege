from math import log2,ceil

r = 0

for x in range(1, 1000):
    m = 10+52+x

    i = ceil(log2(m))

    if ceil(53*i/8) * 2000 <= 93 * 1024:
        r = max(r,x)
    else:
        break
print(r)
