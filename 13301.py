n = int(input())

dp = [1]*(n)

for i in range(2, n):
    dp[i] = dp[i-1] + dp[i-2]

print((dp[n-1]*2 + dp[n-2])*2 if n!=1 else 4)