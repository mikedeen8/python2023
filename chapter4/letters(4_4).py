import turtle
import math

t = turtle.Turtle()
t.speed(10000000000000000000000)

def triangle(t, l, angle):
    t.fd(l)
    t.rt(180 - angle)
    t.fd(l)
    # t.rt(180 - ((180 - angle) / 2))
    # c = math.sqrt(2 * (l ** 2) - 2 * (l ** 2) * math.cos(angle * math.pi / 180))
    # t.fd(c)
    # t.rt(180 - ((180 - angle) / 2))
    # t.rt(180)
    # t.pu()
    # t.fd(c)
    # t.pd()

def polyline(t, n, l, angle):
    for i in range(n):
        t.fd(l)
        t.lt(angle)

def petal(t, r, angle):
    for i in range(2):
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

def t_cos(a, b, c):
    cos = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
    print('angle =',math.acos(cos) * 180 / math.pi)

def triangle(t, l, angle):
    t.fd(l)
    t.rt(180 - angle)
    t.fd(l)
    # t.rt(180 - ((180 - angle) / 2))
    # c = math.sqrt(2 * (l ** 2) - 2 * (l ** 2) * math.cos(angle * math.pi / 180))
    # t.fd(c)
    # t.rt(180 - ((180 - angle) / 2))
    # t.rt(180)
    # t.pu()
    # t.fd(c)
    # t.pd()

def t_cos(a, b, c):
    cos = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
    print('angle =',math.acos(cos) * 180 / math.pi)

def draw_a(t, l, n):
    t.lt(135 / 2)
    b = l / math.sin(135 / 2 * math.pi / 180)
    triangle(t, b, 45)
    t.bk(b / 2)
    t.rt(180 - (135 / 2))
    c = math.sqrt(2 * ((b / 2) ** 2) - 2 * ((b / 2) ** 2) * math.cos(45 * math.pi / 180))
    t.fd(c)
    t.rt(180)
    t.pu()
    t.fd(c + b / 2 * math.cos(135 / 2 * math.pi / 180))
    t.rt(90)
    t.fd(b / 2 * math.sin(135 / 2 * math.pi / 180))
    t.lt(90)
    t.fd(l / n) #l
    t.pd()  
# draw_a(t, 200)

def draw_b(t, l, n):
    t.lt(90)
    t.fd(l)
    t.rt(90)
    t.fd(l / 1.2071067811865477 / 2.5)
    t.rt(90)
    t.pu()
    t.fd(l / 2.9)
    t.pd()
    t.lt(90)
    arc(t, l / 2.9 / 2, 180)
    t.fd(29.9 / 25 * (l / 1.2071067811865477 / 2.9))
    t.lt(90)
    t.fd(l / 2.9)
    t.lt(90)
    t.fd(l / 2.5)
    t.pu()
    t.rt(90)
    t.fd(l - l / 2.9)
    t.rt(90)
    t.pd()
    t.fd(l /1.2071067811865477 / 2.5 + l / 2.9 / 4.4)
    t.bk(l / 1.2071067811865477 - l / 2.9)
    t.rt(180)
    arc(t, (l - l / 2.9) / 2, 180)
    t.fd(l / 10)
    t.bk(l / 10)
    t.pu()
    t.rt(90)
    t.bk((l - l / 2.9) / 2)
    t.rt(90)
    t.fd((l - l / 2.9) / 2)
    t.rt(90)
    t.fd((l - l / 2.9) / 2)
    t.lt(90)
    t.fd(l / n) #l
    t.pd()
# draw_b(t, 200)

def draw_p(t, l, n):
    t.lt(90)
    t.fd(l)
    t.rt(90)
    t.fd(l / 1.2071067811865477 - l /4)
    t.rt(90)
    t.pu()
    t.fd(l / 2)
    t.pd()
    t.lt(90)
    arc(t, l / 4, 180)
    t.lt(90)
    t.pu()
    t.fd(l / 2)
    t.pd()
    t.rt(90)
    t.fd(l / 1.2071067811865477 - l / 4)
    t.rt(180)
    t.pu()
    t.fd(l / 1.2071067811865477)
    t.rt(90)
    t.fd(l / 2)
    t.lt(90)
    t.fd(l / n)
    t.pd()
