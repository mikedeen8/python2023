import math

def estimate_pi():
    k = 0
    a = 2 * math.sqrt(2) / 9801
    S = 0
    b = (math.factorial(4 * k) * (1103 + 26390 * k)) / ((math.factorial(k) ** 4) * (396 ** (4 * k)))
    while b >= 1e-15:
        # print(k)
        b = (math.factorial(4 * k) * (1103 + 26390 * k)) / ((math.factorial(k) ** 4) * (396 ** (4 * k)))
        # print(b)
        S += a * b
        k += 1

    pi = S
    # print(1 / math.pi)
    return pi

print(estimate_pi())