L = []
for i in range(10):
    L.append(int(input()))

modulo = []

for j in L:
    modulo.append(j%42)

modset = set(modulo)
print(len(modset))