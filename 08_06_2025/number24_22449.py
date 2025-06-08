from string import printable

t = "*" + printable[36:62]

f = open("24_22449.txt", 'r').readline()

a = [t.index(s) for s in f]

maxT = 0

lm = l = 0
sm = 0

for r in range(len(f)):
    sm += a[r]

    while r - l + 1 > 500_000:
        sm -= a[l]
        l += 1
    maxT = max(sm, maxT)

    if sm == 6761939:
        print(l, r)
print(maxT)
