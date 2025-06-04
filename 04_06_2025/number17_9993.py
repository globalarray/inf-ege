import math

f = list(map(int, open("17_9993.txt", 'r').readlines()))

maxSuitableNum = max([n for n in f if len(str(n)) >= 2 and str(n)[-2] + str(n)[-1] == '17'])

maxProd = 0
cnt = 0

d = {}

def is_simple(n):
    if n < 1:
        return False

    n = abs(n)

    if n in d:
        return d[n]
    simple = True

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            simple = False
            break
    d[n] = simple

    return simple

for j in range(len(f)-1):
    nums = [f[j], f[j+1]]

    if sum(nums) % maxSuitableNum == 0 and len(list(filter(is_simple, nums))) == 1:
        cnt += 1
        maxProd = max(maxProd, math.prod(nums))
print(cnt, maxProd)
