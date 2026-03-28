t = int(input())

for i in range(t):
    ans = input()
    score = 0
    ans_list = ans.split("X")
    for j in range(len(ans_list)):
        try: ans_list.remove('')
        except ValueError: break
    
    for x in ans_list:
        temp = 0
        for k in range(x.count("O")):
            temp += k+1
        score += temp
    print(score)