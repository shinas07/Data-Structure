
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
    
arr = [10, 50, 90, 20, 33, 22, 90]
target = 33
print(linear_search(arr,target))

