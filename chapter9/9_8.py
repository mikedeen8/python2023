def is_palindrome(s):
    return True if s == s[::-1] else False


def odometr():
    i = 99999
    for c in range(999999):
        i += 1
        if is_palindrome(str(i)[2:]) and is_palindrome(str(i + 1)[1:]) and is_palindrome(str(i + 2)[1:5]) and is_palindrome(str(i + 3)):
            print(i)

odometr()
