def is_sorted(t):
    j = 1
    for i in range(len(t) - 1):
        if t[j] < t[j - 1]:
            return False
        j += 1
    return True

print(is_sorted([2, 2, 3]))
print(is_sorted(['a', 'd', 'f']))