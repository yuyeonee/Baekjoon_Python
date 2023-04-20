n, k = map(int, input().split())
nums = list(map(int, input().split()))
dp = nums

for i in range(1, n):
    dp[i] = dp[i] + dp[i-1]

sums=[dp[k-1]]
for i in range(k, n):
    sums.append(dp[i] - dp[i-k])

print(max(sums))

