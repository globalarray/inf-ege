f = list(map(int, open("1102_17.txt", "r").readlines()))

maxElement = 0
minElement = 10**10

maxSum = -10**7

r = 0

for l in f:
    maxElement = max(maxElement, l)
    minElement = min(minElement, l)

for idx, n in enumerate(f):
    if idx == len(f) -1:
        break
    nums = [n, f[idx+1]]

    suitable1 = False
    suitable2 = False

    for num in nums:
        if num % 3 == maxElement % 3:
            suitable1 = True
        if num % 7 == minElement % 7:
            suitable2 = True
    if suitable1 and suitable2:
        r += 1
        maxSum = max(sum(nums), maxSum)
print(r, maxSum)
