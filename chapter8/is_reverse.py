def is_reverse(word1, word2):
    i = 0
    j = len(word2) - 1
    while j >= 0:
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1
        # print(i)
    return True

print(is_reverse('port', 'trop'))