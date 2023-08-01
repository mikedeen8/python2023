def cumsum(t):
    for i in range(len(t)):
        if i == 0:
            pass
        else:
            t[i] += t[i - 1]
            i += 1
    return t

print(cumsum([1, 2, 3]))