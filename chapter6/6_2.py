def ack(m, n):
    if not isinstance(m, int):
        print('m должно быть целым числом')
        return
    elif not isinstance(n, int):
        print('n должно быть целым числом')
        return
    elif m < 0 and n < 0:
        print('И m, и n должны быть больше нуля')
    elif m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))
    
print(ack(3, 4))