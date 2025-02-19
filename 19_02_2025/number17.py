f = open("17_2024.txt", 'r').readlines()

maxN = 0

r = 0
maxSum = 0

for l in f:
    if str(int(l))[-2:] == "13":
        maxN = max(maxN, int(l))
for idx, l in enumerate(f):
    if len(f)-1 < idx + 2:
        break

    nums = list(map(int, [l, f[idx+1], f[idx+2]]))

    suitableA = len(list(filter(lambda x: len(str(x)) == 3, nums))) == 2

    s = sum(nums)

    if suitableA and s <= maxN:
        r += 1
        maxSum = max(maxSum, s)
print(r, maxSum)
