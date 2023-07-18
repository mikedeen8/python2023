def recurse(n, s): #n >= 0; s - anyone
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)

recurse(3, 0)