s = input()
a = []


for i in range(len(s)):
    for j in range(i, len(s)):
        a.append(s[i:j+1])

ans = set(a)
print(len(ans))