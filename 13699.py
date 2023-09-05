n = int(input())

dp = [1]*36
dp[0] = 1

for i in range(1, 36):
    sum = 0
    for j in range(i):
        sum += dp[j]*dp[i-j-1]
    dp[i] = sum

print(dp[n])