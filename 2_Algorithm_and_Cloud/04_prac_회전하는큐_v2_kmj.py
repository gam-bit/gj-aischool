# 못 풀었음 -> 다시 풀어보고 pass
from collections import deque

n, m = map(int, input().split())
target_list = map(int, input().split())

c_queue = deque([i for i in range(1, n+1)])
    

result = 0
for target in target_list:
    move_size = c_queue.index(target) # pull
    if len(c_queue) - move_size < move_size: # push < pull
        move_size = -(len(c_queue) - move_size)
    c_queue.rotate(-move_size)
    result += abs(move_size)
    c_queue.popleft()

print(result)

