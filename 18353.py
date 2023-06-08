n = int(input())
sds = list(map(int, input().split()))

dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if sds[i] <= sds[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
