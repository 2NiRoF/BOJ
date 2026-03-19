def sp_operation(a, b):
    return (a+b)*(a-b)

a, b = [int(i) for i in input().split()]
print(sp_operation(a, b))