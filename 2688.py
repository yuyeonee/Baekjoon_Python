dp = list([1]*10 for _ in range(64))

for i in range(1, 64):
    for j in range(1, 10):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]


n = int(input())

for i in range(n):
    num = int(input())
    print(sum(dp[num-1]))
