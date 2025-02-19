m = "1?2157*4"

i = 0

while True:
    v = int(m.replace('?', '9', 1).replace('*', str(i), 1))
    if v > 10**10:
        break

    i += 1

res = []

for x in range(10):
    for y in range(-1, i):
        if y == -1:
            y = ""
        g = int(m.replace('?', str(x), 1).replace('*', str(y), 1))

        if g % 2024 == 0:
            res.append(g)
res.sort()

for r in res:
    print([r, r // 2024])
