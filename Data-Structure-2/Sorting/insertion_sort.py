def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1


        while j>=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j+1] = key
    
    return arr  

arr = [34, 22, 66, 2, 12,4]
print(insertion_sort(arr))