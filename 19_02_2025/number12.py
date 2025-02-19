s = '0' + (12 * '1') + (15 * '2') + (17 * '3')

while ("01" in s) or ("02" in s) or ("03" in s):
    s = s.replace("01", "103", 1)
    s = s.replace("02", "10", 1)
    s = s.replace("03", "210", 1)
print(s.count('2'))
