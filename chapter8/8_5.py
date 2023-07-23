def rotate_word(s, r):
    w = ''
    for l in s:
        b = ord(l) + r
        if 65 <= ord(l) <= 90:
            if 65 <= ord(l) + r <= 90:
                b = chr(ord(l) + r)
            else:
                while b < 65 or b > 90:
                    if r >= 0:
                        b -= 26
                    else:
                        b += 26
                b = chr(b)
        elif 97 <= ord(l) <= 122:
            if 97 <= ord(l) + r <= 122:
                b = chr(ord(l) + r)
            else:
                while b < 97 or b > 122:
                    if r >= 0:
                        b -= 26
                    else:
                        b += 26
                b = chr(b)
        elif 1040 <= ord(l) <= 1072:
            if 1040 <= ord(l) + r <= 1072:
                b = chr(ord(l) + r)
            else:
                while b < 1040 or b > 1072:
                    if r >= 0:
                        b -= 33
                    else:
                        b += 33
                b = chr(b)
        elif 1072 <= ord(l) <= 1104:
            if 1072 <= ord(l) + r <= 1104:
                b = chr(ord(l) + r)
            else:
                while b < 1072 or b > 1104:
                    if r >= 0:
                        b -= 33
                    else:
                        b += 33
                b = chr(b)
        else:
            b = l
        w += b
    return w

print(rotate_word('A', 16))