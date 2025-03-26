i = 123456789

while i < 223456790:
    delsCnt = 1 #вкл. корень из числа
    maxDel = 0
    sqrt = i ** 0.5

    if sqrt == round(i**0.5):
        for j in range(2, int(sqrt)-1):
            if i % j == 0:
                if maxDel == 0:
                    maxDel = i // j
                delsCnt += 2

                if delsCnt == 4:
                    break
        if delsCnt == 3:
            print(i, maxDel)
    i += 1
