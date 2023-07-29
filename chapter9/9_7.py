def trio(word):
    for i in range(len(word) - 1):
        if i + 5 > len(word) - 1:
            return False
        elif word[i] == word[i + 1] and word[i + 2] == word[i + 3] and word[i + 4] == word[i + 5]:
            return word
    return False

# print(trio('ccvvbb'))

def words():
    fin = open('python2023/chapter9/words_folder/words.txt')
    line = fin.readline()
    for line in fin:
        word = line.strip()
        if trio(word):
            return trio(word)
        
print(words())