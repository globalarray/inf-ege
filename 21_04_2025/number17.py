f = list(map(int, open("17_21712.txt", 'r').readlines()))

def isSuitable(n):
    return len(str(n).replace('-', '', 1)) == 4 and str(n)[-1] == '6'

minSuitableNum = 10**10

for n in f:
    if isSuitable(n) and n > 0:
        minSuitableNum = min(minSuitableNum, n)

cnt = 0
maxSum = 0

for i in range(len(f)-2):
    nums = [f[i], f[i+1], f[i+2]]

    s = sum(nums)

    if len(list(filter(isSuitable, nums))) == 1 and (s <= minSuitableNum):
        cnt += 1
        maxSum = max(maxSum, s)
print(cnt, maxSum)
