m = 0

for n in range(4, 10000):
    s = "5" + (n * "2")

    while "52" in s or "2222" in s or "1122" in s:
        s = s.replace("52", "11")
        s = s.replace("2222", "5")
        s = s.replace("1122", "25")
    if sum(map(int, list(s))) == 64:
        m = n
print(m)
