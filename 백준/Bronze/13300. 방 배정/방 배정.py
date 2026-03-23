n, k = [int(x) for x in input().split()]
scnt = {}
rcnt = 0
for i in range(n):
    s, y = [str(x) for x in input().split()]
    sy = s+y
    if sy in scnt:
        scnt[sy] += 1
    else:
        scnt[sy] = 1

for sy, cnt in scnt.items():
    if cnt%k == 0:
        rcnt += cnt//k
    else:
        rcnt += cnt//k + 1

print(rcnt)