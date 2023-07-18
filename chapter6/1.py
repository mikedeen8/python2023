import math

def hypotenuse(a, b):
    s_a = a ** 2
    # print(s_a)
    s_b = b ** 2
    # print(s_b)
    s_hypotenuse = s_a + s_b
    # print(s_hypotenuse)
    hypotenuse = math.sqrt(s_hypotenuse)
    # print(hypotenuse)
    if hypotenuse == int(hypotenuse):
        return int(hypotenuse)
    else:
        return hypotenuse

print(hypotenuse(3, 4))