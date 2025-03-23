f = list(map(int, open("23_17.txt", 'r').readlines()))

p = list(filter(lambda x: x % 2 != 0, f))

srNum = sum(p) / len(p)

maxSum = 0
cnt = 0

for i in range(len(f)-1):
    if (f[i] % 5 == 0) or (f[i+1] % 5 == 0):
        if (f[i] < srNum) or (f[i+1] < srNum):
            cnt += 1
            maxSum = max(maxSum, f[i] + f[i+1])
print(cnt, maxSum)
