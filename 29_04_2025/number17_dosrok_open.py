f = list(map(int, open("17_21903.txt", 'r').readlines()))

minSuitableElement = float("inf")

minMult = float("inf")
cnt = 0

for n in f:
    nStr = str(n)
    if nStr[-2] + nStr[-1] == "15" and len(str(abs(n))) == 3:
        minSuitableElement = min(minSuitableElement, n)

for i in range(len(f)-2):
    nums = [f[i], f[i+1], f[i+2]]

    lenP = len(list(filter(lambda x: x >= 0, nums)))

    if not(lenP == 0 or lenP == len(nums)):
        continue
    mult = max(nums) * min(nums)

    if mult > (minSuitableElement ** 2):
        cnt += 1
        minMult = min(mult, minMult)
print(cnt, minMult)
