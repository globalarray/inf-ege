f = map(lambda l: l.split(), open("21_9.txt", 'r').readlines())

cnt = 0

for l in f:
    nums = list(map(int, l))

    if len(nums) - 3 == len(set(nums)):
        repeatedNum = (-sum(set(nums)) + sum(nums)) / 3

        notRepeatedNums = list(filter(lambda v: v != repeatedNum, nums))

        if sum(notRepeatedNums) / len(notRepeatedNums) > 4*repeatedNum:
            cnt += 1
print(cnt)
