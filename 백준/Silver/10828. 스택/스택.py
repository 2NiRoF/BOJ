import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    cmd = list(sys.stdin.readline().split())
    
    if cmd[0] == 'push':
        stack.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        try: result = stack.pop()
        except IndexError: result = -1
        print(result)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        print(1 if stack == [] else 0)
    elif cmd[0] == 'top':
        try: result = stack[-1]
        except IndexError: result = -1
        print(result)