f = map(lambda l: list(map(int, l.split())), open("9_21592.txt").readlines())

num = 0

for idx, nums in enumerate(f):
    povtNums = list(set(filter(lambda x: nums.count(x) == 2, nums)))
    notPovtNums = list(set(filter(lambda x: x not in povtNums, nums)))

    if len(povtNums) == 3 and len(notPovtNums) == 2:
        if abs(max(povtNums) - min(povtNums)) ** 2 > 2 * sum(map(lambda x: x ** 2, notPovtNums)):
            num = idx + 1
print(num)
