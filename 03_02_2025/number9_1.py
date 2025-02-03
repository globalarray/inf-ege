f = open("demo_2025_9.txt").readlines()

r = 0

for line in f:
    nums = list(map(int, line.split('\t')))

    repeatElement = 0
    passed = False

    for k in nums:
        if line.count(str(k)) == 3:
            passed = True
            repeatElement = k
    if passed:
        notRepeated = list(filter(lambda x: x != repeatElement, nums))

        if len(notRepeated) == len(set(notRepeated)):
            if ((repeatElement * 3)**2) > sum(notRepeated)**2:
                r += 1
print(r)
#https://inf-ege.sdamgia.ru/problem?id=70536
