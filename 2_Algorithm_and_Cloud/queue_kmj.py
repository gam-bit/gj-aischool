class Queue:

    
    def __init__(self):
        self.len = 0
        self.queue = []
        
    
    def push(self, x):
        self.queue += [x]
        self.len += 1 

    def pop(self):
        
        a = self.front()
        if a == -1:
            return a
        self.queue = self.queue[1:]
        self.len -= 1
        return a
        

    def size(self):   
        return self.len

    def empty(self):
        if self.len:
            return 0
        return 1


    def front(self):
        try:
            return self.queue[0]
        except:
            return -1

    def back(self):
        try:
            return self.queue[self.len-1]
        except:
            return -1

q = Queue()

order_N = int(float(input()))
for i in range(order_N):
    order = list(input().split())
    
    if order[0] == 'push':
        q.push(int(order[1]))
    elif order[0] == 'pop':
        print(q.pop())
    elif order[0] == 'size':
        print(q.size())
    elif order[0] == 'empty':
        print(q.empty())
    elif order[0] == 'front':
        print(q.front())
    else:
        print(q.back())