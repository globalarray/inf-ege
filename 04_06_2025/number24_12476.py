f = open("24_12476.txt", 'r').readline()

l = m = 0

cnt = 0

for r in range(len(f)-3):
    s = f[l:r+3]
    if len([a for a in ["ORO", "ROR"] if a in s]) != 0:
        l = r+1
        cnt = 0
        continue
    cnt = s.count("RO")

    while cnt > 21:
        if f[l] + f[l+1] == 'RO':
            cnt -= 1
        l += 1
    if cnt == 21:
        s = f[l:r+3]
        m = max(m, len(s))
print(m)