# draw_p(t, 200)

def draw_c(t, l, n):
    t.pu()
    t.fd(l / 2)
    t.lt(90)
    t.fd(l)
    t.pd()
    t.lt(90)
    arc(t, l / 2, 180)
    t.pu()
    t.fd(l / n) #l
    t.pd()
# draw_c(t, 200)

def draw_d(t, l, n):
    t.fd(l / 3)
    arc(t, l / 2, 180)
    t.fd(l / 3)
    t.lt(90)
    t.fd(l)
    t.pu()
    t.lt(90)
    t.fd(l / 2 + l / n) #/
    t.pd()
# draw_d(t, 200, 2)

def draw_e(t, l, n):
    t.lt(90)
    t.pu()
    t.fd(l)
    t.pd()
    t.rt(90)
    t.fd(l / 1.2071067811865477)
    t.bk(l / 1.2071067811865477)
    t.lt(180)
    arc(t, l / 4, 180)
    t.fd(l / 1.2071067811865477)
    t.bk(l / 1.2071067811865477)
    t.lt(180)
    arc(t, l / 4, 180)
    t.fd(l / 1.2071067811865477)
    t.bk(l / 1.2071067811865477)
    t.pu()
    t.fd(l / 1.2071067811865477 + l / n) #l
    t.pd()
# draw_e(t, 200)

def draw_f(t, l, n):
    t.lt(90)
    t.fd(l)
    t.rt(90)
    t.fd(l / 1.2071067811865477)
    t.bk(l / 1.2071067811865477)
    t.rt(90)
    t.fd(l / 2.5)
    t.lt(90)
    t.fd(l / 1.2071067811865477)
    t.rt(90)
    t.rt(90)
    t.pu()
    t.fd(l / 1.2071067811865477)
    t.lt(90)
    t.fd(l - l / 2.5)
    t.lt(90)
    t.fd(l / 1.2071067811865477 + l / n) #l
    t.pd()
# draw_f(t, 200, 2)

def draw_g(t, l, n):
    t.pu()
    t.fd(l / 2.5)
    t.pd()
    t.lt(90)
    t.pu()
    t.fd(l)
    t.pd()
    t.lt(90)
    arc(t, l / 2, 270)
    t.rt(90)
    t.bk(l / 3)
    t.fd(l / 1.5)
    t.pu()
    t.rt(90)
    t.fd(l / 2)
    t.lt(90)
    t.fd(l / n) #l
    t.pd()

# draw_g(t, 200)

def draw_h(t, l, n):
    t.lt(90)
    t.fd(l)
    t.bk(l / 2)
    t.rt(90)
    t.fd(l)
    t.lt(90)
    t.fd(l / 2)
    t.bk(l)
    t.rt(90)
    t.pu()
    t.fd(l / n) #l
    t.pd()

# draw_h(t, 200)

def draw_j(t, l, n):
    t.lt(90)
    t.pu()
    t.fd(l / 4)
    t.pd()
    t.rt(180)
    arc(t, l / 4, 180)
    t.fd(l - l / 4)
    t.pu()
    t.bk(l)
    t.rt(90)
    t.fd(l / n) #l
    t.pd()

# draw_j(t, 200)

def draw_i(t, l, n):
    t.fd(l / 2)
    t.bk(l / 4)
    t.lt(90)
    t.fd(l)
    t.rt(90)
    t.fd(l / 4)
    t.bk(l / 2)
    t.pu()
    t.fd(l / 2)
    t.rt(90)
    t.fd(l)
    t.lt(90)
    t.fd(l / n) #l
    t.pd()

# draw_i(t, 200)

