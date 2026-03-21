t = int(input())
for i in range(t):
    r, s = map(str, input().split())
    r = int(r)
    result = []
    for j in range(len(s)):
        result.append(s[j]*r)
    for k in range(len(s)):
        print(result[k], end="")
    print("")