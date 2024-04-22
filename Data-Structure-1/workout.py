# #single liked list
# class Node:
#     """
#         Initialize a node with the given data.
#     """
#     def __init__(self,data):
#         self.data = data
#         self.next = None


# class SingleLinkedList:
#     def __init__(self):
#         """
#         Initialize an empty singly linked list.
#         """
#         self.head = None

#     def add_at_beginning(self,data):

#         new_node = Node(data)
#         new_node.next = self.head  # Set the next pointer of the new node to the current head
#         self.head = new_node  # Update the head pointer to point to the new node

#     def add_at_end(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             last_node = self.head
#             while last_node.next:
#                 last_node = last_node.next
#             last_node.next = new_node # Set the next pointer of the last node to the new node

#     def print_list(self):
#         current = self.head
#         while current:
#             print(current.data)
#             current = current.next
#         print()

# ll = SingleLinkedList()

# ll.add_at_end(7)
# ll.add_at_beginning(9)
# ll.add_at_beginning(8)

# ll.print_list()


# #Single linked list for traversal
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.ref = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def print_Ll(self):
#         if self.head is None:
#             print('linked list is empty')
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref

# LL = LinkedList()
# LL.print_Ll()


# class Node:
#     def __init__(self,date):
#         self.data = date
#         self.ref = None

# class Linkedlist:
#     def __init__(self):
#         self.head = None

#     def printll(self):
#         if self.head is None:
#             print('linked list is empty')
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref

#     def add_begin(self,data):
#         new_node = Node(data)
#         new_node.ref = self.head
#         self.head = new_node

# ll = Linkedlist()
# ll.add_begin(400)
# ll.add_begin(33)
# ll.add_begin(55)
# ll.printll()


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.ref = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def print_ll(self):
#         if self.head is None:
#             print('list is empty')
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref
    
#     def add_begin(self,date):
#         new_node = Node(date)
#         new_node.ref = self.head
#         self.head = new_node

# ll = LinkedList()
# ll.add_begin(3)
# ll.add_begin(88)
# ll.print_ll()

#add to end

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.ref = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def printll(self):
#         if self.head is None:
#             print('linked list is empty')
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref

#     def add_begin(self,data):
#         new_node = Node(data)
#         new_node.ref = self.head
#         self.head = new_node

#     def add_end(self,data):
#         new_data = Node(data)
#         if self.head is None:
#             self.head = new_data
#         else:
#             n = self.head
#             while n.ref is not None:
#                 n = n.ref
#             n.ref = new_data

# ll1 = LinkedList()
# ll1.add_end(77)
# ll1.add_begin(88)
# ll1.add_end(9)
# ll1.add_begin(7)
# ll1.printll()

# class Node:
#     def __init__(self,data):
#         self.data =  data
#         self.next = None

#  singly linked list with a head pointer pointing to None.nitialize an empty
# class Singlell:
#     def __init__(self):
#         self.head = None

#     def insert_at_beginning(self,data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
    
#     def insert_at_end(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node

#     def insert_at_position(self,position,data):
#         if position < 0:
#             print('Invalid position')
#             return
        
#         if position == 0:
#             self.insert_at_beginning(data)
#             return
        
#         new_node = Node(data)
#         current = self.head
#         for _ in range(position - 1):
#             if current is None:


#adding elment in any position
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class Singlell:
#     def __init__(self):
#         self.head = None

#     def insert_at_firts(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next is not None:
#                 current = current.next
#             current.next = new_node

#     def insert_at_end(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return 
#         else:
#             current = self.head
#             while current.next is not None:
#                 current = current.next
#             current.next = new_node

#     def insert_at_position(self,data,pos):
#         n = self.head
#         while n is not None:
#             if pos==n.data:
#                 break
#             n = n.next
#         if n is None:
#             print('node is not present in ll')
#         else:
#             new_node = Node(data)
#             new_node.next = n.next
#             n.next = new_node


#     def display(self):
#         if self.head is None:
#             print('Lined list is empty')
#         else:
#             current = self.head
#             while current is not None:
#                 print(current.data)
#                 current = current.next 
        
    
# ll = Singlell()
# ll.insert_at_firts(44)
# ll.insert_at_position(77,44)
# ll.insert_at_firts(9)
# ll.display()

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node

#     def add_to_first(self,data):
#         new_node =Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node

#     def add_to_before(self,data,pos):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
        