def draw_k(t, l, n):
    t.lt(90)
    t.fd(l)
    t.bk(l)
    t.rt(90)
    t.pu()
    t.fd(l / 1.2071067811865477)
    t.pd()
    t.lt(180 - 31.11322355654884)
    w = math.sqrt((l / 1.2071067811865477) ** 2 + (l / 2) ** 2)
    t.fd(w)
    t.rt(180 - (31.11322355654884 * 2))
    t.fd(w)
    t.pu()
    t.rt(31.11322355654884 + 90)
    t.fd(l)
    t.lt(90)
    t.fd(l / n) #l
    t.pd()

# draw_k(t, 200)

def draw_l(t, l, n):
    t.fd(l / 1.2071067811865477)
    t.bk(l / 1.2071067811865477)
    t.lt(90)
    t.fd(l)
    t.bk(l)
    t.rt(90)
    t.pu()
    t.fd(l / n + l / 1.2071067811865477) #l
    t.pd()

# draw_l(t, 200)

def draw_m(t, l, n):
    t.lt(90)
    t.fd(l)
    t.pu()
    t.bk(l)
    t.rt(90)
    t.fd(l / 1.2071067811865477 / 2)
    t.lt(180 - 67.50000000000001)
    d = math.sqrt(l ** 2 + (l / 1.2071067811865477 / 2) ** 2)
    t.pd()
    t.fd(d)
    t.bk(d)
    t.rt(180 - (67.50000000000001 * 2))
    t.fd(d)
    t.rt(67.50000000000001 + 90)
    t.fd(l)
    t.lt(90)
    t.pu()
    t.fd(l / n + 10) #l
    t.pd()

# draw_m(t, 200)

def draw_n(t, l, n):
    t.lt(90)
    t.fd(l)
    t.pu()
    t.bk(l)
    t.rt(90)
    t.fd(l / 1.2071067811865477)
    t.lt(180 - 50.36072776224388)
    d = math.sqrt(l ** 2 + (l / 1.2071067811865477) ** 2)
    t.pd()
    t.fd(d)
    t.bk(d)
    t.rt(90 - 50.36072776224388)
    t.fd(l)
    t.lt(180)
    t.fd(l)
    t.lt(90)
    t.pu()
    t.fd(l / n)  #l
    t.pd()

# draw_n(t, 200)

def draw_o(t, l, n):
    t.pu()
    t.fd(l / 2.5)
    t.pd()
    petal(t, l / 2, 175)
    t.pu()
    t.fd(l / 2 + l / n + 10)
    t.pd()

# draw_o(t, 200)

def draw_q(t, l, n):
    t.pu()
    t.fd(l / 2.5)
    t.pd()
    arc(t, l / 2, 360)
    t.pu()
    t.fd(l / 1.2071067811865477 / 4)
    t.pd()
    t.lt(135)
    t.fd(l / 1.2071067811865477 / 4)
    t.bk(l / 1.2071067811865477 / 3)
    t.fd(l / 1.2071067811865477 / 3 - l / 1.2071067811865477 / 4)
    t.lt(45)
    t.pu()
    t.rt(45)
    t.bk(l / 1.2071067811865477 / 3 - l / 1.2071067811865477 / 4) 
    t.fd(l / 1.2071067811865477 / 3)
    t.bk(l / 1.2071067811865477 / 4)
    t.rt(135)
    t.bk(l / 1.2071067811865477 / 4)
    t.fd(l / 1.2071067811865477 / 2 + l / n)
    t.pd()

# draw_q(t, 200)

def draw_r(t, l, n):
    t.lt(90)
    t.fd(l)
    t.rt(90)
    t.fd(l / 1.2071067811865477 - l /4)
    t.rt(90)
    t.pu()
    t.fd(l / 2)
    t.pd()
    t.lt(90)
    arc(t, l / 4, 180)
    t.lt(90)
    t.pu()
    t.fd(l / 2)
    t.pd()
    t.rt(90)
    t.fd(l / 1.2071067811865477 - l / 4)
    t.rt(180)
    t.rt(90 - 58.886776443451176)
    d = math.sqrt((l / 2) ** 2 + (l / 1.2071067811865477) ** 2)
    t.fd(d)
    t.pu()
    t.lt(90 - 58.886776443451176)
    t.fd(l / n)
    t.pd()

# draw_r(t, 200)

