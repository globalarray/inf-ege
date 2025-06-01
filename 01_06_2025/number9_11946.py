f = list(map(lambda l: list(map(int, l.split())), open("8t4LTdUdL.csv", "r")))

cnt = 0

for nums in f:
    povtNums = list(set(list(filter(lambda x: nums.count(x) > 1, nums))))
    notPovtNums = list(filter(lambda x: x not in povtNums, nums))

    if len(povtNums) == 1 and len(notPovtNums) == 4:
        suit = True
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                suit = False
                break
        if suit:
            cnt += 1
print(len(f) - cnt)