#         current = self.head
#         for _ in range(pos-1):
#             if current.next is None:
#                 print('empty')
#                 return
#             current = current.next
#         new_node.next = current.next
#         current.next = new_node



#     def display(self):
#         current = self.head
#         while current:
#             print(current.data)
#             current = current.next

# ll = LinkedList()
# ll.append(88)
# ll.append(44)
# ll.append(222)
# ll.display()


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class singlell:
#     def __init__(self):
#         self.head = None

#     def append(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return 
#         current = self.head
#         while current.next is not None:
#             current = current.next
#         current.next = new_node

#     def add_after(self,data,pos):
#         n = self.head
#         while n is not None:
#             if pos == n.data:
#                 break
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data,end='->')
#             current = current.next
#         print()


# ll = singlell()
# ll.append(8)
# ll.append(7)
# ll.display()


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class linkedlist:
#     def __init__(self):
#         self.head = None

#     def add_to_first(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node

#     def add_to_end(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node

#     def append(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node

    # def delete_by_value(self,value):
    #     current = self.head
    #     if current is not None and current.data == value:
    #         self.head = current.next 
    #         return
        
    #     while current:
    #         if current.data == value:
    #             break
    #         prev = current
    #         current = current.next
        
    #     prev.next = current.next

#     def display(self):
#         if self.head is None:
#             print('linked list is empty')
#         current = self.head
#         while current:
#             print(current.data,end="--> ")
#             current = current.next
#         print()

# ll = linkedlist()
# ll.add_to_end(786)
# ll.add_to_first(44)
# ll.add_to_first(333)
# ll.delete_by_value(44)
# ll.add_to_end(882)
# ll.append(8)
# ll.display()



# class Node:
#     def __init__(self,data):
#         self.data = data




# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class linkedlist:
#     def __init__(self):
#         self.head = None

#     def append(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
            
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data,end="--> ")
#             current = current.next
#         print()


# ll = linkedlist()
# ll.append(8)
# ll.append(233)
# ll.display()

# ll2 = linkedlist()
# ll2.append(6)
# ll2.append(9)
# ll2.display()


# def merge(ll1,ll2):
#     current = ll1.head
#     while current.next:
#         current = current.next
#     current.next = ll2.head
#     return ll1

# newlsit = merge(ll, ll2)

# current = newlsit.head
# while current:
#     print(current.data,end="-->")
#     current =  current.next




# def merge(ll, ll2):
#     current = ll.head
#     while current.next:
#         current = current.next
#     current.next = ll2.head
#     return ll

# newlist = merge(ll, ll2)
# current = newlist.head
# while current:
#     print(current.data, end='---> ')
#     current = current.next



# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class linkedll:
#     def __init__(self):
#         self.head = None

#     def append(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head 
#             while current.next:
#                 current = current.next 
#             current.next = new_node

#     def display(self):
#         if self.head is None:
#             print("list is empty")
#         current = self.head
#         while current:
#             print(current.data,end="-->")
#             current = current.next
#         print()

#     def add_to_begin(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node 

#     def add_to_position(self,data,pos):
#         new_node = Node(data)
#         if pos == 0:
#             new_node.next = self.head
#             self.head = new_node
#             return
        
#         prev = None
#         current = self.head
#         index = 0

#         while current and index < pos:
#             prev = current
#             current = current.next 
#             index += 1

#         if index == pos:
#             prev.next = new_node
#             new_node.next = current
#         else:
#             print('Position is out of reange')

    
#     def delete_value(self,pos):
#         if pos == 0:
#             self.head.next = self.head
#             return 
        
#         prev = None
#         current = self.head
#         index = 0

#         while current and index < pos:
#             prev = current
#             current = current.next 
#             index += 1
#         if index == pos:
#             prev.next = current.next
#         else:
#             print('Postion out of range')




# ll = linkedll()
# ll.add_to_begin(55)
# ll.add_to_begin(7)
# ll2 = linkedll()
# ll2.add_to_begin(8)
# ll2.display()



# def merge(ll, ll2):
#     current = ll.head
#     while current.next:
#         current = current.next
#     current.next = ll2.head
#     return ll

# newlist = merge(ll, ll2)
# current = newlist.head
# while current:
#     print(current.data, end='---> ')
#     current = current.next


# def merge(ll,ll2):
#     current  = ll.head
#     while current.next:
#         current = current.next
#     current.next = ll2.head
#     return ll


