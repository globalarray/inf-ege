import math


def m(n):
    delimeters = []

    for j in range(1, int(math.sqrt(n))+1):
        if n % j == 0:
            delimeters.append(n // j)
            delimeters.append(j)
    delimeters.sort()
    return delimeters

for i in range(201455, 201470):
    dels = m(i)

    if len(dels) == 4:
        print(dels)
