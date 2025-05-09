f = list(map(int, open("17_18582.txt", 'r').readlines()))

minElement = str(min(f))[-1]

cnt = 0
maxSum = 0

for i in range(len(f)-2):
    nums = [f[i], f[i+1], f[i+2]]

    lowerZeroNums = list(filter(lambda x: x < 0, nums))

    if len(lowerZeroNums) > len(nums) - len(lowerZeroNums):
        s = sum(nums)
        if str(s)[-1] == minElement:
            cnt += 1
            maxSum = max(abs(s), maxSum)
print(cnt, maxSum)
