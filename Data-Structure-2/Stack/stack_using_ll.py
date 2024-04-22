class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return None

        popped_item = self.top.data
        self.top = self.top.next
        return popped_item
    
stack = Stack()
stack.push(11)
stack.push(22)

print(stack.pop())


