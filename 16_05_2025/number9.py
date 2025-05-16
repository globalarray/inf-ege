f = map(lambda l: list(map(int, l.split())), open("9_18594.txt", 'r'))

cnt = 0

for nums in f:
    if len(nums) % 2 == 0:
        chNums = list(filter(lambda x: x % 2 == 0, nums))

        if len(chNums) == len(nums)/2:
            nums.sort()

            if (nums[0] ** 2) <= sum(nums[1:4]):
                cnt += 1
print(cnt)
