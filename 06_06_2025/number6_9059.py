from turtle import *

screensize(10000, 10000)
speed(5)
k = 15

down()
begin_fill()
for _ in range(6):
    fd(3*k)
    lt(270)
    fd(5*k)
    rt(90)
end_fill()
lt(270)

begin_fill()
for _ in range(6):
    fd(5*k)
    rt(90)
    fd(3*k)
    lt(270)
end_fill()

cnv = getcanvas()

cnt = 0

for x in range(-200, 200):
    for y in range(-200, 200):
        if cnv.find_overlapping(x*k,y*k,x*k,y*k) != ():
            cnt += 1
print(cnt)
