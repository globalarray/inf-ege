f = open("24_21717.txt", 'r').readline()

m = 10000

for l in range(len(f)):
    for r in range(l+m, l, -1):
        s = f[l:r+1]

        if s.count("RSQ") == 130 and s[-1] != "Q":
            m = min(len(s), m)
        elif s.count("RSQ") < 130:
            break
print(m)
