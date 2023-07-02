import turtle
import math
bob = turtle.Turtle()

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
    turtle.mainloop()

arc(bob, 100, 360)