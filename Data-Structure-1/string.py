# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial(num-1)
    

# result = factorial(5)
# print(result)


# def sumNum(value):
#     if value == 0:
#         return 0
#     else:
#         return value + sumNum(value - 1)


# result = sumNum(5)
# print(result)

def array_sum(arr,index): 
    if index >= len(arr):
        return 0
    else:
        return arr[index] + array_sum(arr, index + 1)
    
arr = [1, 2, 3, 4, 5]
result = array_sum(arr , 0)
print(result)