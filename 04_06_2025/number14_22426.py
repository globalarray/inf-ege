def to7(n):
    r = ""

    if n == 0: return "0"

    lowerZero = n < 0

    n = abs(n)

    while n > 0:
        r += str(n % 7)
        n //= 7
    r = r[::-1]

    if lowerZero:
        r = "-" + r
    return r

v = to7(15*(343**2031)+7*(49**1142)-3*(7**111)+(7**222)-16809).replace("-", "")

chNumCnt = len(list(filter(lambda x: int(x) % 2 == 0, list(v))))

print(abs(chNumCnt - (len(v) - chNumCnt)))
