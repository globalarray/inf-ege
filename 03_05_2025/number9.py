from math import prod

f = map(lambda l: list(map(int, l.split())), open("9_18134.txt", 'r').readlines())

cnt = 0

for nums in f:
    povtNums = list(set(list(filter(lambda x: nums.count(x) == 2, nums))))

    if len(povtNums) == 2:
        if (max(povtNums) ** 2) > prod(list(filter(lambda x: x not in povtNums, nums))):
            cnt += 1
print(cnt)
