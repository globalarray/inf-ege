f = map(lambda l: list(map(int, l.split(';'))), open("9_7030.csv", 'r').readlines())

cnt = 0

for nums in f:
    povtNums = list(set(filter(lambda x: nums.count(x) == 2, nums)))

    if len(povtNums) == 3:
        povtNums.sort()

        if (povtNums[0] ** 2) + (povtNums[1] ** 2) == povtNums[2] ** 2:
            cnt += 1
print(cnt)
