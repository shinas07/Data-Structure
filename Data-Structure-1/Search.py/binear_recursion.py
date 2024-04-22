def binary_search(arr, low, high, target):
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return f"found at {mid}"
        elif arr[mid] < target:
            return binary_search(arr, mid + 1, high, target)
        else:
            return binary_search(arr, low, mid-1, target)
    
    return -1


arr = [2, 13, 9, 4, 34, 59, 33, 29]
index = binary_search(arr, 0, len(arr) - 1, 59) 
print(index)

