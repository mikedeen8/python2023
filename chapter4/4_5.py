import turtle
import math
bob = turtle.Turtle()
bob.speed(10000000000000000)
bob.pencolor('blue')
vov = turtle.Turtle()
vov.speed(10000000000000000)
vov.pencolor('red')
turtle.bgcolor('black')



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

            

def triangle1(t, l, angle):
    t.fd(l)
    t.rt(180 - angle)
    t.fd(l)
    t.rt(180 - ((180 - angle) / 2))
    c = math.sqrt(2 * (l ** 2) - 2 * (l ** 2) * math.cos(angle * math.pi / 180))
    t.fd(c)
    t.rt(180 - ((180 - angle) / 2))
    t.rt(180)
    t.pu()
    t.fd(c)
    t.pd()
    print(c)

def spiral_1(t, r):
    for i in range(r):
        arc(t, r, 10)
        r = r / 1.01
spiral_1(bob, 200)
def spiral_2(T, R):
    T.lt(90)
    T.pu()
    T.fd(150)
    T.lt(90)
    T.fd(70)
    T.rt(90)
    T.pd()
    for i in range(R):
        triangle1(T, R, 72)
        T.rt(50)
        R = R - 1
spiral_2(vov, 200)


turtle.mainloop()