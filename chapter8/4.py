def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

def count_1(w, l):
    count = 0
    for letter in w:
        if letter == l:
            count += 1
    print(count)

# count_1('wqpdwhefuehfuehfuheufuhfuhwuefhsi', 'w')

def count_2(w, l):
    c = 0
    count = 0
    for i in range(len(w)):
        # print(c)
        # print(find(w, l, c))
        if find(w, l, c) != -1:
            c = find(w, l ,c) + 1
            count += 1
            # print(count)
    print(count)

count_2('jskjdkejjjfkefjkdj', 'j')