row_n, col_n = [int(i) for i in input().split()]

A = []
for row in range(row_n):
    A.append([int(i) for i in input().split()])

B = []
for row in range(row_n):
    B.append([int(i) for i in input().split()])


C = []
for row in range(row_n):
    C.append([])
    for col in range(col_n):
        C[row].append(A[row][col]+B[row][col])

for i in range(row_n):
    print(*C[i])