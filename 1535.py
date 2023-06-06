n = int(input())

hp = list(map(int, input().split()))
happy = list(map(int, input().split()))

person = [[0,0]]
for i in range(n):
    person.append([hp[i], happy[i]])

dp = [[0]*100 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 100):
        if person[i][0] <= j:
            dp[i][j] = max(dp[i-1][j], person[i][1]+dp[i-1][j-person[i][0]])
        else:
            dp[i][j] = dp[i-1][j]
            
print(max(dp[n]))