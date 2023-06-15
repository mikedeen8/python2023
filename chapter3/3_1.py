import math
def right_justify(s):
    b = 70 - len(s) - 1
    if b<0:
        print(s[abs(b):])
    else:
        l =' ' * b + s
        print(l)
right_justify('mrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmrazmraz')