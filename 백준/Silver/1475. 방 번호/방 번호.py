n = input()
cnt = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    for j in range(len(n)):
        if int(n[j]) == i:
            cnt[i] += 1

sixnine = (cnt[6]+cnt[9]+1)//2
cnt[6] = sixnine
cnt[9] = 0  
maxcnt = max(cnt)
maxnum = cnt.index(maxcnt)

print(maxcnt)