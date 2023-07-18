def is_power(a, b):
    if a == b or a % b == 0 and is_power(a / b, b):
        return True
    elif b == 0 or b == 1:
        return False
    else:
        return False
    
print(is_power(27, 3))

'''
Следующую функцию не обязателно было делать, но я решил сделать так, чтобы онв показывала,
в какую степень нужно возвести число b, чтобы оно стало числом a (третий аргумент - это счётчик.
!При вызове функции счётчик должен равнятся нулю, иначе функция будет работать некорректно!).

'''
def is_power_2(a, b, c):
    if a == b:
        v = c
        print('Число a является числом b в', v + 1, 'степени.')
        return True
    elif a % b == 0 and is_power_2(a / b, b, c + 1):
        return True
    elif b == 0 or b == 1:
        return False
    else:
        return False

# print(is_power_2(27, 3, 0))