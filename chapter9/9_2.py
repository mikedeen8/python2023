def has_no_e(word):
    if 'e' in word or 'E' in word:
        return False
    else:
        return True

# print(has_no_e('baker'))

def words():
    count = 0
    n = 0
    fin = open('python2023/chapter9/words_folder/words.txt')
    line = fin.readline()
    for line in fin:
        word = line.strip()
        if has_no_e(word):
            # print(word)
            count += 1
        else:
            n += 1
        a = str((count / (n + count)) * 100) + '%'
    return a

print(words())