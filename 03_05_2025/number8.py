from itertools import product

items = product("DIKMO", repeat=5)

m = 0

for idx, it in enumerate(items):
    if it.count('M') == 2 and "".join(it).count("MM") == 0:
        m = max(m, idx + 1)
print(m)
