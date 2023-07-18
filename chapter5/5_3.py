def is_triangle(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        print('Да')
    else:
        print('Нет')

def input_is_triangle():
    a = int(input('Введите сторону a: \n'))
    b = int(input('Введите сторону b: \n'))
    c = int(input('Введите сторону c: \n'))
    is_triangle(a, b, c)

input_is_triangle()