f = list(map(int, open("17 (5).txt", 'r').readlines()))

maxSuitableElement = max([n for n in f if (str(n)[-2] + str(n)[-1]) == '23'])

cnt = 0
xm = 0

for i in range(len(f)-2):
    nums = [f[i], f[i+1], f[i+2]]

    if len([n for n in nums if n < 0]) == 1:
        nums.sort()

        s = nums[-2] + nums[-1]

        if s > maxSuitableElement:
            cnt += 1
            xm = max(xm, s)
print(cnt, xm)
