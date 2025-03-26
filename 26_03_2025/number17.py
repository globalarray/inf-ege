f = list(map(int, open("26_03_17.txt", 'r').readlines()))

cnt = 0
maxSum = 0

for i in range(len(f)-1):
    for j in range(i+1, len(f)):
        if (f[i] % 160) != (f[j] % 160):
            if (f[i] % 7 == 0) or (f[j] % 7 == 0):
                cnt += 1
                maxSum = max(f[i]+f[j], maxSum)
print(cnt, maxSum)
