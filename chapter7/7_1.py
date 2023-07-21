import math

def mysqrt(a):
    x = 2
    while True:
        # print(x)
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return float(x)

# mysqrt(4)
def test_square_root():
    print('a', ' ' * 4, 'mysqrt(a)', ' ' * 4, 'math.sqrt(a)', ' ' * 4, 'diff')
    print('-', ' ' * 4, '-' * 9, ' ' * 4, '-' * 12, ' ' * 4, '-' * 4)
    for i in range(9):
        i += 1.0
        if i == 5:
            print(i, ' ' * 2, round(mysqrt(i), 11), ' ', round(math.sqrt(i), 10), ' ' * 4, abs(math.sqrt(i) - mysqrt(i)))    
        elif len(str(mysqrt(i))) < 10 or len(str(math.sqrt(i))) < 10:
            print(i, ' ' * 2, round(mysqrt(i), 11), ' ' * (13 - len(str(math.sqrt(i)))) , round(math.sqrt(i), 10), ' ' * (16 - len(str(math.sqrt(i)))), abs(math.sqrt(i) - mysqrt(i)))
        else:
            print(i, ' ' * 2, round(mysqrt(i), 11), '', round(math.sqrt(i), 10), ' ' * 4, abs(math.sqrt(i) - mysqrt(i)))

test_square_root()