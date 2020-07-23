class Stack:

    def __init__(self):
        self.len = 0
        self.stack = []

    def push(self, x):
        self.stack.append(x)
        self.len += 1

    def pop(self):
        try:
            a = self.stack.pop()
            self.len -= 1
        except:
            a = -1
        return a

    def size(self): 
        return self.len
        
        
    def empty(self):
        if self.len:
            return 0
        return 1
        
    def top(self):
        
        if self.empty():
            return -1
        return self.stack[self.len-1]


#----------------------

stack = Stack()

order_N = int(float(input()))

for i in range(order_N):
    order = list(input().split())
    if order[0] == 'push':
        stack.push(int(order[1]))
    
    elif order[0] == 'pop':
        print(stack.pop())
    
    elif order[0] == 'top':
        print(stack.top())
        
    elif order[0] == 'empty':
        print(stack.empty())
    
    else: # 무조건 올바른 명령만 들어오기 때문
        print(stack.size())