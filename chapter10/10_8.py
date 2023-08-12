import random

def has_duplicates(t):
    p = 0
    for i in range(len(t) - 1):
        g = 0
        for i in range(len(t) - 1):
            if t[p] == t[g] and p != g:
                return True
            g += 1
        p += 1

def birthday():
    c = []
    d = 0
    for i in range(100):
        for i in range(23):
            c.append(random.randint(0, 366))
        if has_duplicates(c):
            d += 1
        c = []
    return d / 100

print(birthday())