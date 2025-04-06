f = list(map(int, open("17.txt", 'r').readlines()))

cnt = 0
maxSum = 0

for i in range(len(f)-1):
    s = f[i] + f[i+1]
    if ((f[i] % 3 == 0) or (f[i+1] % 3 == 0)) and (s % 5 == 0):
        cnt += 1
        maxSum = max(maxSum, s)
print(cnt, maxSum)
