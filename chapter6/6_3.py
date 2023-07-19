def first(word):
    return word[0]

def middle(word):
    return word[1:-1]

def last(word):
    return word[-1]

def is_palindrome(str):
    if len(str) <= 1 or (first(str) == last(str) and is_palindrome(middle(str))):
        return True
    else:
        return False
print(is_palindrome('asddsa'))