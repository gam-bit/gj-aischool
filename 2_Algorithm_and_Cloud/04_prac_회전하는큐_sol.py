from collections import deque

n, m = map(int, input().split())
target_list = map(int, input().split()) # m개


q_list = deque([i for i in range(1, n+1)])
 # deque([1, 2, 3, 4, 5, ..., n-1, n])

result = 0

for target_num in target_list:
    movement_size = q_list.index(target_num)

    if movement_size > len(q_list) - movement_size:
        movement_size = -(len(q_list) - movement_size) # movement_size -= len(q_list)
    
    result += abs(movement_size)
    q_list.rotate(-movement_size)

    q_list.popleft()

print(result)


    