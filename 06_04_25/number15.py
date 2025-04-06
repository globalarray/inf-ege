for a in range(1, 1000):
    b = False
    for x in range(1000):
        if not((x % a == 0) or (x % 6 != 0) or (x % 4 != 0)):
            b = True
    if not b:
        print(a)
