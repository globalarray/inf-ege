f = open("inf_22_10_20_24.txt", 'r').readlines()

cnt = 0

for l in f:
    if l.count('E') > l.count('A'):
        cnt += 1
print(cnt)
