f = open("24_29_03_1.txt", 'r').readline()

mx = [0] * (len(f) + 3)

for i in range(len(f)):
    if f[i:i+3] == "LDR":
        mx[i+3] = max(mx[i+3], mx[i] + 3)
print(max(mx))
