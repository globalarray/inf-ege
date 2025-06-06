f = list(map(int, open("17_8161.txt", 'r').readlines()))

maxSuitableElement = max([i for i in f if len(str(abs(i))) == 3])

cnt = 0
maxSum = -float("inf")

for i in range(len(f)-1):
    nums = [f[i], f[i+1]]

    tr = list(filter(lambda x: len(str(abs(x))) == 3, nums))

    s = sum(nums)

    if len(tr) == 1 and s <= maxSuitableElement:
        cnt += 1
        maxSum = max(maxSum, s)
print(cnt, maxSum)
