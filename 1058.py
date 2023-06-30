n = int(input())
YoN = list(input() for _ in range(n))
mostfamous = 0

for i in range(n):
    friends = 0
    for j in range(n):
        if i==j:
            continue
        if YoN[i][j] == 'Y':
            friends += 1
        elif YoN[i][j] =='N':
            for k in range(n):
                if YoN[j][k]=='Y' and YoN[i][k]=='Y':
                    friends += 1
                    break
    if mostfamous < friends:
        mostfamous = friends
    
print(mostfamous)