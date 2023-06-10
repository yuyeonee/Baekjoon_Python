n = int(input())

dp = list([0,0] for _ in range(n+1))
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, n+1):
    for j in range(2):
        if j==0:
            dp[i][j] = dp[i-1][0] + dp[i-2][0]
        else:
            dp[i][j] = dp[i-1][0] + dp[i-1][1]

print(*dp[n])