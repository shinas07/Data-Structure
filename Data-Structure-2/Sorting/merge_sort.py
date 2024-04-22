# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]
#         merge_sort(left_half)
#         merge_sort(right_half)
#         merge(arr, left_half, right_half)

# def merge(arr, left_half, right_half):
#     i = j = k =0

#     while i < len(left_half) and j < len(right_half):
#         if left_half[i] < right_half[j]:
#             arr[k] = left_half[i]
#             i+=1
#         else:
#             arr[k] = right_half[j]
#             j+=1
#         k+=1

#     while i < len(left_half):
#         arr[k] = left_half[i]
#         i+=1
#         k+=1
#     while j < len(right_half):
#         arr[k] = right_half[j]
#         j+=1 
#         k+=1

# arr = [6, 1, 2, 9, 2, 3, 1]
# merge_sort(arr)
# print(arr)


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

# arr = [3, 44, 333, 4, 55,4]
# print(merge_sort(arr))


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1  

        return arr
    

arr = [55,4,22, 1,23, 99,3]
print(merge_sort(arr))


