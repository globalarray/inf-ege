from itertools import product

items = product("0123456789", repeat=4)

cnt = 0

for it in items:
    if it[0] == '0':
        continue

    if len(it) == len(set(it)):
        suit = True
        for i in range(len(it)-1):
            if int(it[i]) % 2 == int(it[i+1]) % 2:
                suit = False
                break
        if suit:
            cnt += 1
print(cnt)