def draw_s(t, l, n):
    t.pu()
    t.lt(90)
    t.fd(l)
    t.rt(90)
    t.fd(l / 1.2071067811865477 + l / 1.2071067811865477 / 4)
    t.pd()
    t.lt(180)
    t.fd(l / 1.2071067811865477)
    arc(t, l / 4, 180)
    t.fd(l / 1.2071067811865477)
    t.rt(90)
    t.pu()
    t.fd(l / 2) 
    t.pd()
    t.lt(90)
    arc(t, l / 4, 180)
    t.pu()
    t.lt(90)
    t.fd(l / 2) 
    t.pd()
    t.rt(90)
    t.fd(l / 1.2071067811865477 + l / 1.2071067811865477 / 4)
    t.bk(l / 1.2071067811865477 + l / 1.2071067811865477 / 4)
    t.pu()
    t.rt(180)
    t.fd(l / 1.2071067811865477 / 4 + l / n) #l
    t.pd()

# draw_s(t, 200)

def draw_t(t, l, n):
    t.pu()
    t.fd(l / 1.2071067811865477 / 2)
    t.pd()
    t.lt(90)
    t.fd(l)
    t.rt(90)
    t.bk(l / 1.2071067811865477 / 2)
    t.fd(l / 1.2071067811865477)
    t.rt(90)
    t.pu()
    t.fd(l)
    t.lt(90)
    t.fd(l / n) #l
    t.pd()

# draw_t(t, 200)

def draw_u(t, l, n):
    t.lt(90)
    t.pu()
    t.fd(l / 1.2071067811865477 / 2)
    t.pd()
    t.fd(l - (l / 1.2071067811865477 / 2))
    t.bk(l - l / 1.2071067811865477 / 2)
    t.rt(180)
    arc(t, l / 1.2071067811865477 / 2, 180)
    t.fd(l - l / 1.2071067811865477 / 2 + 2)
    t.bk(l - l / 1.2071067811865477 / 2 + 2)
    t.pu()
    t.bk(l / 1.2071067811865477 / 2)
    t.rt(89.7)
    t.fd(l / n + 10) #l
    t.pd()

# draw_u(t, 200)

def draw_v(t, l, n):
    b = l / math.sin(135 / 2 * math.pi / 180)
    s = l /  math.cos(135 / 2 * math.pi / 180)
    t.lt(90)
    t.pu()
    t.fd(l)
    t.rt(90)
    t.fd(l / 1.2071067811865477)
    t.pd()
    t.rt(180)
    t.lt(135 / 2)
    triangle(t, b, 45)
    t.bk(b / 2)
    t.rt(180 - (135 / 2))
    c = math.sqrt(2 * ((b / 2) ** 2) - 2 * ((b / 2) ** 2) * math.cos(45 * math.pi / 180))
    t.pu()
    t.fd(c)
    t.rt(90)
    t.fd(l / 2)
    t.lt(90)
    t.fd(l / n)
    t.pd()

# draw_v(t, 200)

def draw_w(t, l, n):
    t.pu()
    t.fd(l / 1.2071067811865477)
    t.lt(90)
    t.fd(l)
    t.rt(90)
    t.pd()
    t.lt(180)
    t.lt(90)
    t.fd(l)
    t.pu()
    t.bk(l)
    t.rt(90)
    t.fd(l / 1.2071067811865477 / 2)
    t.lt(180 - 67.50000000000001)
    d = math.sqrt(l ** 2 + (l / 1.2071067811865477 / 2) ** 2)
    t.fd(d / 2)
    t.pd()
    t.fd(d / 2)
    t.bk(d / 2)
    t.rt(180 - (67.50000000000001 * 2))
    t.fd(d / 2)
    t.rt(67.50000000000001 + 90)
    t.fd(l)
    t.lt(90)
    t.lt(90)
    t.fd(l)
    t.lt(90)
    t.pu()
    t.fd(l / 1.2071067811865477 + l / n)
    t.pd()

# draw_w(t, 200)

