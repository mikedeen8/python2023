def do_twice(f, g):
    f(g)
    f(g)
def print_spam(g):
    print(g)

# do_twice(print_spam, 'спам')

def print_twice(b):
    print(b)
    print(b)
do_twice(print_twice, 'спам')

def do_four(a, b):
    do_twice(a, b)
do_four(print_twice, 'спам')