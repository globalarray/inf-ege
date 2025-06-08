f = map(lambda l: list(map(int, l.split())), open("09_08.txt", 'r'))

num = 0

for idx, nums in enumerate(f):
    povtNums = list(set(filter(lambda x: nums.count(x) > 1, nums)))

    if len(povtNums) == 2 and len(nums) - 4 == len(set(nums)) and len([x for x in povtNums if nums.count(x) == 3]) == 2:
        notPovtNums = list(filter(lambda x: x not in povtNums, nums))

        if (sum(notPovtNums) ** 3) > (sum([n ** 2 for n in povtNums]) * 3):
            num = idx + 1
            break
print(num)
