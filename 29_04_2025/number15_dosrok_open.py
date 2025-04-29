for a in range(1000):
    suit = True

    for x in range(1000):
        if not(not(x&52 != 0 and (x&48 == 0)) or not(x&a == 0)):
            suit = False
    if suit:
        print(a)
        break
