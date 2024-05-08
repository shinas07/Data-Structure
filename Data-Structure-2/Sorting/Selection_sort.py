
def selection_sort(arr):
    for i in range(len(arr)):
        min_indz = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_indz]:
                min_indz = j
        arr[i], arr[min_indz] = arr[min_indz], arr[i]

    return arr
arr = [9, 3, 1, 6, 2, 4]
print(selection_sort(arr))