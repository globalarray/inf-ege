f = list(map(int, open("17_19749.txt", 'r').readlines()))

f2 = f.copy()

f2.sort()

y = f2[0] % 3
z = f2[-1] % 7

cnt = 0
maxSum = -10**10

for i in range(len(f)-2):
    nums = [f[i], f[i+1], f[i+2]]

    if len(list(filter(lambda x: x % 3 == y, nums))) == 1:
        if len(list(filter(lambda x: x % 7 == z, nums))) >= 2:
            cnt += 1
            maxSum = max(maxSum, sum(nums))
print(cnt, maxSum)
