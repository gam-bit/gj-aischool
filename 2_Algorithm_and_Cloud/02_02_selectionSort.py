def selectionSort(N, array):
    for i in range(N):
        
        min_idx = i
        for j in range(i, N):
            if array[min_idx] > array[j]:
                min_idx = j
        
        array[i], array[min_idx] = array[min_idx], array[i]
        print(array)
    return array


n = int(input())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)

print("---Sort 후---")
for i in selectionSort(n, arr):
    print(i)