f = open("inf_26_04_21_24.txt", 'r').readlines()

maxLen = 0
tempLen = 0

for line in f:
    if line.count('A') < 25:
        for i in range(len(line)):
            if line.count(line[i]) > 1:
                maxLen = max(maxLen, line.rindex(line[i]) - line.index(line[i]))
print(maxLen)
