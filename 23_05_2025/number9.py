f = map(lambda l: list(map(int, l.split())), open("9_19481.csv", 'r'))

result = 0

for idx, nums in enumerate(f):
    if len(nums) == len(set(nums)):
        nums.sort()

        if ((nums[0] + nums[-1]) ** 2) > sum(map(lambda n: n ** 3, nums[1:len(nums)-1])):
            result += (idx + 1)
print(result)
