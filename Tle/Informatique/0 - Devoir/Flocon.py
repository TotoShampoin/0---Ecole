import turtle

def trig(size, step):
    if step<=0:
        turtle.fd(size)
    else:
        trig(size/3,step-1)
        turtle.lt( 60)
        trig(size/3,step-1)
        turtle.rt(120)
        trig(size/3,step-1)
        turtle.lt( 60)
        trig(size/3,step-1)

turtle.turtlesize(0.5)
turtle.up()
turtle.goto(-150, 150)
turtle.speed(0)
turtle.down()
for i in range(1,4):
    trig(300,4)
    turtle.rt(120)
