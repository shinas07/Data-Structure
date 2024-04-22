# # # single linked list    
# # class Node:
# #     def __init__(self,data):
# #         self.data = data
# #         self.next = None

# # class Singlell:
# #     def __init__(self):
# #         self.head = None # Initialize the head of the linked list as None

# #     def append(self,data):

# #         new_data = Node(data)
# #         if self.head is None:
# #             self.head = new_data
# #         else:
# #             current = self.head
# #             while current.next is not None:
# #                 current = current.next
# #             current.next = new_data

# #     def display(self):
# #         current = self.head
# #         while current is not None:
# #             print(current.data)
# #             current.next

# # ll = Singlell
# # ll.append(8)
# # ll.append(99)
# # ll.display()



# #Traversal
# # class Node:
# #     def __init__(self,data):
# #         self.data = data
# #         self.ref = None

# # class LinkedL:
# #     def __init__(self):
# #         self.head = None

# #     def print_li(self):
# #         if self.head is None:
# #             print('Linked list is emplty')
# #         else:
# #             n = self.head
# #             while n is not None:
# #                 print(n.data)
# #                 n = n.ref

# # ll = LinkedL()
# # ll.print_li()

# # addBegin
# # class Node:
# #     def __init__(self,date):
# #         self.data = date
# #         self.ref = None

# # class Linedlist:
# #     def __init__(self):
# #         self.head = None

# #     def printll(self):
# #         if self.head is None:
# #             print('linked list is empty')
# #         else:
# #             n = self.head
# #             while n is not None:
# #                 print(n.data)
# #                 n = n.ref
    
# #     def add_begin(self,data):
# #         new_node = Node(data)
# #         new_node.ref = self.head
# #         self.head = new_node

# # ll = Linedlist()
# # ll.add_begin(100)
# # ll.add_begin(88)
# # ll.printll()


# # #anding to the end
# # class Node:
# #     def __init__(self,data):
# #         self.data = data
# #         self.ref = None

# # class LinkedList:
# #     def __init__(self):
# #         self.head = None
    
# #     def printll(self):
# #         if self.head is None:
# #             print('linked list is empty')
# #         else:
# #             n = self.head
# #             while n is not None:
# #                 print(n.data)
# #                 n = n.ref

# #     def add_begin(self,data):
# #         new_node = Node(data)
# #         new_node.ref = self.head
# #         self.head = new_node

# #     def add_end(self,data):
# #         new_node = Node(data)
# #         if self.head is None:
# #             self.head = new_node
# #         else:
# #             n = self.head
# #             while n.ref is not None:
# #                 n = n.ref
# #             n.ref = new_node

# # ll = LinkedList()
# # ll.add_begin(44)
# # ll.add_begin(33)
# # ll.add_end(88)
# # ll.printll()


# # """
# # adding elements to after the give Node
# # """

# # class Node:
# #     def __init__(self,data):
# #         self.data = data
# #         self.next = None

# # class singlell:
# #     def __init__(self):
# #         self.head = None
    
# #     def adding_to_first(self,data):
# #         new_node = Node(data)
# #         new_node.next = self.head
# #         self.head = new_node
    
# #     def add_in_order(self,data):
# #         new_node = Node(data)
# #         # If the linked list is empty, add the new node as the first node
# #         if self.head is None:
# #             self.head = new_node
# #             return 
        

        
# #         # Traverse the list to find the insertion point
# #         current = self.head
# #         while current.next is not None:
# #             current = current.next

# #         # Add the new node at the end of the list
# #         current.next = new_node

# #     def pirnt_list(self):
# #         current = self.head
# #         while current is not None:
# #             print(current.data)
# #             current = current.next

# #     def add_after(self,data,pos):
# #         n = self.head
# #         while n is not None:
# #             if pos == n.data:
# #                 break
# #             n = n.next

# #         if n is None:
# #             print("Node is empty")
# #         else:
# #             new_node = Node(data)
# #             new_node.next = n.next
# #             n.next = new_node
        

