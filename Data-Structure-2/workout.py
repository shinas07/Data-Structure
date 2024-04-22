# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(0, len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

#     return arr

# arr = [8,33,4, 5, 2, 44]
# print(bubble_sort(arr))

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key  = arr[i]

#         j = i - 1
#         while j >=0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j-=1
#         arr[j + 1] = key
#     return arr

# arr = [4,5,2,33,4,2]
# print(insertion_sort(arr))


# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         key = arr[i]

#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr

# arr = [3,4,52,11,3,88,1,3]
# print(insertion_sort(arr))


# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         key = arr[i]
#         j = i-1

#         while j >= 0 and key < arr[j]:
#             arr[j] = arr[j+1]
#             j -= 1
        
#         arr[j+1] = key

#     return arr


# arr = [3,4,52,11,3,88,1,3]
# print(insertion_sort(arr))


# def merge_sort(arr):
#     if len(arr) > 1:

#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)
#         merge(arr, left_half, right_half)


# def merge(arr, left_half, right_half):
#     i = j = k = 0

#     while i < len(left_half) and j < len(right_half):
#         if left_half[i] < right_half[j]:
#             arr[k] = left_half[j]
#             i += 1

#         else:
#             arr[k] = right_half[j]
#             j 


# class Stack:
#     def __init__(self):
#         self.item = []

#     def push(self, item):
#         self.item.append(item)

#     def pop(self):
#         if self.item is None:
#             return self.item.pop()

#     def display(self):
#         print(self.item)


# stack = Stack()
# stack.push(44)
# stack.push(333)
# stack.display()


# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i = j = k = 0
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1

#     return arr

# arr = [44,5,3,2,4,5,6,3,4]
# print(merge_sort(arr))


# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr) -i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr


# arr = [44,3,4,2,1,3,33,3]

# print(bubble_sort(arr))


# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -= 1

#         arr[j+1] = key
    
#     return arr



# print(insertion_sort(arr))


# def seleciton_sort(arr):
#     for i in range(len(arr)):
#         min_value = i
#         for j in range(i+1,len(arr)):
#             if arr[j] < arr[min_value]:
#                 min_value = j
#             arr[i], arr[min_value] = arr[min_value], arr[i]

#     return arr

# arr = [33,4,5,3,456,3]
# print(seleciton_sort(arr))

# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

#     return arr

# arr = [55,4,2,14,4,22,1]
# print(bubble_sort(arr))

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i-1

#         while j >= 0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1

#         arr[j+1] = key

#     return arr

# arr = [4,22,31,11,6,2]
# print(insertion_sort(arr))

# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_value = i

#         for j in range(i+1, len(arr)):
#             if arr[j] > arr[min_value]:
#                 min_value = j
#             arr[j], arr[min_value] = arr[min_value], arr[j]

#     return arr


# arr = [44,2,1,3,52,1]
# print(selection_sort(arr))



# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i = j = k = 0

#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(left_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1

#     return arr
    


# arr = [44,3,2,3,33,4,2]
# print(merge_sort(arr))

# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1

#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]

#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1


# def quick_sort(arr, low, high):
#     if low < high:
#         pivot_index = partition(arr, low, high)

#         quick_sort(arr, low, pivot_index - 1)
#         quick_sort(arr, pivot_index + 1, high)
    
#     return arr




# arr = [4, 4, 444, 1, 3, 66, 2]
# print(quick_sort(arr,0,len(arr) -1))

# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1

#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i],arr[j] = arr[j], arr[i]

#         arr[i+1], arr[high] = arr[high], arr[i + 1]
#         return i + 1
    
# def quick_sort(arr, low, high):
#     if low < high:
#         pivot_index = partition(arr, low, high)
#         quick_sort(arr,low, pivot_index - 1)
#         quick_sort(arr,pivot_index + 1,high)

# my_list = [3, 6, 8, 10, 1, 2, 1]
# print("Original array:", my_list)
# quick_sort(my_list, 0, len(my_list) - 1)
# print("Sorted array:", my_list)


# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self,data):
#         self.items.append(data)

#     def is_empty(self):
#         return len(self.items) == 0
    
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             print('Stack is empty')
#             return None
        
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
        
#     def all_values(self):
#         all_values = []
#         while not self.is_empty():
#             value = self.items.pop()
#             all_values.append(value)
#         return all_values



# stack = Stack()
# stack.push(33)
# stack.push(88)
# print(stack.all_values())

# class Stack:
#     def __init__(self,size):
#         self.stack = []
#         self.size = size
#         self.top = -1

#     def push(self,item):
#         if self.top == self.size -1:
#             print('stack overflow')
#         else:
#             self.top += 1
#             self.stack.append(item)

#     def pop(self):
#         if self.top == -1:
#             print('Stack is empty')
#             return None
#         else:
#             self.top -= 1
#             popped = self.stack.pop()
#             return popped
        
#     def peek(self):
#         if self.top == -1:
#             print('stack is empty')
#             return None
#         else:
#             return self.stack[self.top]
        
#     def display(self):
#         print("Stack elements:")
#         for i in range(self.top, -1, -1):
#             print(self.stack[i])


# stack = Stack(5)

# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(5)


# stack.display()

# print("Top element:", stack.peek())


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class stack:
#     def __init__(self):
#         self.top = None

#     def push(self,item):
#         new_node = Node(item)
#         if self.top is None:
#             self.top = new_node
#         else:
#             new_node.next = self.top
#             self.top = new_node

#     def pop(self):
#         if self.top is None:
#             return None
#         else:
#             popped_node = self.top
#             self.top = self.top.next


#     def display(self):
#         current = self.top
#         while current:
#             print(current.data)
#             current = current.next


# s = stack()
# s.push(88)
# s.push(23)
# s.pop()
# s.display()

# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(0,len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# arr = [33,42,3,21,2,333,4,12,2]
# print(bubble_sort(arr))

# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         key = arr[i]
#         j = i-1
#         while j >= 0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
        
#         arr[j + 1] = key

#     return arr

# arr = [33,42,3,21,2,333,4,12,2]
# print(insertion_sort(arr))

# def selction_sort(arr):
#     for i in range(len(arr)):
#         min_values = i
#         for j in range(i+1,len(arr)):
#             if arr[j] < arr[min_values]:
#                 min_values = j
        
#         arr[i], arr[min_values] = arr[min_values], arr[i]

#     return arr
# arr = [33,42,3,21,2,333,4,12,2]
# print(selction_sort(arr))

# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i = j = k = 0

#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1
        
#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1

#     return arr

# arr = [44,21,12,34,55,2,34]
# print(merge_sort(arr))


# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1
#     for j in range(low, high):
#         if arr[j] < pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
    
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]

#     return i + 1


# def quick_sort(arr, low,high):
#     if low < high:
#         pivot_indext = partition(arr, low, high)
#         quick_sort(arr,low, pivot_indext -1)
#         quick_sort(arr, pivot_indext + 1, high)

# arr = [44, 2, 1,22, 3,1 ,333,11]
# quick_sort(arr,0,len(arr) -1)
# print(arr)

# def unique_first_value(arr):
#     unique = False
#     for i in range(len(arr)):
#         unique = True
#         for j in range(len(arr)):
#             if i != j and arr[i] == arr[j]:
#                 unique = False
#         if unique:
#             return arr[i]
        

# arr = [99,2,2,1,22,99,1]
# print(unique_first_value(arr))