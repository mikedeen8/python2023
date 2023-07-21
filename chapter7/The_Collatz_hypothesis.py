def sequence(m):
    while True:
        if m == 1:
            return 'Это работает'
        if m % 2 == 0:
            m = m / 2
        else:
            m = m * 3 + 1

def Collatz():
    m = 0
    for m in range(100000):
        m += 1
        d = int(str(m)[-1])
        if m == 12 or m == 13 or m == 14:
            print(sequence(m), m, 'раз!')
        elif d == 2 or d == 3 or d == 4:
            print(sequence(m), m, 'раза!')
        else:
            print(sequence(m), m, 'раз!')
    print('Неворятно! Походу это работает m раз!')


Collatz()