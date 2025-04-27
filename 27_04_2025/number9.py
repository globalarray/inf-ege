f = map(lambda l: list(map(int, l.split())), open("9_21592.txt", 'r').readlines())

r = 0

for idx, nums in enumerate(f):
    povtNums = list(set(list(filter(lambda x: nums.count(x) == 2, nums))))

    if len(povtNums) == 3 and len(nums) - 3 == len(set(nums)):
        notPovtNums = list(filter(lambda x: x not in povtNums, nums))

        if ((max(povtNums) - min(povtNums)) ** 2) > 2 * sum(map(lambda x: x ** 2, notPovtNums)):
            r = max(r, idx + 1)
print(r)
