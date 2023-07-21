def eval_loop():
    while True:
        a = str(input())
        c = 'готово'
        if a == c:
            break
        b = eval(a)
        print(b)
    return b

print(eval_loop())