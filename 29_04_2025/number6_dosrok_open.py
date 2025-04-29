from turtle import *

screensize(2000, 2000)
tracer(0)
k=20

down()

rt(90)

for _ in range(7):
    rt(45)
    fd(11*k)
    rt(45)

up()

for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(4, 'black')
update()

done()
