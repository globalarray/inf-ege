for a in range(1000):
    b = True

    for x in range(1, 100):
        for y in range(1, 100):
            if not((x - y >= 39) or (y <= x) or (y >= (a - 20))):
                b = False
                break
        else:
            break
    if b:
        print(a)
