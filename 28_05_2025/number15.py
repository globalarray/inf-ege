for a in range(100, 1, -1):
    suit = True

    for x in range(1, 1000):
        if not ((120 % a == 0) and ((x % a != 0) <= ((x % 18 == 0) <= (x % 24 != 0)))):
            suit = False
            break
    if suit:
        print(a)
        break
