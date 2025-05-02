from itertools import product

alphabet = "0123456789ABCDFE"

it = list(product(alphabet, repeat=4))

it2 = list(product(alphabet, repeat=2))

cnt = 0

for i in it:
    if i[0] == '0':
        continue
    for i2 in it2:
        v16 = "".join(i) + "a" + "".join(i2)
        v8 = oct(int(v16, 16))[2:]

        if len(v8) == 9 and v8[4] == '2' and v8[-1] == '3':
            cnt += 1
print(cnt)
