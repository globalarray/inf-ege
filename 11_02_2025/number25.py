import math

def m(n):
    delimeters = []

    for j in range(1, int(math.sqrt(n)) + 1):
        if n % j == 0 and j != 1 and j != n:
            delimeters.append(n // j)
            delimeters.append(j)
    if len(delimeters) < 2:
        return 0

    delimeters.sort(reverse=True)

    return sum(delimeters[:2])

r = []

for i in range(112_500_000, 112_550_000 + 1):
    s = str(m(i))
    
    if s[-4:] == "1214":
        r.append(i)
r.sort()

print(r)
