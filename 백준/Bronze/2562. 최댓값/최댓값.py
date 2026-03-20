a =[]

for i in range(9):
    a.append(int(input()))

print(max(a))
c = 0
for k in a:
    if k == max(a):
        index = a[c]
        break
    else: c += 1
print(c+1)