# class stack:

#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if not self.items is None:
#             popitem = self.items[-1]
#             self.items.pop()
#             return popitem
#         else:
#             raise IndexError('Stack is empty')
        
#     def peek(self):
#         if not self.items is None:
#             return self.items[-1]
#         else:
#             raise IndexError('Stack is empty')
        
# string = 'shians'
# stack = stack()
# for c in string:
#     stack.push(c)

# reversed_string = ""
# for i in range(len(string)):
#     popitem = stack.pop()
#     reversed_string += popitem

# print(reversed_string).


# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, items):
#         self.items.append(items)

#     def pop(self):
#         if not self is None:
#             return self.items.pop()
#         else:
#             print('Stack is empty')
#             return None
        
#     def peek(self):
#         if not self.items is None:
#             return self.items[-1]
#         else:
#             print('Stack is empty')
#             return None
        
#     def size(self):
#         return len(self.items)
    

# def reverse_string(input_string):
#     stack = Stack()
#     for char in input_string:
#         stack.push(char)

#     reverse_string = ""
#     while stack:
#         reverse_string += stack.pop()

#     return reverse_string


# input_string = "Shinas"
# reverse_string = reverse_string(input_string)
# print(reverse_string)

# stack = Stack()
# stack.peek()



def rever_string(s):
    stack = []

    for char in s:
        stack.append(char)

    rever_string = ""
    while stack:
        rever_string += stack.pop()
    
    return rever_string



string = 'shians'
print(rever_string(string))