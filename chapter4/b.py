import math
import turtle

bob = turtle.Turtle()
def polyline(t, n, l, angle):
    for i in range(n):
        t.fd(l)
        t.lt(angle)

def petal(t, r, angle):
    arc(t, r, angle)
    t.lt(180 - angle)

def polygon(t, n, l, angle): #t - turtle, l - length, n - number of sides
    angle = 360 / n
    polyline(t, n, l, angle)

def arc(t, r, angle):
    c = 2 * math.pi * r * angle / 360
    n = int(c / 3) + 1
    l = c / n
    step_angle = angle / n
    polyline(t, n, l, step_angle)
def draw_b(t, l):
    t.lt(90)
    t.fd(l)
    t.rt(90)
    t.fd(l / 2.5)
    t.rt(90)
    t.pu()
    t.fd(l / 2.9)
    t.pd()
    t.lt(90)
    arc(t, l / 2.9 / 2, 180)
    t.fd(29.9 / 25 * (l / 2.9))
    t.lt(90)
    t.fd(l / 2.9)
    t.lt(90)
    t.fd(l / 2.5)
    t.pu()
    t.rt(90)
    t.fd(l - l / 2.9)
    t.rt(90)
    t.pd()
    t.fd(l / 2.5)
    t.bk(l / 2.5)
    t.rt(180)
    arc(t, (l - l / 2.9) / 2, 180)
    t.pu()
    t.rt(90)
    t.bk((l - l / 2.9) / 2)
    t.rt(90)
    t.fd((l - l / 2.9) / 2)
    t.rt(90)
    t.fd((l - l / 2.9) / 2)
    t.lt(90)
    t.fd(l / 1.5) #l
    t.pd()
# draw_b(t, 200)
def triangle(t, l, angle):
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
triangle(bob, 200, 45)
