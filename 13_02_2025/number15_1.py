p = set([i for i in range(25, 51)])
q = set([i for i in range(32, 48)])

def f(x, a):
    return not((x in a) or (x in p)) or (not(x in a) or (x in q))

a = set([i for i in range(-1000, 1000)])

for x in range(-1000, 1000):
    if f(x, a) is not True:
        a.remove(x)
print(len(a)-1)
