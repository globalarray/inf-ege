from itertools import product

variants = product(['A', 'B', 'C', 'D', 'X', 'Y', 'Z'], repeat=4)

r = 0

for v in variants:
    suitable = True
    for idx, cr in enumerate(v):
        if idx < 2:
            if not(cr in "XYZ"):
                suitable = False
                break
        else:
            if not(cr in "ABCD"):
                suitable = False
                break
    if suitable:
        r += 1

print(r)

#https://inf-ege.sdamgia.ru/problem?id=14269
