def bubble_sort(a, n):
    for m in range(n - 1):
        for i in range(n - 1 - m):
            if a[i] > a[i+1]:
                tmp = a[i]
                a[i] = a[i+1]
                a[i+1] = tmp
        print("iteration: ", m, " array: ", a)
    print(a)
    
    
    
arr = [10, 4, 5, 3, 6, 9, 2, 7, 1, 0, 8]
n = len(arr)
bubble_sort(arr, n)
