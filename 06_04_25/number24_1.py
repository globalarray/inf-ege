f = open("inf_26_04_21_24.txt", 'r').readlines()

maxLen = 0

for line in f:
    if line.count('G') < 25:
        for c in line:
            if line.count(c) < 2:
                continue
            maxLen = max(maxLen, line.rindex(c) - line.index(c))
print(maxLen)
