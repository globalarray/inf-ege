def getDelimetersCnt(v):
    cnt = 0

    for i in range(1, int(v**0.5)+1):
        if v % i == 0:
            cnt += 2
    return cnt

for n in range(1, 10000):
    s = '>' + ('0' * 39) + ('1' * n) + ('2' * 39)

    while (">1" in s) or (">2" in s) or (">0" in s):
        if ">1" in s:
            s = s.replace(">1", "22>", 1)
        if ">2" in s:
            s = s.replace(">2", "2>", 1)
        if ">0" in s:
            s = s.replace(">0", "1>", 1)

    delCnt = getDelimetersCnt(sum(map(int, list(filter(lambda c: c.isdigit(), s)))))

    if delCnt == 2:
        print(n)
        break
