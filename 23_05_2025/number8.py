n = 6 # длина числа

cnt = (8 * (9 ** (n - 1))) + 1 #кол-во чисел без 9 в записи

for i in range((10**n)-1, (10**(n-1))-1, -1):
    strI = str(i)

    if "9" in strI:
        continue
    cnt -= 1

    if str(cnt)[-1] != '5':
        continue
    suit = True

    for j in range(1, len(strI)):
        nums = list(map(int, [strI[j - 1], strI[j]]))

        if ((nums[0] % 2) == (nums[1] % 2)) and (nums[0] % 2 != 0):
            suit = False
            break
    if suit:
        print(i)
        break
