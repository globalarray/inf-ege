from itertools import permutations

a = '457 46 567 12 136 235 13'.split()
s = 'FE EC CA AB BD DG GC GF FD'.split()

v = "ABCDEFG"

print(" ".join(str(i) for i in range(1, len(v)+1)))

for p in permutations(v):
    if all([str(p.index(x) + 1) in a[p.index(y)] for x, y in s]):
        print(*p)
        break
