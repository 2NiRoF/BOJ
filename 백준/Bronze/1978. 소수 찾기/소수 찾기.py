import sys
import math

n = int(sys.stdin.readline())
numbers = [int(x) for x in input().split()]

count = 0
for i in range(0, len(numbers)):
    temp_cnt = 0
    for j in range(1, int(math.sqrt(numbers[i]))+1):
        if numbers[i] == 1:
            pass
        elif numbers[i] % j == 0:
            temp_cnt += 1
        else:
            None
    if temp_cnt == 1:
        count += 1

print(count)