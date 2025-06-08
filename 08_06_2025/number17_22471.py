f = list(map(int, open("17_22471.txt", 'r').readlines()))

minSuitableElement = min([x for x in f if x > 0 and len(str(abs(x))) == 3])

cnt = 0
maxSum = -float("inf")

for i in range(len(f)-2):
    nums = [f[i], f[i+1], f[i+2]]

    otrNum = len(list(filter(lambda x: x < 0, nums)))

    if len(nums) - otrNum > otrNum:
        if max(nums) + min(nums) > minSuitableElement:
            cnt += 1
            maxSum = max(maxSum, sum(nums))
print(cnt, maxSum)
