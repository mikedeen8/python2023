def has_duplicates(t):
    p = 0
    for i in range(len(t) - 1):
        g = 0
        for i in range(len(t) - 1):
            if t[p] == t[g] and p != g:
                return True
            g += 1
        p += 1

print(has_duplicates(['a', 'b', 'a', 'v']))