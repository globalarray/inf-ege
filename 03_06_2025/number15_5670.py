for a in range(1, 1000):
    b = True

    for x in range(1, 1000):
        if not ((x + a >= 160) or ((x % 7 == 0) <= (not(x - 17 > 0)))):
            b = False
            break
    if b:
        print(a)
        break
