from itertools import product, permutations

def f(x,y,z,w):
    return x and (z <= w) and not y

for x1,x2,x3,x4,x5,x6,x7 in product([0,1], repeat=7):
    t = (
        (x1, x2, 1, x3, 1),
        (x4, 1, 0, x5, 1),
        (1, 0, x6, x7, 1),
    )

    if len(t) != len(set(t)):
        continue

    for p in permutations("xyzw"):
        if all(f(**dict(zip(p, line))) == line[-1] for line in t):
            print(*p)
            break
