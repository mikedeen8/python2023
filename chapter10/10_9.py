def words_1():
    t = []
    fin = open('python2023/chapter10/words_folder/words.txt')
    line = fin.readline()
    for line in fin:
        word = line.strip()
        t.append(word)
    return t

print(words_1())

def words_2():
    t = []
    fin = open('python2023/chapter10/words_folder/words.txt')
    line = fin.readline()
    for line in fin:
        word = line.strip()
        t += [word]
    return t

print(words_2())