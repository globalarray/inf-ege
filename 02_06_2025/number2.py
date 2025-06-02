from itertools import product, permutations


def f(x,y,z,w):
    return (w or x or y) <= ((y or z) and x or y and (w or z))

for x1,x2,x3,x4,x5 in product([0,1], repeat=5):
    t = (
        (0, 0, 0, x1, 0),
        (x2, 1, 1, x3, 0),
        (x4, 1, x5, 1, 0)
    )

    for p in permutations("xyzw"):
        if all(f(**dict(zip(p, line))) == line[-1] for line in t):
            print(*p)
            break
