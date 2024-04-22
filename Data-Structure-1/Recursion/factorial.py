def factorical(num):
    if num <= 1:
        return num
    else:
        return num * factorical(num - 1)
    
result = factorical(5)
print(result)