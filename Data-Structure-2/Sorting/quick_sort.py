arr = [2,3,4,5,6,7,74,2,1,2]
result = quick_sort(arr)
print(result)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
arr = [3, 2,12,2,6, 8, 10, 1,3,9,2,44,5, 2, 1]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)




def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index- 1)
        quick_sort(arr, pivot_index + 1,high)


arr = [22, 3, 44, 2, 1, 3, 4]
quick_sort(arr, 0, len(arr) - 1)
print(arr)