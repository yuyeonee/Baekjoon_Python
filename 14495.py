n = int(input())

dp = [1]*n

for i in range(3, n):
    dp[i] = dp[i-3] + dp[i-1]

print(dp[n-1])
