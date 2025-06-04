from itertools import permutations

mutations = permutations("001111122")

for n in range(4, 1000):
    s = ">" + (25 * "0") + ("1" * n) + (25 * "2")

    while (">1" in s) or (">2" in s) or (">0" in s):
        s = s.replace(">1", "22>", 1)
        s = s.replace(">2", "2>", 1)
        s = s.replace(">0", "1>", 1)
    sm = sum(map(int, list(s.replace(">", ""))))

    if sm % 15 == 0 and sm > 999:
        print(n)
        break
