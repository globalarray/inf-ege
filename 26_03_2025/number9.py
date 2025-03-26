f = map(lambda l: list(map(int, l.split())), open("26_03_09.txt", 'r').readlines())

cnt = 0

for nums in f:
    maxNum = max(nums)

    if nums.count(maxNum) != 1:
        continue
    if len(nums) != len(set(nums)):
        if maxNum / ((sum(nums) - maxNum) / (len(nums) - 1)) > 3:
            cnt += 1
print(cnt)
