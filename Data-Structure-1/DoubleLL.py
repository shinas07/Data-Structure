# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.prev = None
#         self.next = None

# class DoubleLL:
#     def __init__(self):
#         self.head = None

#     def add_begin(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node

#     def add_end(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current:
#                 current = current.next
#             current.next = new_node
#             new_node.prev = current

            
#     def display_to_forward(self):
#         if self.head is None:
#             print('Linkedlist is empty')
#             return
#         current = self.head
#         while current:
#             print(current.data,end="-->")
#             current = current.next

#     def display_to_reverse(self):
#         if self.head is None:
#             print('Linkedlist list is empty')
#         else:
#             current = current.next 
#             while current.next is not None:
#                 current = current.next
#             while current is not None:
#                 print(current.data,end="-->")
#                 current = current.prev

# dll = DoubleLL()
# dll.add_end(8)
# dll.add_end(333)
# dll.display_to_forward()
# dll.display_to_reverse()



# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class Doublell:
#     def __init__(self):
#         self.head = None


#     def add_begin(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             if self.head:
#                 self.head.prev = new_node
#             self.head = new_node

#     def add_end(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
#             new_node.prev = current
    


#     def display_at_forword(self):
#         if self.head is None:
#             print('list is empty')
#         else:
#             current = self.head
#             while current:
#                 print(current.data)
#                 current = current.next

#     def add_after(self,data,x):
#         if self.head is None:
#             print('List is empty!')
#         else:
#             current = self.head 
#             while current is not None:
#                 if x == current.data:
#                     break
#                 current = current.next
#         if current is None:
#             print('given Node is not present in dll')
#         else:
#              new_node = Node(data)
#              new_node.next = current.next
#              new_node.next = current
#              if current.next is not None:
#                  current.next = new_node
#              current.next =new_node


#     def delete_from_begin(self):
#         if self.head is None:
#             print('list is empty')
#         elif self.head.next is None:
#             self.head = None
#             return
#         self.head = self.head.next
#         self.head.prev = None


#     def delete_from_end(self):
#         if self.head is None:
#             print('list is empty')
#         elif self.head.next is None:
#             self.head = None
#             return
#         current = self.head
#         while current.next is not None:
#             current = current.next
#         current.prev.next = None

#     def delete_by_value(self,value):
#         if self.head is None:
#             print('Linked list is empty')
#             return 
        
#         if self.head.data == value:
#             self.head = self.head.next
#             return
        
#         current = self.head
#         while current.next is not None:
#             if current.next.data == value:
#                 current.next = current.next.next
#                 return 
#             current = current.next


    # def add_before(self,key,data):
    #     new_node = Node(data)
    #     if self.head is None:
    #         print('List is empty')
    #     elif self.head.data == key:
    #         new_node.next = self.head
    #         self.head.prev = new_node
    #         self.head = new_node
    #     else:
    #         current = self.head
    #         while current:
    #             if current.data == key:
    #                 new_node.next = current
    #                 new_node.prev = current.prev
    #                 current.prev.next = new_node
    #                 current.prev = new_node
    #                 return 
    #             current = current.next
    #         print("Key not found in the list")

# dll = Doublell()
# dll.add_begin(88)
# dll.add_begin(33)
# dll.add_begin(333)
# dll.add_begin(999)
# dll.delete_by_value(88)
# dll.display_at_forword()


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class Doublell:
#     def __init__(self):
#         self.head = None

#     def append(self,data)
