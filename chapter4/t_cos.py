import math
l = 200
def t_cos(a, b, c):
    cos = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
    print('angle =',math.acos(cos) * 180 / math.pi)
d = math.sqrt((l / 2) ** 2 + (l / 1.2071067811865477) ** 2)
w = 100 / 2 / math.cos(75.5 * math.pi / 180)
w = math.sqrt((l / 1.2071067811865477) ** 2 + l ** 2)
t_cos( w / 2, w / 2.5, l / 1.2071067811865477)