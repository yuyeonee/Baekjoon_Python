n, m = map(int, input().split())

dp = list([1]*m for _ in range(n))

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i][j-1]

print(max(dp[n-1])%1000000007)