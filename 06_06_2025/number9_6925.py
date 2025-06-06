f = map(lambda l: list(map(int, l.split())), open("9_6925.txt", 'r').readlines())

def checkNumsSr(nums):
    chetSr = 0

    chetNums = list(filter(lambda x: x % 2 == 0, nums))

    if len(chetNums) != 0:
        chetSr = sum(chetNums) / len(chetNums)

    notChetSr = 0

    if len(nums) - len(chetNums) != 0:
        notChetSr = (sum(nums) - sum(chetNums)) / (len(nums) - len(chetNums))

    return abs(chetSr - notChetSr) > 50

cnt = 0

for nums in f:
    povtNum = list(set(filter(lambda x: nums.count(x) > 1, nums)))

    suit1 = len(povtNum) == 1 and nums.count(povtNum[0]) == 2
    suit2 = checkNumsSr(nums)

    if (suit1 or suit2) and not(suit1 and suit2):
        cnt += 1
print(cnt)
