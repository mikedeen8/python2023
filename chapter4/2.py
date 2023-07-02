import turtle
bob = turtle.Turtle()
def square(t, l): #t - turtle, l - length
    for i in range(4):
        t.fd(l)
        t.lt(90)
    print(t)
    turtle.mainloop()
square(bob, 50)