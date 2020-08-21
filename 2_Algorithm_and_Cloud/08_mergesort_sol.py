# https://www.acmicpc.net/problem/2751
# 분할 정복법 : divide + conquer, combine

# top-down sol과 동일


def combine(num_list, start_idx, mid_idx, end_idx):
    l_idx = start_idx # start_idx ... mid_idx (포함)
    r_idx = mid_idx+1 # mid_idx+1 ... end_idx

    sorted_list = []
    
    while l_idx <= mid_idx and r_idx <= end_idx:    
        if num_list[l_idx] < num_list[r_idx]:
            min_val = num_list[l_idx]
            l_idx += 1
        else:
            min_val = num_list[r_idx]
            r_idx += 1

        sorted_list.append(min_val)

    if l_idx <= mid_idx: # start_idx ... mide_idx 부분에 정렬된 원소들이 남아 있음
        sorted_list += num_list[l_idx:mid_idx+1]
    else: 
        sorted_list += num_list[r_idx:end_idx+1]

    num_list[start_idx:end_idx+1] = sorted_list




def merge_sort(num_list, start_idx, end_idx):
    if start_idx < end_idx:
        mid_idx = (start_idx + end_idx) // 2
        
        merge_sort(num_list, start_idx, mid_idx)
        merge_sort(num_list, mid_idx+1, end_idx)

        combine(num_list, start_idx, mid_idx, end_idx)
    

    # return None이 생략 된 것 



n = int(input())
num_list = []

for _ in range(n):
    num_list.append(int(input()))
    
merge_sort(num_list, 0, len(num_list)-1)
print(num_list)
    
