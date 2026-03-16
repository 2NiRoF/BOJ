n = int(input())
A = [int(i) for i in input().split()]
v = int(input())
cnt = 0

for k in A:
    if k == v:
        cnt += 1
print(cnt)