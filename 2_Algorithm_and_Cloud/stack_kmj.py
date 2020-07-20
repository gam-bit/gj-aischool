def push(x):
    stack.append(x)

def pop():
    try:
        a = stack.pop()
    except:
        a = -1
    return a

def size(): 
    n = 0
    for i in stack:
        n += 1
    return n
    
    
def empty():
    if size() == 0:
        return 1
    return 0
    
def top():
    
    if empty():
        return -1
    return stack[size()-1]


#----------------------
order_N = int(float(input()))
stack = []

for i in range(order_N):
    order = input('명령을 입력하세요: ')
    if 'push' in order:
        push(int(order.replace('push ', '')))
    
    elif order == 'pop':
        print(pop())
    
    elif order == 'top':
        print(top())
        
    elif order == 'empty':
        print(empty())
    
    else: # 무조건 올바른 명령만 들어오기 때문
        print(size())