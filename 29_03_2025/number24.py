f = open("24_29_03.txt", 'r').read()

n = dict()

for i in range(len(f)-1):
    if f[i] == 'E':
        k = f[i+1]

        if k not in n:
            n[k] = 1
            continue

        n[k] += 1

mx = 0

for char, count in n.items():
    if count > mx:
        mx = count
        print(char, count)
