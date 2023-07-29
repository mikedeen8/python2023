def uses_all(word, letters):
    for l in letters:
        if not l in word:
            return False
    return True

# print(uses_all('word', 'wrd'))

def words(letters):
    fin = open('python2023/chapter9/words_folder/words.txt')
    line = fin.readline()
    count = 0
    for line in fin:
        word = line.strip()
        if uses_all(word, letters):
            count += 1
            # print(word)
    return count

print(words('aeiou'))
print(words('aeiouy'))