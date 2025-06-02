f = list(map(int, open("Dm0oNnyHF.txt", 'r').readlines()))

maxSuitableElement = max([x for x in f if len(str(x)) > 2 and (str(x)[-2] + str(x)[-1]) == '54'])

cnt = 0
maxNum = 0

for i in range(len(f)-1):
    nums = [f[i], f[i+1]]

    if str(nums[0])[-1] == str(nums[1])[-1]:
        s = sum(map(abs, nums))

        if s <= maxSuitableElement:
            cnt += 1
            maxNum = max(maxNum, nums[0], nums[1])
print(cnt, maxNum)
