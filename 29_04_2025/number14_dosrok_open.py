def to7(n):
    r = ""

    while n > 0:
        r += str(n % 7)
        n //= 7
    return r[::-1]

r = 0

for x in range(1, 2300):
    if to7((7**350)+(7**150)-x).count('0') == 200:
        r = max(r, x)
print(r)
