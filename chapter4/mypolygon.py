import turtle
import math
bob = turtle.Turtle()
for i in range(4):
    bob.fd(100)
    bob.rt(90)
print(bob)
turtle.mainloop()
# def draw_m(t, l):
#     t.lt(90)
#     t.fd(l)
#     t.pu()
#     t.bk(l)
#     t.rt(90)
#     t.fd(l / 1.2071067811865477 / 2)
#     t.lt(180 - 67.50000000000001)
#     d = math.sqrt(l ** 2 + (l / 1.2071067811865477 / 2) ** 2)
#     t.fd(d / 2)
#     t.pd()
#     t.fd(d / 2)
#     t.bk(d / 2)
#     t.rt(180 - (67.50000000000001 * 2))
#     t.fd(d / 2)
#     t.rt(67.50000000000001 + 90)
#     t.fd(l)
#     t.lt(90)
#     t.pu()
#     t.fd(l / 1.5) #l
#     t.pd()

# draw_m(bob, 200)

# turtle.mainloop()
# draw_m(t, 200)