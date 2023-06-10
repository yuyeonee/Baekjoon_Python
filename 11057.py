'''
1로 끝날 때/ 2로 끝날 때/ 3으로 끝날 때/ 해서 합산

'''

n = int(input())

dp = list([1]*10 for _ in range(n))

for i in range(1, n):
    for j in range(1, 10):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(sum(dp[n-1])%10007)