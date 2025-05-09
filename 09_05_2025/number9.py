f = map(lambda l: list(map(int, l.split())), open("9_17770.txt", 'r'))

cnt = 0

for nums in f:
    nums.sort()

    s = nums[-1] + nums[-2]

    suitNums = list(filter(lambda x: str(x)[-1] == '5', nums))

    if (((nums[-1] + nums[-2]) * 2) > ((sum(nums) - s) * 3)) and len(suitNums) >= 2:
        cnt += 1
print(cnt)
