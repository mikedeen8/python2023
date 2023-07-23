def uses_only(word, letters):
    for l in letters:
        if l == ' ' or l == '.' or l == ','or l == '?' or l == '!':
            pass
        elif not l.upper() in word and not l.lower() in word:
            return False
    for c in word:
        if c == ' ' or c == '.' or c == ',' or c == '?' or c == '!':
            pass
        elif not c.upper() in letters and not c.lower() in letters:
            return False
    return True

print(uses_only('wasdwvc', 'wasdvc'))
# print(uses_only('Hello, fecal hole!', 'acefhlo'))         # :)