f = map(lambda l: list(map(int, l.split())), open("9_21895.txt", 'r').readlines())

cnt = 0

for nums in f:
    if len(nums) == len(set(nums)):
        nums.sort()

        if (nums[-1] + nums[-2]) <= sum(nums[:len(nums)-2]):
            cnt += 1
print(cnt)
