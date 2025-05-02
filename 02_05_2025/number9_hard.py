f = map(lambda l: list(map(int, l.split())), open("9.22_20488.txt", 'r').readlines())

cnt = 0

for nums in f:
    if len(nums) != len(set(nums)) and nums.count(max(nums)) == 1:
        povtNums = list(filter(lambda x: nums.count(x) > 1, nums))
        notPovtNums = list(filter(lambda x: x not in povtNums, nums))

        if sum(notPovtNums) / sum(povtNums) >= 3:
            cnt += 1
print(cnt)
