def uses_only(word, letters):
    for l in word:
        if l == ' ' or l == '.' or l == ','or l == '?' or l == '!':
            pass
        elif not l.upper() in letters and not l.lower() in letters:
            return False
    return True

print(uses_only('wasdwd', 'wasdvcf'))
# print(uses_only('Hello, fecal hole!', 'acefhlo'))         # :)