f = list(map(int, open("17.txt", 'r').readlines()))

suitableSummary = 0
cnt = 0
maxSum = -10**6

for n in f:
    if n < 0:
        suitableSummary += n

for i in range(len(f)-2):
    nums = [f[i], f[i+1], f[i+2]]

    if (min(nums) * max(nums)) > suitableSummary:
        cnt += 1
        maxSum = max(sum(nums), maxSum)
print(cnt, maxSum)