def draw_x(t, l, n):
    t.lt(90)
    t.pu()
    t.fd(l)
    t.pd()
    t.rt(180 - 39.639272237756124)
    w = math.sqrt((l / 1.2071067811865477) ** 2 + l ** 2)
    t.fd(w)
    t.rt(90 + 39.639272237756124)
    t.pu()
    t.fd(l / 1.2071067811865477)
    t.pd()
    t.rt(90 + 39.639272237756124)
    t.fd(w)
    t.rt(180 - 39.639272237756124)
    t.pu()
    t.fd(l)
    t.lt(90)
    t.fd(l / n)

# draw_x(t, 200)

def draw_y(t, l, n):
    t.lt(6)
    t.lt(39.639272237756124)
    w = math.sqrt((l / 1.2071067811865477) ** 2 + l ** 2)
    t.fd(w)
    t.rt(180)
    t.fd(w / 2)
    t.rt(180 - 89.56780231091845)
    t.fd(w / 2)
    t.pu()
    t.bk(w)
    t.rt(180 - 89.56780231091845 / 2)
    t.fd(l / n)
    t.rt(90)
    t.fd(l / 10)
    t.lt(90)
    t.pd()

# draw_y(t, 200)


def draw_z(t, l, n):
    t.lt(90)
    t.pu()
    t.fd(l)
    t.pd()
    t.rt(90)
    t.fd(l)
    t.pu()
    t.bk(l)
    t.rt(90)
    t.fd(l / 1.2071067811865477)
    t.lt(180 - 50.36072776224388)
    d = math.sqrt(l ** 2 + (l / 1.2071067811865477) ** 2)
    t.pd()
    t.fd(d)
    t.bk(d)
    t.rt(90 - 50.36072776224388)
    t.fd(l)
    t.lt(180)
    t.fd(l)
    t.lt(180)
    t.pu()
    t.fd(l / 1.2071067811865477 + l / n) #l
    t.pd()

# draw_z(t, 200)


def letters(t, l, s, n):
    p = list(s)
    t.rt(90)
    t.pu()
    t.fd(100)
    t.pd()
    t.lt(90)
    # print(p[0])
    for i in range(len(p)):
        if p[i] == 'a':
            draw_a(t, l, n)
        elif p[i] == 'b':
            draw_b(t, l, n)
        elif p[i] == 'c':
            draw_c(t, l, n)
        elif p[i] == 'd':
            draw_d(t, l, n)
        elif p[i] == 'e':
            draw_e(t, l, n)
        elif p[i] == 'f':
            draw_f(t, l, n)
        elif p[i] == 'g':
            draw_g(t, l, n)
        elif p[i] == 'h':
            draw_h(t, l, n)
        elif p[i] == 'i':
            draw_i(t, l, n)
        elif p[i] == 'j':
            draw_j(t, l, n)
        elif p[i] == 'k':
            draw_k(t, l, n)
        elif p[i] == 'l':
            draw_l(t, l, n)
        elif p[i] == 'm':
            draw_m(t, l, n)
        elif p[i] == 'n':
            draw_n(t, l, n)
        elif p[i] == 'o':
            draw_o(t, l, n)
        elif p[i] == 'p':
            draw_p(t, l, n)
        elif p[i] == 'q':
            draw_q(t, l, n)
        elif p[i] == 'r':
            draw_r(t, l, n)
        elif p[i] == 's':
            draw_s(t, l, n)
        elif p[i] == 't':
            draw_t(t, l, n)
        elif p[i] == 'u':
            draw_u(t, l, n)
        elif p[i] == 'v':
            draw_v(t, l, n)
        elif p[i] == 'w':
            draw_w(t, l, n)
        elif p[i] == 'x':
            draw_x(t, l, n)
        elif p[i] == 'y':
            draw_y(t, l, n)
        elif p[i] == 'z':
            draw_z(t, l, n)
        elif p[i] == ' ':
            t.pu()
            t.fd(l * n / 2)
            t.pd()
# letters(t, 50, 'ass we can', 2)
t.pu()
t.bk(900)
t.pd()
# letters(t, 50, 'qwertyuiopasdfghjklzxcvbnm', 2)
turtle.mainloop()