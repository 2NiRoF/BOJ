t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    floor = h if n%h == 0 else n%h
    room = n//h if n%h == 0 else n//h+1
    if room < 10:
        print(str(floor) + '0' + str(room))
    else:
        print(str(floor) + str(room))