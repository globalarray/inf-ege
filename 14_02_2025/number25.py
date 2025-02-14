limFormat = "129936*1"

lim = 0

i = 0

while True:
    l = int(limFormat.replace('*', str(i), 1))

    if l < 10**8:
        lim = l
    else:
        break

    i += 1
for j in range(int("1200361"), lim+1):
    jStr = str(j)

    if j % 273 == 0 and jStr[:2] == "12" and jStr[-1:] == "1" and jStr[4:6] == "36":
        print([j, j // 273])
