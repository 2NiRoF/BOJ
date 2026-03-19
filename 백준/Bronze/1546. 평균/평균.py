n = int(input())
scores = [int(x) for x in input().split()]
m = max(scores)

avg_new = (sum(scores)*100)/(n*m)
print(avg_new)