for a in range(1, 10000):
    suit = True

    for x in range(1, 1000):
        b = 35 <= x <= 65

        if not (b <= (((x + 1) % 17 != 0) or x % a == 0)):
            suit = False
            break
    if suit:
        print(a)
