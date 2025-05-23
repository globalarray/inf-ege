def f(n):
    A = a1 <= n <= a2

    M = 32 <= n <= 68
    N = 54 <= n <= 76

    return not(M or N) == (not A)

d = [y for x in [32, 68, 54, 76] for y in [x, x-1, x+1]]

r = []

for a1 in d:
    for a2 in d:
        if a2 >= a1 and all(f(x) for x in d):
            r += [a2 - a1]
print(min(r))
