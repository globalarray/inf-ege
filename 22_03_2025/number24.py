f = open("24.txt", 'r').read()

indexes = []

for idx, c in enumerate(f):
    if c == 'W':
        indexes.append(idx)

min_len = 10**10

min_indexes = []

for i in range(len(indexes)-1):
    c = 1 #т.к i - первая W
    for k in range(i+1, len(indexes)):
        c += 1
        if c == 130:
            raz = indexes[k] - indexes[i]

            if min_len > raz:
                min_len = raz
                min_indexes = [indexes[i], indexes[k]]
            break

print(len(f[min_indexes[0]:min_indexes[1]+1]))
