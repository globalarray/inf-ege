f = open("1_24.txt", 'r').read().replace("Q", "a").replace("R", "a").replace("W", "a")

f = f.replace("2", "1").replace("4", "1")

print(f)

r = 0
tempLen = 0

for i in range(len(f)-1):
    if f[i] == 'a' and f[i+1] == 'a':
        r = max(r, tempLen + 1)
        tempLen = 0
    elif f[i] == '1' and f[i+1] == '1':
        r = max(r, tempLen + 1)
        tempLen = 0
    else:
        tempLen += 1
r = max(r, tempLen + 1)
print(r)
