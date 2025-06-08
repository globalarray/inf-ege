r = 0
maxSum = 0

for n in range(4, 10000):
    s = "1" + ("2" * n)

    while "12" in s or "322" in s or "222" in s:
        s = s.replace("12", "2", 1)
        s = s.replace("322", "21", 1)
        s = s.replace("222", "3", 1)
    s = sum(map(int, list(s)))

    if s >= maxSum:
        maxSum = s
        r = n
print(r)
