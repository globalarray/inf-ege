f = map(lambda l: list(map(int, l)), map(lambda s: s.split(), open("107_9.txt", 'r').readlines()))

cnt = 0

for nums in f:

    suitable = False

    for i in range(4):
        for j in range(i + 1, 4):
            indexes = [0, 1, 2, 3]

            indexes.remove(i)
            indexes.remove(j)

            for sIdx in indexes:
                if nums[i] + nums[j] < nums[sIdx]:
                    suitable = True
    if suitable:
        cnt += 1
print(cnt)
