f = open("09.txt", 'r').readlines()

cnt = 0

for l in f:
    nums = list(map(int, l.split()))

    chetNums = list(filter(lambda x: x % 2 == 0, nums))

    if len(set(nums)) == len(nums) and len(chetNums) > (len(nums) - len(chetNums)):
        if sum(chetNums) < sum(list(filter(lambda x: x % 2 != 0, nums))):
            cnt += 1
print(cnt)
