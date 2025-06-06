f = open("24_21.txt", 'r').readline()

m = 0

for l in range(len(f)):
    for r in range(l+m, len(f)):
        s = f[l:r+1]

        if len([cmb for cmb in ["XX", "YY", "ZZ"] if cmb in s]) == 0:
            m = max(m, len(s))
        else:
            break
print(m)
