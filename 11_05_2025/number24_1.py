f = open("24_4602.txt", 'r').readline()

m = 0

for l in range(len(f)):
    for r in range(l + m, len(f)):
        s = f[l:r+1]

        suit = True

        for i in range(0, len(s)-1, 2):
            if not((s[i] in "BCD") and (s[i+1] in "AO")):
                suit = False
                break
        if suit:
            m = max(len(s), m)
        else:
            break
print(m//2)
