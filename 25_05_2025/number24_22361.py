f = open("24_22360.txt", 'r').readline()

m = 0

digits = "01234567"

d = 10**100

for l in range(len(f)):
    if f[l] == '0':
        continue
    for r in range(l+m, len(f)):
        s = f[l:r+1]

        suit = True

        for c in s:
            if c not in digits:
                suit = False
                break

        if suit:
            m = max(len(s), m)
        else:
            break
print(m)

for l in range(len(f)):
    if f[l] == '0':
        continue
    for r in range(l+16, len(f)):
        s = f[l:r + 1]

        suit = True

        for c in s:
            if c not in digits:
                suit = False
                break

        if suit:
            v = int(s, 8)

            if v < d:
                print(l, s)
                d = v
        break

"""for l in range(len(f)):
    for r in range(l+108, len(f)):

        s = f[l:r + 1]

        if len(s) > 0 and (s[0] == '0' or s[-1] not in "06"):
            break

        suit = True

        for c in s:
            if c not in "0123456789AB":
                suit = False
                break
        if suit:
            print(int(s, 12), r)

        break"""
