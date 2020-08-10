# https://www.acmicpc.net/problem/1920
# pass

# 슬라이싱으로 접근하면 O(N)이 돼서 linear search와 같아짐
# → 배열을 그대로 두고 인덱스로 보는 위치만 변경하기
def search_idx(target_num, num_list, start_idx, end_idx):
    mid_idx = int((end_idx + start_idx)/2) # --(start_idx + end_idx) // 2와 동일

    if start_idx > end_idx:
        return -1
    
    if num_list[mid_idx] == target_num:
        return mid_idx
    
    elif num_list[mid_idx] < target_num:
        return search_idx(target_num, num_list, mid_idx+1, end_idx)

    elif num_list[mid_idx] > target_num:
        return search_idx(target_num, num_list, start_idx, mid_idx-1)
    
    
    

n = int(input())
fixed_list = list(map(int, input().split()))
fixed_list.sort()

m = int(input())
compare_list = list(map(int, input().split()))

for num in compare_list:
    if search_idx(num, fixed_list, 0, len(fixed_list)-1) >= 0:
        print("1")
    else:
        print("0")
