import turtle

bob = turtle.Turtle()
# bob.speed(100000000000000000000)

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n - 1)
    t.rt(2 * angle)
    draw(t, length, n - 1)
    t.lt(angle)
    t.bk(length * n)

draw(bob, 100, 3)

turtle.mainloop()