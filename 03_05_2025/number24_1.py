f = (open("24_17535.txt", 'r').read())

left = 0
cnt = 0

r = 0

for i in range(1, len(f)):
    if f[i-1] + f[i] == 'CD':
        cnt += 1
    while cnt > 160:
        if f[left] + f[left+1] == 'CD':
            cnt -= 1
        left += 1
    if cnt == 160:
        r = max(r, i - left + 1)
print(r)
