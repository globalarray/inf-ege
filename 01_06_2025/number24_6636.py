f = open("24_6636.txt", 'r').readline()

m = 0

for l in range(len(f)):
    for r in range(l+m, len(f)):
        s = f[l:r+1]

        if len(s) % 2 != 0:
            continue

        suit = True

        for i in range(0, len(s)-1, 2):
            if not(int(s[i]) % 2 == 0 and int(s[i+1]) % 2 != 0):
                suit = False
                break
        if suit:
            print(s)
            m = max(m, len(s))
        else:
            break
print(m // 2)
