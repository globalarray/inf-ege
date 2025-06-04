for a in range(1000):
    b = True
    for x in range(1000):
        if not b:
            break
        for y in range(1000):
            if not((x*x <= 136) or (y < 4 * x + a - 70) or (2 * y > 51)):
                b = False
                break
    if b:
        print(a)
        break
