def right_justify(s):
    l =' ' * (70 - len(s) - 1) + s
    print(l)
right_justify('monty')