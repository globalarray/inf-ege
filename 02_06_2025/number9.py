f = map(lambda l: list(map(int, l.split())), open("9_02.csv").readlines())

n = 0

for idx, nums in enumerate(f):
    povtNums = list(set(list(filter(lambda x: nums.count(x) > 1, nums))))
    notPovtNums = list(filter(lambda x: x not in povtNums, nums))

    if len(povtNums) == 1 and len(notPovtNums) == 4:
        if povtNums[0] > sum(nums)/len(nums):
            n = idx + 1
print(n)