# # ll = singlell()
# # ll.adding_to_first(44)
# # ll.adding_to_first(22)
# # ll.adding_to_first(222)
# # ll.add_after(3,222)
# # ll.pirnt_list()

# # """
# # adding elements to before the give Node

# # """

# # class Node:
# #     def __init__(self,data):
# #         self.data = data
# #         self.next = None

# # class Singlell:
# #     def __init__(self):
# #         self.head = None

# #     def add_to_first(self,data):
# #         new_node = Node(data)
# #         new_node.next = self.head
# #         self.head = new_node

# #     def add_in_order(self,data):
# #         new_node = Node(data)
# #         if self.head is None:
# #             self.head = new_node
# #         else:
# #             current = self.head
# #             while current.next is not None:
# #                 current = current.next
# #             current.next = new_node


# #     def add_to_after(self,data,pos):
# #         n = self.head
# #         while n is not None:
# #             if pos == n.data:
# #                 break
# #             n = n.next

# #         if n is None:
# #             print('No position val')
# #         else:
# #             new_node = Node(data)
# #             new_node.next = n.next
# #             n.next = new_node

# #     def add_to_before(self,data,pos):
# #         if self.head is None:
# #             print('Linked list is empty')
# #             return
# #         if self.head.data == pos:
# #             new_node = Node(data)
# #             new_node.next = self.head
# #             self.head = new_node
# #             return 
# #         n = self.head 
# #         while n.next is not None:
# #             if n.next.data == pos:
# #                 break
# #             n = n.next 
# #         if n.next is None:
# #             print('Node is not found')
# #         else:
# #             new_node = Node(data)         
# #             new_node.next =   n.next
# #             n.next = new_node

# #     def printll(self):
# #         current = self.head
# #         while current is not None:
# #             print(current.data)
# #             current = current.next
        

# # ll = Singlell()
# # ll.add_in_order(333)
# # ll.add_in_order(3)
# # ll.add_to_after(4,3)
# # ll.add_in_order(3)
# # # ll.add_in_order(55)
# # # ll.add_to_first(4)
# # # ll.add_to_first(6)
# # # ll.add_to_before(8999,4)
# # # ll.add_in_order(333)
# # # ll.add_to_after(88,4)
# # ll.printll()
# # # ll.add_in_order(22)


# # removing node

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class singlell:
#     def __init__(self):
#         self.head = None

#     def add_begin(self,data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node


#     def add_end(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node            

#     def delete_end(self):
#         if self.head is None:
#             print("This list is empty. Cannot delete form empty list")
#             return 
#         elif self.head.next is None:
#             self.head = None
#             return 
#         current = self.head 
#         while current.next.next:
#             current = current.next
#         current.next = None

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end = " -> ")
#             current = current.next

#     def delete_begin(self):
#         if self.head is None:
#             print('list is empty')
#             return 
#         self.head = self.head.next

#     def delete_by_data(self,data):
#         if self.head is None:
#             print('List is empty')
#             return
#         while self.head and self.head.data == data:
#             self.head == self.head.next
        
#         prev = None
#         current = self.head

#         while current:
#             if current.data == data:

#                 if prev:
#                     prev.next = current.next
#                 else:
#                     self.head = current.next
#                 current = current.next
#             else:
#                 prev = current
#                 current = current.next



# ll = singlell()
# ll.add_begin(88)
# ll.add_begin(33)
# ll.add_end(2)
# ll.add_end(8)
# ll.add_end(34)
# ll.delete_by_data(34)
# ll.display()


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def add_at_begnning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Previous node must be valid.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node


    def display(self):
        current = self.head
        while current:
            print(current.data,end=" --> ")
            current = current.next
        print()

ll = SingleLinkedList()
ll.add_at_end(22)
ll.add_at_begnning(28)
ll.add_at_begnning(3)
ll.add_at_end(88)
ll.insert_after(22,99)
ll.display()
            
