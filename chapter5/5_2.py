def check_fermat(a, b, c, n):
    if n > 2 and (a ** n) + (b ** n) == c ** n:
        print('Не может быть, Ферма ошибся!')
    else:
        print('Нет, это не работает.')

def input_fermat():
    a = int(input('Введите число a: \n'))
    b = int(input('Введите число b: \n'))
    c = int(input('Введите число c: \n'))
    n = int(input('Введите степень n: \n'))    
    check_fermat(a, b, c, n)

input_fermat()