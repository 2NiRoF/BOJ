attendance = [int(i) for i in range(1, 31)]

for k in range(len(attendance)-2):
    attendance.remove(int(input()))

if attendance[0] < attendance[1]:
    for i in attendance:
        print(i)
else:
    for i in attendance:
        print(attendance[len(attendance)-i-1])