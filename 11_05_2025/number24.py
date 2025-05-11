f = open("24_9791.txt", 'r').readline()

m = 0

digits = "0123456789ABCDEF"

for l in range(len(f)):
    for r in range(l + m, len(f)):
        s = f[l:r+1]

        suit = True

        for idx, c in enumerate(s):
            if c not in digits:
                suit = False
                break
        if suit:
            m = max(m, len(s))
        else:
            break
print(m)
