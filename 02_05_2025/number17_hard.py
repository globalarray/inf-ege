from math import prod

f = list(map(int, open("17.16_14653.txt", 'r')))

"""f2 = f.copy()

f2.sort()

print(list(filter(lambda x: x>0 and x % 17 == 0, f2)))"""

#17+17

maxEl = 0

"""for n in f:
    if len(str(n)) < 2:
        continue

    if str(n)[-2] + str(n)[-1] == "69":
        maxEl = max(maxEl, n)
print(maxEl)

exit()"""

cnt = 0
minSquare = float("inf")

minElementsSum = 17 * 2

for i in range(len(f)-3):
    nums = [f[i+j] for j in range(4)]

    if len(list(filter(lambda x: len(str(abs(x))) == 3, nums))) != 2:
        continue
    if len(list(filter(lambda x: x % 18 == 0, nums))) != 1:
        continue
    s = sum(nums)
    if s % minElementsSum != 0:
        continue
    if prod(nums) > (9969 ** 2):
        continue
    minSquare = min(minSquare, s ** 2)
    cnt += 1
print(cnt, minSquare)
