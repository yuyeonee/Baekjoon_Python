n = int(input())
card = list(map(int, input().split()))

dp = card[:]

for i in range(1, n):
    for j in range(0, i):
        dp[i] = max(dp[j]+dp[i-j-1], dp[i])
print(dp[-1])