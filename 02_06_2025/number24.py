f = open("AGU3HUeiX.txt", 'r').readline()

l = 0

m = 100000

cnt = 0

for r in range(len(f)):
    if f[r] == 'Y':
        l = r + 1
        cnt = 0
        continue
    if f[r] == 'X':
        cnt += 1
    while cnt >= 500:
        m = min(r-l+1, m)

        if f[l] == 'X':
            cnt -= 1
        l += 1
print(m)
