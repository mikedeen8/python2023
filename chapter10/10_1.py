def nested_sum(t):
    c = []
    for i in t:
        c.append(sum(i))
    print(sum(c))

nested_sum([[1, 2], [3, 4, 5], [6, 5, 2]])

def nested_sum_2(t):
    c = []
    f = []
    for i in t:
        if type(i) == int:
            pass
        else:
            for k in i:
                if type(k) == list:
                    # print(i)
                    c.append(nested_sum_2(i))
                else:
                    c.append(k)
                    # print(c)    
    return (sum(c))

def nested_sum_1(t):
    c = []
    for i in t:
        if type(i) == int:
            c.append(i)
    return nested_sum_2(t) + sum(c)

# print(nested_sum_1([[1, 2], [3], 2, [9, [5, 7], 8]]))
# print(nested_sum_1([1, 2, 3, [2], [[[2], 3]]]))
# nested_sum([[1, 2], [[3], [2, 3]], [4, 5, 6]])