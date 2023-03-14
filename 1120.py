s1, s2 = input().split()
best = 0

for i in range(len(s2)-len(s1)+1):
    count = 0
    for j in range(len(s1)):
        if s2[i:len(s2)+i][j] == s1[j]:
            count += 1
    if best<count:
        best=count

print(len(s1)-best)

