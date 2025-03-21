s = '>' + ('1' * 26) + ('2' * 10) + ('3' * 14)

while (">1" in s) or (">2" in s) or (">3" in s):
    if ">1" in s:
        s = s.replace(">1", "22>", 1)
    if ">2" in s:
        s = s.replace(">2", "2>", 1)
    if ">3" in s:
        s = s.replace(">3", "1>", 1)

print(sum(map(int, filter(lambda x: x.isdigit(), list(s)))))
