from itertools import product, permutations


def f(x, y, z, w):
    return ((x and (not y)) or (w <= z)) == (z == x)

for x1, x2, x3 in product([0,1], repeat=3):
    t = (
        (x1, 0, 0, 1, 1),
        (0, 1, 0, 0, 1),
        (0, x2, x3, 1, 1)
    )

    if len(t) == len(set(t)):
        for p in permutations("xyzw"):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(p)
