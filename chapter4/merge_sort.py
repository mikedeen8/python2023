def merge_sort(a):
    p = len(a) // 2
    c = a[:p]
    d = a[p:]
    if p == 1:
        return a
    merge_sort(c)

arr = [10, 4, 5, 3, 6, 9, 2, 7, 1, 0, 8]
n = len(arr)
print(merge_sort(arr))
# print(arr[:3])