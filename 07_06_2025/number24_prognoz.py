f = open("24 (5).txt", 'r').readline()

m = 0

for l in range(len(f)):
    for r in range(l+m, len(f)):
        s = f[l:r+1]

        if "EE" in s:
            break

        if s.count("ADOBE") <= 80:
            m = max(m, len(s))
        else:
            break
print(m)
