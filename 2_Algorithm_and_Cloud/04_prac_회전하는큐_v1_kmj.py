# 못 풀었음 -> 다시 풀어보고 pass
from collections import deque

n, m = map(int, input().split())
target_list = map(int, input().split())

c_queue = deque([i for i in range(1, n+1)])
    

result = 0
for target in target_list:
    pull_size = c_queue.index(target)
    push_size = len(c_queue) - pull_size
    if push_size > pull_size:
        mov_size = -pull_size
    else:
        mov_size = push_size
    c_queue.rotate(mov_size)
    result += abs(mov_size)
    c_queue.popleft()

print(result)

