# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class Circularll:
#     def __init__(self):
#         self.head = None

#     def append(self,data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             new_node.next = self.head
#             return
        
#         current = self.head
#         while current:
#             current =  current.next
#         current.next = new_node
#         new_node = self.head

#     def prepend(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         current = self.head
#         if current:
#             while current.next != self.head:
#                 current = current.next
#             current.next = new_node
#         else:
#             new_node.self = new_node
#         self.head = new_node


#     def delete(self, data):
#         if not self.head:
#             return 
#         if self.head.data = key