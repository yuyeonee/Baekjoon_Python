n = int(input())
scores = list(int(input()) for i in range(n))

for i in range(3):
    scores.append(0)

dp = [0]*(n+3)
dp[0] = scores[0]
dp[1] = scores[0] + scores[1]
dp[2] = max(scores[0]+scores[2], scores[1]+scores[2])

for i in range(3, n):
    dp[i] = max(dp[i-3]+scores[i-1]+scores[i], dp[i-2]+scores[i])

print(dp[n-1])

