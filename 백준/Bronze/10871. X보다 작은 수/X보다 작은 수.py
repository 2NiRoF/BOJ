n, x = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

for k in A:
    if k < x:
        print(f"{k} ", end="")