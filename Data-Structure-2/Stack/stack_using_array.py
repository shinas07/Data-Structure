class Stack:
    def __init__(self, max_size):
        self.stack = [None] * max_size
        self.max_size = max_size
        self.top = -1

    def push(self, item):
        if self.is_full():
            print('Stack Overflow')
            return
        
        self.top +=  1
        self.stack[self.top] = item

    def pop(self):
        if self.is_empty():
            print('Stack Underflow')
            return None
        
        popped_itme = self.stack[self.top]
        self.top = -1
        return popped_itme
    
    def top_element(self):
        if self.is_empty():
            return None
        return self.stack[self.top]
    
    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.max_size - 1
    



stack = Stack(5)
stack.push(4)
stack.push(99)

print(stack.top_element())
print(stack.pop())