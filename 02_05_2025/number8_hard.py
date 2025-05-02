from itertools import product

items = product("0123456789AB", repeat=5)

suitable = "13579B"

result = 0

for it in items:
    cnt = 0

    if it[0] == '0':
        continue

    for i in range(len(it)-1):
        if (it[i] in suitable) and (it[i+1] in suitable):
            cnt += 1
    if cnt <= 2:
        result += 1
print(result)
