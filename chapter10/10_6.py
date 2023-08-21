def is_anagram(s, p):
    t = list(s)
    f = list(p)
    for i in t:
        if not i in f:
            return
        else:
            t.remove(i)
            f.remove(i)
    return True

print(is_anagram('sevc', 'evcs'))