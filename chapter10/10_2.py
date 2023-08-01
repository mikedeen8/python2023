def cumsum(t):
    c = t
    for i in range(len(t)):
        if i == 0:
            pass
        else:
            c[i] += t[i - 1]
            i += 1
    return c

print(cumsum([1, 2, 3]))