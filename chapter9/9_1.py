def words():
    fin = open('python2023/chapter9/words_folder/words.txt')
    line = fin.readline()
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)