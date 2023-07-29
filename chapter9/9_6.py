def is_abecedarian(word):
    for i in range(len(word) - 1):
        if ord(word[i].lower()) != ord(word[i + 1].lower()) - 1 and ord(word[i].lower())!= ord(word[i + 1].lower()):
            return False
        i += 1
    return True

# print(is_abecedarian('abbcD'))

def words():
    fin = open('python2023/chapter9/words_folder/words.txt')
    line = fin.readline()
    count = 0
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            # print(word)
            count += 1
    return count

print(words())