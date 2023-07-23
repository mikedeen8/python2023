def has_no_letter(word, letter):
    for l in letter:
        if l.lower() in word or l.upper() in word:
            return False
    return True

# print(has_no_letter('baker', 'sgze'))

def words():
    letter = str(input('Введите строку запрещённых букв: \n'))
    count = 0
    n = 0
    fin = open('python2023/chapter9/words_folder/words.txt')
    line = fin.readline()
    for line in fin:
        word = line.strip()
        if has_no_letter(word, letter):
            count += 1
    return count
#Мне кажется, наименьшее количество слов исключает сочетание из букв: q, w, z, x и j.

print(words())