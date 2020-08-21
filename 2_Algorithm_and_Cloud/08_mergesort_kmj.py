# https://www.acmicpc.net/problem/2751
# 못 함 --> solution 설명 후 pass함


def combine(num_list, start_idx, mid_idx, end_idx):
    
    l_idx = start_idx
    r_idx = mid_idx + 1
    sorted_list = []

    while l_idx <= mid_idx and r_idx <= end_idx:
        if num_list[l_idx] < num_list[r_idx]:
            min_value = num_list[l_idx]
            l_idx += 1
        else: 
            min_value = num_list[r_idx]
            r_idx += 1
        
        sorted_list.append(min_value)
    

    # if l_idx <= mid_idx :
    #     sorted_list += num_list[l_idx:mid_idx+1]
    # else:
    #     sorted_list += num_list[r_idx:end_idx+1]    
    sorted_list += num_list[r_idx:end_idx+1]
    sorted_list += num_list[l_idx:mid_idx+1]

    num_list[start_idx:end_idx+1] = sorted_list




def mergesort(num_list, start_idx, end_idx):
    
    if start_idx < end_idx:    

        mid_idx = (start_idx + end_idx) // 2 
        
        mergesort(num_list, start_idx, mid_idx)
        mergesort(num_list, mid_idx+1, end_idx)
        
        combine(num_list, start_idx, mid_idx, end_idx)
        # print(num_list)


n = int(input())

num_list_for_sort = []
for _ in range(n):
    num_list_for_sort.append(int(input()))


mergesort(num_list_for_sort, 0, n-1)
print(num_list_for_sort)