n = int(input())
f = n
if n == 0:
    print(1)
else:
    while n > 1:
        n -= 1
        f *= (n)
    print(f)