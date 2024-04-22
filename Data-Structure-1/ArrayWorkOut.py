# unique
# arr = [1, 2, 3, 3, 4, 4, 5]
# unique = []
# for i in range(1,len(arr)):
#     if unique not in arr:
#         unique.append(i)
# print(unique)


# Count Occurrences of Element
# arr = [1, 2, 3, 3, 4, 4, 5]
# counts = {}
# for num in arr:
#     if num in counts:
#         counts[num] += 1
#     else:
#         counts[num] = 1
# print(counts)

# max and min
# arr = [1, 2, 3, 4, 5]
# min = arr[0]
# max = arr[0]
# for num in arr[1:]:
#     if num > max:
#         max = num
#     elif num < min:
#         min = num
# print(f'Max values is{max} and min values is {min}')

# # sum of positive numbers
# arr = [3, -1, 4, -5, 6, 0, 7, -2]
# sum_of_num = 0
# for i in arr:
#     if i > 0 and i % 2 == 0:
#         sum_of_num += i
# print(sum_of_num)

# logest string
# strings = ["apple", "banana", "kiwi", "orange"]
# longest_string = strings[0]
# for string in strings:
#     if len(longest_string) < len(string):
#         longest_string = string
# print(longest_string)

# 1. Reverse a String
# orginal_string = 'shinas'
# print(orginal_string[::-1])

# # without slice
# orginal_string = 'shinas'
# reversed_str = ''
# for char in orginal_string:
#     reversed_str = char + reversed_str
# print(reversed_str)

# 2. Count Vowels and Consonants
# vowels = "aeiou"
# words = 'shinas'
# count = 0
# for i in words:
#     if i in vowels:
#         count += 1
# print(count)


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

# class DoubleLinkedList:
#     def __init__(self):
#         self.head = None

#     def is_empty(self):
#         return self.head is None
    
#     def append(self, data):
#         new_node = Node(data)
#         if self.is_empty():
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:
#             current = current.next
        
#         new_node.prev = current
#         current.next = new_node

#     def display_forward(self):
#         current = self.head

#         while current:
#             print(current.data, end = " <-> ")
#             current = current.next

#     def display_backward(self):
#         current = self.head
#         while current.next:
#             current = current.next

#         while current:
#             print(current.data, end= " <-> ")
#             current = current.prev
#         print("None")

# # Creating an instance of the DoubleLinkedList class
# dd = DoubleLinkedList()
# dd.append(4)
# dd.append(99)
# dd.display_backward()



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next 


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


    def display(self):
        current = self.head
        while current:
            print(current.data,end = "--> ")
            current = current.next
        print()

    # def delete_middle(self):
    #     if not self.head:
    #         return None
        
    #     slow_ptr = self.head
    #     fast_ptr = self.head
    #     prev_ptr = None

    #     while fast_ptr and fast_ptr.next:
    #         fast_ptr = fast_ptr.next.next
    #         prev_ptr = slow_ptr
    #         slow_ptr = slow_ptr.next

    #     prev_ptr.next = slow_ptr.next

    def delete_middle(self):
        if self.head is None:
            return
        
        fast_ptr = self.head
        slow_ptr = self.head
        prev = None

        while fast_ptr and fast_ptr.next:

            fast_ptr = fast_ptr.next.next
            prev = slow_ptr
            slow_ptr = slow_ptr.next

        prev.next = slow_ptr.next

ll = linkedlist()
ll.append(44)
ll.append(99)
ll.append(33)
ll.append(222)
ll.delete_middle()
ll.display()


def removing(self, value):
    if self.head and self.head == value:
        self.head = self.head.next
        return 
    
    current = self.head
    prev = None

    while current:
        if current.data == value:
            prev.next = current.next
            return
        prev = current
        current = current.next


