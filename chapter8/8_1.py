a = 'qwerty'
# print(a.strip('q'))
# print(a.replace('y', a))
def s_replace(a, y):
    if len(a) > 100:
        return a
    else:
        a = a.replace(y, a)
        #print(a)
        return s_replace(a, y)

# print(s_replace('qwerty', 'y'))