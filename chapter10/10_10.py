def words():
    t = []
    fin = open('python2023/chapter10/words_folder/words.txt')
    line = fin.readline()
    for line in fin:
        word = line.strip()
        t += [word]
    return t
        
# print(words())

def in_bisect(t, w):
    i = len(t) // 2
    if len(t) == 0:
        return
    if t[i] == w:
        return i
    elif t[i] > w:
        t = t[:i]
        return in_bisect(t, w)
    elif t[i] < w:
        t = t[i + 1:]
        if in_bisect(t, w) == None:
            return
        return in_bisect(t, w) + i + 1

print(in_bisect(words(), 'chief'))