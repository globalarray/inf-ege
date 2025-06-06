from itertools import permutations

m = 0

for cmb in permutations("345"):
    s = 30 * "".join(cmb)
    while ("43" in s) or ("53" in s):
        if "43" in s:
            s = s.replace("43", "33", 1)
        else:
            s = s.replace("53", "433", 1)
    m = max(m, s.count('3'))
print(m)
