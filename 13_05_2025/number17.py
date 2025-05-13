f = list(map(int, open("17_22230.txt", 'r').readlines()))

#ровно два числа являются четырёхзначными
#хотя бы одно число делится без остатка на минимальный положительный элемент последовательности, оканчивающийся на 8
#сумма элементов тройки не меньше максимального элемента последовательности, кратного 25

maxSuitableElement = -float("inf")
minSuitableElement = float("inf")

cnt = 0
maxSum = 0

for n in f:
    if n > 0 and str(n)[-1] == '8':
        minSuitableElement = min(minSuitableElement, n)
    if n % 25 == 0:
        maxSuitableElement = max(maxSuitableElement, n)

for i in range(len(f)-2):
    nums = [f[i], f[i+1], f[i+2]]

    suitableNums = list(filter(lambda x: len(str(abs(x))) == 4, nums))

    if len(suitableNums) == 2:
        if any(list(filter(lambda x: x % minSuitableElement == 0, nums))):
            s = sum(nums)

            if s >= maxSuitableElement:
                cnt += 1
                maxSum = max(s, maxSum)
print(cnt, maxSum)
