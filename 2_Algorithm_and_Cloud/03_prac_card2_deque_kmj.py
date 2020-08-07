## pass

# import sys
# input = sys.stdin.readline
from collections import deque

class Queue:
    def __init__(self, length):
        self.array_list = deque()
    
    def push(self, value):
        self.array_list.append(value)
    
    def pop(self):
        if self.size() > 0:
            return self.array_list.popleft()
        
        return -1

        # try:
        #     return self.array_list.popleft()
        # except IndexError:
        #     return -1
    
    def size(self):
        return len(self.array_list)
    
    def empty(self):
        # return int(self.size() <= 0)
        if self.size() > 0:
            return 0
        
        return 1
    
    def front(self):
        if self.size() > 0:
            return self.array_list[0]
        
        return -1

    def back(self):
        if self.size() > 0:
            return self.array_list[self.size()-1]
        
        return -1

    def rotate(self, k):
        return self.array_list.rotate(k)



n = int(input())
queue_list = Queue(length=n)

i = 1
while queue_list.size() != n:
    queue_list.push(i)
    i += 1

while queue_list.size() != 1: 
    queue_list.pop()
    queue_list.rotate(-1)
    
    
print(queue_list.front())