# newlist = merge(ll, ll2)
# current = newlist.head
# while current:
#     print(current.data, end='-->')
#     current = current.next


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None


# class DoubelLinkedlist:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def append(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:
            
#             current = current.next 

#         current.next = new_node
#         new_node.prev = current

#     def display(self):
#         current = self.head 
#         while current:
#             print(current.data,end=" <-> ")
#             current = current.next
#         print()

#     def array_to_ll(self,arr):
#         self.head = arr[0]
#         current = self.head
#         for i in range(1,len(arr)):
#             current.next = arr[i]
#             current = current.next

# dll = DoubelLinkedlist()
# dll.append(49)
# dll.append(43)
# dll.append(4)
# dll.append(9)

# dll.display


# # linked list
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class Linkedll:
#     def __init__(self):
#         self.head = None

#     def add_to_begin(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
        
#     def add_to_end(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return 
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end='--> ')
#             current = current.next
#         print()

#     def add_after(self,data,value):
#         new_node = Node(data)
#         if self.head == value:
#             self.head.next = new_node
#             return 
#         current = self.head
#         while current:
#             if current.data == value:
#                 new_node.next = current.next
#                 current.next = new_node
#             current = current.next

#     def add_before(self,data,value):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return 
#         current = self.head
#         while current:
#             if current.data == value:
#                 prev.next = new_node
#                 new_node.next = current
#             prev = current
#             current = current.next 

#     def add_to_position(self,data,pos):
#         if pos < 0:
#             print('Invalid position')
#             return
#         new_node = Node(data)
#         if pos == 0:
#             new_node.next = self.head
#             self.head = new_node
#             return 
        
#         current = self.head
#         index = 0
#         while current and index != pos -1:
#             current = current.next 
#             index += 1
#         if not current:
#             print('position exceeds')
#             return
        
#         new_node.next = current.next
#         current.next = new_node  

#     def updata_value(self, old_value,  new_value):
#         current = self.head
#         while current:
#             if current.data == old_value:
#                 current.data = new_value
#                 return 
#             current = current.next

#     def delete_mid(self):
#         if self.head is None:
#             print('list is empty')
#             return
        
#         slow_ptr = self.head
#         fast_ptr = self.head
#         prev_ptr = None

#         while fast_ptr and fast_ptr.next:
#             prev_ptr = slow_ptr
#             slow_ptr = slow_ptr.next 
#             fast_ptr = fast_ptr.next.next

#         prev_ptr.next = slow_ptr.next

#     def delete_by_position(self, pos):
#         if self.head is None:
#             print('list is empty')
        
#         prev = None
#         current = self.head
#         index = 0
#         while current and index != pos:
#             prev = current
#             current = current.next
#             index += 1
        
#         prev.next = current.next

#     def insert_to_position(self, pos, data):
#         new_node = Node(data)
#         if pos == 0:
#             new_node.next = self.head
#             self.head = new_node
#             return 
        
#         current = self.head
#         prev = self.head
#         count = 0
        
#         while current and count < pos:
#             prev = current
#             current = current.next 
#             count += 1

#         prev.next = new_node
#         new_node.next = current

#     def reverse(self):
#         prev = None
#         current = self.head
#         while current:
#             new_node = current.next
#             current.next  = prev
#             current = new_node

#         self.head = prev

        

# ll = Linkedll()
# ll.add_to_position(17,4)
# ll.add_to_begin(882)
# ll.add_to_end(333)
# ll.add_to_begin(99)
# ll.add_to_begin(22)
# ll.add_to_end(33)
# ll.add_before(1,333)
# ll.add_after(100,99)
# ll.insert_to_position(3,9)
# ll.updata_value(882,2222)
# # ll.delete_mid()
# ll.delete_by_position(2)
# # ll.reverse()
# # ll.display()


# ll2 = Linkedll()
# ll2.add_to_end(11333)
# ll2.add_to_begin(1199)
# ll2.add_to_begin(1122)
# ll2.add_to_end(1133)
# ll2.add_before(111,333)
# # ll2.display()



# def merge(ll, ll2):
#     current = ll.head
#     while current.next:
#         current = current.next
#     current.next = ll2.head
#     return ll


# newlist = merge(ll, ll2)
# current = newlist.head
# while current:
#     print(current.data, end='-->')
#     current = current.next


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class singlell:
#     def __init__(self):
#         self.head = None

