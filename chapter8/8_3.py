def is_palindrome(s):
    return True if s == s[::-1] else False

print(is_palindrome('qwedfgnvu'))