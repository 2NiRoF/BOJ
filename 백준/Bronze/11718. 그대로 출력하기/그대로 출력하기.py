import sys

s = []
k = 0
while k < 100:
    try:
        s.append(sys.stdin.readline().rstrip())
        k += 1
    except EOFError:
        break

for i in range(len(s)):
    print(s[i])