from re import *

f = open("24_20813.txt", 'r').readline().replace('-', 'A', -1).replace('*', 'B', -1)

num = r'([789][0789]*|[0789])'

reg = rf'{num}([AB]{num})+'

mx = 0

for g in finditer(reg, f):
    mx = max(len(g.group()), mx)
print(mx)
