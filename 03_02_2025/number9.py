f = open("09.txt").readlines()

r = 0

for line in f:
    nums = list(map(int, line.split('\t')))

    if len(nums) == len(set(nums)):
        m = max(nums) + min(nums)

        if m / 2 > (sum(nums) - m) / (len(nums) - 2):
            r += 1
print(r)
#https://inf-ege.sdamgia.ru/problem?id=61355
