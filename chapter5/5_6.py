import turtle

bob = turtle.Turtle()
bob.speed(100000000000000000000000000000000000000)

def Koch(t, x):
    if x <= 3:
        t.fd(x)
        return
    Koch(t, x / 3)
    t.lt(60)
    Koch(t, x / 3)
    t.rt(120)
    Koch(t, x / 3)
    t.lt(60)
    Koch(t, x / 3)

# Koch(bob, 1000000000000000000000)

def snowflake(t, x):
    for i in range(3):
        Koch(t, x)
        t.rt(360 / 3)

# snowflake(bob, 100)

def Koch_2(t, x):
    if x <= 3:
        t.fd(x)
        return
    Koch_2(t, x / 3)
    t.lt(80)
    Koch_2(t, x / 3)
    t.rt(160)
    Koch_2(t, x / 3)
    t.lt(80)
    Koch_2(t, x / 3)

Koch_2(bob, 1000)

turtle.mainloop()