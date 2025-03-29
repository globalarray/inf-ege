f = list(map(int, open("17.txt", 'r').readlines()))

maxEl = 0
cnt = 0
maxSum = 0

for n in f:
    nStr = str(n)
    if len(nStr) > 3 and nStr[len(nStr)-3:len(nStr)] == "321":
        maxEl = max(maxEl, n)

for i in range(len(f)-2):
    nums = [f[i], f[i+1], f[i+2]]

    if len(list(filter(lambda x: len(str(x)) == 5, nums))) == 2:
        if (nums[0] % 5 == 0) or (nums[1] % 5 == 0) or (nums[2] % 5 == 0):
            s = sum(nums)
            if s > maxEl:
                cnt += 1
                maxSum = max(maxSum, s)
print(cnt, maxSum)
