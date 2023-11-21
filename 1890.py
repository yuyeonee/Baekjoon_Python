n = int(input())
nums = list(list(map(int, input().split())) for _ in range(n))
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        temp = nums[i][j]
        if temp==0:
            continue
        if i+temp<n:
            dp[i+temp][j] += dp[i][j]
        if j+temp<n:
            dp[i][j+temp] += dp[i][j]

print(dp[n-1][n-1])

