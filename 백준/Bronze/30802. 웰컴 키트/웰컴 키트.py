import sys

n = int(sys.stdin.readline())
shirts = [int(x) for x in sys.stdin.readline().split()]
t, p = map(int, sys.stdin.readline().split())

pens_Q = n//p
pens_M = n%p

shirts_Q = []

for k in shirts:
    shirts_Q.append(-((-k)//t))

howmanyshirts = sum(shirts_Q)
print(howmanyshirts)
print(pens_Q, pens_M)