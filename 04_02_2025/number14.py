def convert(x, base):
    r = 0

    for idx, c in enumerate(str(x)[::-1]):
        r += int(c) * (base**idx)
    return r

for y in range(7):
    for x in range(7):
        s = convert("%d%d320" % (y, x), 7) + convert("1%d3%d3" % (x, y), 9)
        if s % 181 == 0:
            print(s // 181)
#https://inf-ege.sdamgia.ru/problem?id=48389
