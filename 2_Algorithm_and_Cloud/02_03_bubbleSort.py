def bubbleSort(N, array):
    swap = 0
    
    for i in range(len(array)):
        
        for j in range(n-i-1):
            
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swap += 1
            
        if swap == 0:
            break
    
        print(array)
    return array



n = int(input())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)

print("---Sort 후---")
for i in bubbleSort(n, arr):
    print(i)
         
            