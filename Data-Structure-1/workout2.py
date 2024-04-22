# def biner_search(arr, low , high, target):
#     mid = (low + high) // 2
#     if arr[mid] == target:
#         return mid
#     if arr[mid] < target:
#         return arr[mid] - biner_search(arr, mid + 1, high, target)
#     else: 
#         return arr[mid] - biner_search(arr,low, mid +1, target)
    
# arr = [1,2,3,4,5,6,7]
# result = biner_search(arr,0,len(arr), 4)
# print(result)

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
#             print(current.data,end="-->")
#             current = current.next
#         print()


# ll = linkedlist()
# ll.append(77)
# ll.append(88)
# ll.display()

# ll2 = linkedlist()
# ll2.append(33)
# ll2.append(444)
# ll2.display()


# def merge(ll, ll2):
#     current = 

# word = 'apple'
# reversed_word = ''

# for char in word:
#     reversed_word = char + reversed_word

# print(reversed_word) # Output: 'eppla'



# word = 'apple'

# new_word = ""

# for i in range(len(word)):
#     if i == 0:
#         new_word += word[-1]
#     elif i == len(word) - 1:
#         new_word += word[0]
#     else:
#         new_word += word[i]

# print(new_word)


# word = 'apple'

# new_word = ""

# for i in range(len(word)):
#     if i == 0:
#         new_word += word[0].upper()
#     elif i == len(word) - 1:
#         new_word += word[-1].upper()
#     else:
#         new_word += word[i]

# print(new_word)


# word = 'shinas'
# def reverce_string(word):
#     if len(word) == 0:
#         return word
#     else:
#         return reverce_string(word[1:]) + word[0]
    

# print(reverce_string(word))