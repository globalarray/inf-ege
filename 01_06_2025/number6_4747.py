from turtle import *

screensize(10000, 10000)
tracer(0)
k = 15

down()

colors = ["black", "green", "red", "yellow", "purple", "orange", "blue", "brown", "pink", "magenta", "aqua"]

for i in range(100):
    idx = i

    if i > 9:
        idx = int(i - (10 * (i // 10)))
    clr = colors[idx]

    color(clr)

    fd(10*k)
    rt(50)

    print(pos())

    g = list(map(lambda x: abs(int(x)), pos()))

    if g[0] == g[1] == 0:
        break
print(i+1)
update()
done()