#     def append(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head 
#             while current.next:
#                 current = current.next
#             current.next = new_node

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data,end="--->")
#             current = current.next
#         print()

# ll = singlell()
# ll.append(8)
# ll.append(99)
# ll.display()

# ll2 = singlell()
# ll2.append(88)
# ll2.append(33)
# ll2.display()


# def merge(ll, ll2):
#     new_list = ll.head
#     while new_list.next:
#         new_list = new_list.next
#     new_list.next = ll2.head


# merge(ll, ll2)
# newlist = ll.head
# while newlist:
#     print(newlist.data,end="-->")
#     newlist = newlist.next
# print()

# def bubble_sort(ll):
#     swapped = True
#     while swapped:
#         swapped = False
#         current = ll.head
#         while current.next:
#             if current.data > current.next.data:
#                 current.data, current.next.data = current.next.data, current.data
#                 swapped = True
#             current = current.next

# bubble_sort(ll)
# sortedll = ll.head
# while sortedll:
#     print(sortedll.data, end="-->")
#     sortedll = sortedll.next




class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class Doublell:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.prev = new_node
        else:
            current = self.head 
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display(self):
        current = self.head
        while current:
            print(current.data,end="---> ")
            current = current.next
        print()


    def insert_to_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
                new_node = self.head
            else:
                self.head = new_node
        else:
            current = self.head
            count = 0
            while current and count < position - 1:
                current = current.next
                count += 1
            if current is None:
                print('postion exeeded')
            else:
                new_node.next = current.next
                if current.next:
                    current.prev = new_node
                current.next = new_node
                new_node.prev  = current

    def delete_from_begin(self):
        if self.head is None:
            print("list is empty. Nothing to delete")
            return
        if self.head.next:
            self.head.next.prev = None
        self.head = self.head.next


    def delete_from_end(self):
        current = self.head
        while current.next:
            current = current.next
        current.prev.next = None

    def delete_node(self, value):
        if self.head is Node:
            print('list is empty')
            return
        
        if self.head.data == value:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        
        current = self.head
        while current:
            if current.data == value:
                if current.next:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                else:
                    current.prev.next = None
                return
            current = current.next

    def add_after(self, data, value):
        new_node = Node(data)
        current = self.head
        while current.next:
            if current.data == value:
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                new_node.prev = current
                current.next = new_node
                return
            current = current.next
    def display_reverse(self):
        current = self.head
        # Move to the last node
        while current and current.next:
            current = current.next
        # Traverse backward and print each node's data
        while current:
            print(current.data, end="-->")
            current = current.prev

    def update_value(self, old_value, new_value):
        current = self.head 
        while current:
            if current.data == old_value:
                current.data = new_value
                break
            current = current.next
        
# dll = Doublell()
# dll.append(44)
# dll.append(4)
# dll.append(4222)
# dll.insert_to_position(2,3)
# dll.delete_from_end()
# dll.add_after(22,4)
# # dll.display_reverse()
# dll.update_value(44,7)
# dll.display()


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# def arr_to_ll(arr):
#     for data in arr:
#         new_node = Node(data)
#         if hea

            

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class linkedll:
#     def __init__(self):
#         self.head = None

#     def append(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head 
#             while current.next:
#                 current = current.next
#             current.next = new_node

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data,end="--> ")
#             current = current.next
#         print()

#     def delete(self,position):
#         current = self.head
#         count = 0
#         while current and count < position -1:
#             current = current.next
#             count += 1
#         if current is None:
#             print("postion is exeeded")
#         else:





# ll = linkedll()
# ll.append(77)
# ll.append(22)
# ll.display()


# def binery_search(arr, target, low, high):
#     mid = (low + high) // 2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] < target:
#         return binery_search(arr, target, mid + 1, high)
#     else:
#         return binery_search(arr, target, low, mid -1)


# def reverse_string(s):
#     if len(s) <=1:
#         return s
#     else:
#          return s[-1] + reverse_string(s[:-1])
    

# original_string = "hello"
# reversed_string = reverse_string(original_string)
# print("Original string:", original_string)
# print("Reversed string:", reversed_string)



# def insert_after(self, prev_node, data):
#     if prev_node is None:
#         print('haaaai')
#         return
#     new_node = Node(data)
#     new_node.next = prev_node.next
