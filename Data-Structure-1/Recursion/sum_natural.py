def sum_natural(num):
    if num == 0:
        return 0
    else:
        return num + sum_natural(num - 1)
    
result = sum_natural(5)
print("Sum of the first 5 natural numbers:",result)