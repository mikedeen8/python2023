def any_lowercase(s):
    count = 0
    for c in s:
        if c.islower():
            count += 1
    if count == len(s):
        return True
    else:
        return False
    
print(any_lowercase('fjijfiwejferufuvfufn'))