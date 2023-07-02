import turtle
bob = turtle.Turtle()
def square(t): #t - turtle
    for i in range(4):
        t.fd(1000)
        t.lt(90)
    print(t)
    turtle.mainloop()
square(bob)