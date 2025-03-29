def convert(v, base):
    r = 0

    for idx, c in enumerate(v[::-1]):
        r += int(c) * (base ** idx)
    return r

for a in range(1000):
    for x in range(9):
        if (convert("842" + str(x) + "5", 9) + a) % convert("8" + str(x) + "725", 9) == 0:
            print(a)
