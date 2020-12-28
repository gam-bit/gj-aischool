def quicksort(lst):
    
    n = len(lst) 

    if n <= 1:
        return lst

    pivot_lst = [lst[0], lst[n//2], lst[n-1]]
    pivot = sum(pivot_lst) - min(pivot_lst) - max(pivot_lst)

    less_lst = []
    equal_lst = []
    more_lst = []

    for v in lst:
        if v > pivot:
            more_lst.append(v)
        elif v < pivot:
            less_lst.append(v)
        else:
            equal_lst.append(v)

    print(f"less: {less_lst}, equsl: {equal_lst}, more: {more_lst}")
    return quicksort(less_lst) + equal_lst + quicksort(more_lst)





l = [3,7,5,4,2,6,1]

print(quicksort(l))
