from string import printable

def to27(n):
    r = ""

    n = abs(n)

    while n > 0:
        r += printable[n % 27]
        n //= 27
    return r[::-1]

cnt = 0

for c in to27(4*(729**2025)+2*(243**1413)-5*(81**169)-3*(9**107)+7019):
    if int(c, 27) % 3 == 0:
        cnt += 1
print(cnt)
