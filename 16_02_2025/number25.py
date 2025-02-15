limMask = 0

i = 0

while True:
    temp = "12991%d56" % i #12??1*56

    if int(temp) <= 10**8:
        limMask = temp
    else:
        break

    i += 1

jStr = "12??1*56"

for j in range(int("1200156"), int(limMask) + 1):
    jStr = str(j)

    if j % 317 == 0 and jStr[:2] == "12" and jStr[4] == '1' and jStr[-2:] == "56":
        print(j, j // 317)
