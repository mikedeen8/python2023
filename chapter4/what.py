import turtle
import math
bob = turtle.Turtle()
for i in range(4):

    #M
    bob.lt(90)
    bob.fd(20)
    bob.rt(150)
    bob.fd(40/math.sqrt(3))
    bob.lt(120)
    bob.fd(40/math.sqrt(3))
    bob.rt(150)
    bob.fd(20)

    #M-R
    bob.pu()
    bob.lt(90)
    bob.fd(20)
    bob.lt(90)
    bob.pd()

    #R
    bob.fd(20)
    bob.rt(120)
    bob.fd(10)
    bob.rt(120)
    bob.fd(10)
    bob.lt(60 + math.acos(2/math.sqrt(7))*180/math.pi)
    bob.fd(5*math.sqrt(7))
    bob.lt(math.asin(2/math.sqrt(7))*180/math.pi)

    #R - A
    bob.pu()
    bob.fd(20)
    bob.lt(90)
    bob.pd()

    #A
    bob.rt(15)
    bob.fd(20/math.cos(15*math.pi/180))
    bob.rt(150)
    bob.fd(20/math.cos(15*math.pi/180))
    bob.pu()
    bob.lt(180)
    bob.fd(10/math.cos(15*math.pi/180))
    bob.lt(75)
    bob.pd()
    bob.fd(20*math.cos(75*math.pi/180))
    bob.pu()
    bob.lt(75)
    bob.fd(10/math.cos(15*math.pi/180))
    bob.lt(105)
    bob.fd(40*math.cos(75*math.pi/180))

    #A - Z
    bob.fd(20)
    bob.lt(90)
    bob.pd()

    # Z
    bob.lt(90)
    bob.bk(20)
    bob.pu()
    bob.fd(20)
    bob.rt(135)
    bob.pd()
    bob.fd(40 / math.sqrt(2))
    bob.lt(135)
    bob.fd(20)

turtle.mainloop()