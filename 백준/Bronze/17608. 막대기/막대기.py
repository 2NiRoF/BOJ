import sys

n = int(sys.stdin.readline())

stack = []
for i in range(n):
    stack.append(int(sys.stdin.readline()))
temp = stack[-1]

j = 1
while True:
    try:
        if stack[-j-1] <= temp:
            del(stack[-j-1])
        else:
            temp = stack[-j-1]
            j += 1
    except IndexError:
        break

print(len(stack))