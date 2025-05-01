Apr = [2, 4, 6, 8, 12, 2311]
Mar = [4, 8, 12, 2025]

May = Apr + Mar

for x in May:
    if (x not in Apr) or (x not in Mar):
        May.remove(x)
print(sum(set(May)))
