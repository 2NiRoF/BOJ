n = int(input())
a_n = [int(x) for x in input().split()]
x = int(input())

numset = set(a_n)

cnt = 0
for i in range(n):
    if x - a_n[i] in numset:
        cnt += 1
        if x - a_n[i] == a_n[i]:
            cnt -= 1
cnt = int(cnt / 2)
print(cnt)