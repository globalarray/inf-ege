m = 0

for a in range(1, 3000):
    s = (a*768*12)*50

    if s / 1_310_720 <= 300:
        m = max(m, a)
print(m)
