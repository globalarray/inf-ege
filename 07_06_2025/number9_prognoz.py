f = map(lambda l: list(map(int, l.split())), open("09_07.txt", 'r'))

sm = 0
cnt = 0

for nums in f:
    povtNums = list(set(filter(lambda x: nums.count(x) > 1, nums)))
    notPovtNums = list(filter(lambda x: x not in povtNums, nums))

    if len(povtNums) == 1 and len(set(nums)) == len(nums) - 2:
        if povtNums[0] < (2 * min(notPovtNums)):
            sm += sum(nums)
            cnt += 1
print(sm/(cnt * 6))
