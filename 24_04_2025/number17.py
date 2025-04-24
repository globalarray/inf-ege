f = list(map(int, open("17_21595.txt", 'r')))

def suitable(n):
    return len(str(n).replace("-", "", -1)) == 4 and str(n)[-1] == '3'

maxSuitableLen = len([n for n in f if suitable(n) == True])

maxSum = 0
cnt = 0

for i in range(len(f)-2):
    nums = [f[i], f[i+1], f[i+2]]

    nums.sort()

    s = nums[-1] + nums[-2]

    if s > (maxSuitableLen ** 2):
        cnt += 1
        maxSum = max(maxSum, abs(sum(nums)))
print(cnt, maxSum)
