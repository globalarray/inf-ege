nums = []

def pushIfSuitableNum(n):
    if n % 451 == 0:
        nums.append(n)

mask = "10?451*3"

for i in range(10):
    num = mask.replace("*", "", 1).replace("?", str(i), 1)

    pushIfSuitableNum(int(num))

limitNum = 0

k = 0

complete = False

while True:
    if complete:
        break

    for i in range(10):
        num = int(mask.replace("*", str(k), 1).replace("?", str(i), 1))

        if num > (10**9):
            complete = True
            break
        pushIfSuitableNum(num)
        if k < 10:
            pushIfSuitableNum(int(mask.replace("*", "0" + str(k), 1).replace("?", str(i), 1)))
    k += 1
nums.sort()

for n in nums:
    print(n, n // 451)
