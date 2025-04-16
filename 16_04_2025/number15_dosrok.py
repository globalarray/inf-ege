for a in range(1000):
    suit = True
    for x in range(1000):
        for y in range(1000):
            if not((5 < y) or (x > 32) or (x + (2 * y) < a)):
                suit = False
                break
        else:
            continue
        break
    if suit:
        print(a)
        break
