f = open("24_22362.txt", 'r').readline()

m = 0

for l in range(len(f)):
    for r in range(l+m-1, len(f)):
        s = f[l:r+1]

        if len(s) > 0 and (s[0] == '0' or s[-1] not in "0369"):
            break

        suit = True

        for c in s:
            if c not in "0123456789AB":
                suit = False
                break
        if suit:
            if len(s) == 109:
                print(int(s, 12), l)
            m = max(m, len(s))
        else:
            break
print(m)
