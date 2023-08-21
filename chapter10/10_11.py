def words():
    t = []
    fin = open('python2023/chapter10/words_folder/words.txt')
    line = fin.readline()
    for line in fin:
        word = line.strip()
        t += [word]
    return t

def is_palindrome(s):
    return True if s == s[::-1] else False

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
    
def par(t):
    for w in t:
        l = w[::-1]
        if type(in_bisect(t, l)) == int and in_bisect(t, l) + 1 and not is_palindrome(w):
        # if l in t:
            print(w, l)
    
par(words())