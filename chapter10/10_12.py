def words():
    t = []
    fin = open('python2023/chapter10/words_folder/words.txt')
    line = fin.readline()
    for line in fin:
        word = line.strip()
        t += [word]
    return t

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

def word_par(t):
    for w in t:
        l = 0
        c = ''
        p = ''
        for i in w:
            if l % 2 == 0:
                c += i
            else:
                p += i
            l += 1
        if in_bisect(t, c) and in_bisect(t, p):
            print(c, p, w)

# word_par(words())

def word_trio(s):
    for w in s:
        l = 0
        c = ''
        p = ''
        f = ''
        for i in w:
            if l % 3 == 0:
                c += i
            elif l % 3 == 1:
                p += i
            else:
                f += i
            l += 1
        if in_bisect(s, c) and in_bisect(s, p) and in_bisect(s, f):
            print(c, p, f, w)
        
word_trio(words())