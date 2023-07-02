#me
import turtle
import math

bob = turtle.Turtle()
def polygon(t, n, l): #t - turtle, l - length, n - number of sides
    for i in range(n):
        t.fd(l)
        t.lt(360 / n)
    print(t)
    turtle.mainloop()
def circle(t, r):
    c = 2 * math.pi * r
    n = 50
    l = c / n
    polygon(t, n, l)
circle(bob, 100) 

#Downey
# import math
# import turtle

# bob = turtle.Turtle()
# def polygon(t, l, n): #t - turtle, l - length, n - number of sides
#     for i in range(n):
#         t.fd(l)
#         t.lt(n / 360)
#     print(t)
#     turtle.mainloop()
# def circle(t, r):
#     circumfrence = 2 * math.pi * r
#     n = 50
#     length = circumfrence / n
#     polygon(t, length, n)
# circle(bob, 180)