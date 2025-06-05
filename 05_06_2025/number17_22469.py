from math import prod

f = list(map(int, open("17_22469.txt", 'r').readlines()))

suitableSumChr = str(sum([i for i in f if i % 2 != 0 and len(str(abs(i))) == 5]))[-1]

cnt = 0
maxProd = 0

for i in range(len(f)-1):
    nums = [f[i], f[i+1]]

    if len([n for n in nums if str(n)[-1] == suitableSumChr]) == 1:
        cnt += 1
        maxProd = max(maxProd, prod(nums))
print(cnt, maxProd)
