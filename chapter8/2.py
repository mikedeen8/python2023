def names():
    prefixes = 'БВККЛМНШ'
    suffix = 'ряк'
    r = 0
    for letter in prefixes:
        if r == 'Квяк':
            print(letter + suffix)
            r = 0
        elif letter == 'К':
            print(letter + 'вяк')
            r = letter + 'вяк'
        elif letter == 'Л' or letter == 'М' or letter == 'Н':
            print(letter + 'як')
        elif letter == 'Ш':
            print(letter + 'мяк')
        else:
            print(letter + suffix)

names()