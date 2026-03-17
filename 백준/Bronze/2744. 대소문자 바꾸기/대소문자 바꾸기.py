s = input()
s2 = []
for i in range(len(s)):
    if s[i].isupper():
        s2.append(s[i].lower())
    else:
        s2.append(s[i].upper())

for i in s2:
    print(i, end="")