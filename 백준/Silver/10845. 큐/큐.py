from collections import deque
import sys

queue = deque([])

n = int(sys.stdin.readline().strip())
for i in range(n):
    cmd = sys.stdin.readline().strip()
    cmds = cmd.split()
    if len(cmds) == 2:
        queue.append(cmds[-1])
    
    elif cmd == 'pop':
        try:
            result = queue.popleft()
        except IndexError:
            result = -1
        print(result)
    
    elif cmd == 'size':
        print(len(queue))

    elif cmd == 'empty':
        print(1 if len(queue)==0 else 0)
    
    elif cmd == 'front':
        try: result = queue[0]
        except IndexError: result = -1
        print(result)
    
    elif cmd == 'back':
        try: result = queue[-1]
        except IndexError: result = -1
        print(result)

#문제에 나와있지 않은 명령은 주어지지 않기 때문에 예외처리는 구현하지 않음