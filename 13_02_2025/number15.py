def f(x, a):
    return (not(x in a) or (x*x <= 100)) and ((x*x > 64) or (x in a))

a = set([i for i in range(-1000, 1000)])

for x in range(-1000, 1000):
    if not(f(x, a)):
        a.remove(x)
print(len(a)-1)
