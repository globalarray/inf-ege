f = map(lambda l: list(map(int, l.split(';'))), open("9_7335.csv", 'r'))

cnt = 0

for nums in f:
    suit = False

    if len(nums) == len(set(nums)):
        if int((max(nums) + min(nums)) / 2) in nums:
            suit = True
    else:
        povtNums = list(filter(lambda x: nums.count(x) > 1, nums))
        notPovtNums = list(filter(lambda x: x not in povtNums, nums))

        if sum(map(lambda x: x ** 2, povtNums)) < sum(map(lambda x: x ** 2, notPovtNums)):
            suit = not suit
    if suit:
        cnt += 1
print(cnt)
