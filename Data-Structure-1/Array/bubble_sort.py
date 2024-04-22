#Bubble sort

arr = [3, 9, 2, 0, 4, 2, 29, 28, 78]

for i in range(len(arr)):
    for j in range(1,len(arr) -i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr [j + 1], arr[j]

print(arr)

