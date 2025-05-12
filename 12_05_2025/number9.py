f = map(lambda l: list(map(int, l.split())), open("9_22222.txt", 'r').readlines())

cnt = 0

for nums in f:
    if len(nums)-1 == len(set(nums)):
        povtNum = list(set(filter(lambda x: nums.count(x) > 1, nums)))[0]

        if max(nums) == povtNum:
            continue

        notPovtNums = list(filter(lambda x: x != povtNum, nums))

        notPovtNums.sort()

        if (povtNum ** 2) >= (notPovtNums[0] ** 2) + (notPovtNums[1] ** 2):
            cnt += 1
print(cnt)
