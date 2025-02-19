res = 0

for a in range(100):
    b = False
    for x in range(100):
        for y in range(100):
            if not((y + 2 * x != 48) or (a < x) or (a < y)):
                b = True
    if b is False:
        res = max(res, a)
print(res)
