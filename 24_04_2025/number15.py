b = [i for i in range(60, 81)]

for a in range(1, 1000):
    suit = True
    for x in range(1, 1000):
        if not(x % a == 0 or ((x not in b) or x % 22 != 0)):
            suit = False
            break
    if suit:
        print(a)
