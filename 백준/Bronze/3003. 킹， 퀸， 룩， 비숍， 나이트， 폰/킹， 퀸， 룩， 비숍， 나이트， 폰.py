import sys

pieces = [int(x) for x in sys.stdin.readline().split()]
correct = [1, 1, 2, 2, 2, 8]

request = []

for i in range(len(pieces)):
    request.append(correct[i]-pieces[i])

print(*request)