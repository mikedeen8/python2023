import turtle
import math

bob = turtle.Turtle()
bob.speed(1000000000000000000000)
# bob.lt(90)
def triangle(t, l, angle):
    t.fd(l)
    t.rt(180 - angle)
    t.fd(l)
    t.rt(180 - ((180 - angle) / 2))
    c = math.sqrt(2 * (l ** 2) - 2 * (l ** 2) * math.cos(angle * math.pi / 180))
    t.fd(c)
    # t.rt(180 - ((180 - angle) / 2))
    t.rt(180)
    t.pu()
    t.fd(c)
    t.pd()

# triangle(bob, 200, 72)

def figure(t, l, number):
    N = 360 / number
    if number == 6:
        t.rt(90)
    for i in range(number):
        triangle(t, l, N)
        t.lt(180 - (180 - N) / 2)

# bob.pu()
# bob.bk(700)
# bob.pd()
# figure(bob, 100, 5)
# bob.pu()
# bob.fd(700)
# bob.pd()
# figure(bob, 100, 6)
# bob.pu()
# bob.lt(90)
# bob.fd(700)
# bob.pd()
# figure(bob, 100, 7)

bob.pd
figure(bob, 100, 10)

turtle.mainloop()