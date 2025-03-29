def suitable(n):
    if n % 3147 == 0:
        print(n)

msk = "1*4239?7"

j = 0

while True:
    v = msk.replace("?", "9", 1).replace("*", str(j), 1)

    if int(v) > 10**10:
        break

    j += 1

for i in range(10):
    v = int(msk.replace("?", str(i), 1).replace("*", "", 1))

    suitable(v)

for k in range(j+1):
    for i in range(10):
        if k < 10:
            v = int(msk.replace("?", str(i), 1).replace("*", "00" + str(k), 1))
            suitable(v)
        if k < 100:
            v = int(msk.replace("?", str(i), 1).replace("*", "0" + str(k), 1))
            suitable(v)

        v = int(msk.replace("?", str(i), 1).replace("*", str(k), 1))

        suitable(v)
