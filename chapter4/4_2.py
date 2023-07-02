import turtle
import math
bob = turtle.Turtle()
bob.speed(100000000)

def polyline(t, n, l, angle):
    for i in range(n):
        t.fd(l)
        t.lt(angle)

def polygon(t, n, l, angle): #t - turtle, l - length, n - number of sides
    angle = 360 / n
    polyline(t, n, l, angle)

def arc(t, r, angle):
    c = 2 * math.pi * r * angle / 360
    n = int(c / 3) + 1
    l = c / n
    step_angle = angle / n
    polyline(t, n, l, step_angle)

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)
def petal2(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)
# petal(bob, 100, 80)

# for i in range(7):  
#     petal(bob, 500, 360 / 7)
#     bob.lt(360 / 7)
#     petal(bob, 500, 360 / 7)

# petal(bob, 100)

def flower_1(t, r, number):
    for i in range(number):
        petal(t, r, 360 / number)
        t.lt(360 / number)

def flower_2(t, r, number):
    for i in range(number):
        petal2(t, r, 90)
        t.lt(360 / number)

def flowers():
    bob.pu()
    bob.bk(300)
    bob.pd()
    flower_1(bob, 100, 7)
    bob.pu()
    bob.fd(300)
    bob.pd()
    flower_2(bob, 50, 10)
    bob.pu()
    bob.fd(300)
    bob.pd()
    flower_1(bob, 300, 20)

flowers() 

turtle.mainloop()