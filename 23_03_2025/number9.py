f = map(lambda arr: list(map(int, arr)), map(lambda l: l.split(), open("23_9.txt", 'r').readlines()))

cnt = 0

for nums in f:
    if len(set(nums)) == len(nums) - 3:
        povtNum = int((sum(nums) - sum(set(nums))) / 3)

        if nums.count(povtNum) != 4:
            continue

        if povtNum < (sum(nums) / len(nums)):
            cnt += 1
print(cnt)
