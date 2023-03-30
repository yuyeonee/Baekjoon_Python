n = int(input())
nums = list(map(int, input().split()))

dp = list(x for x in nums)

for i in range(1,n):
    dp[i] = max(dp[i-1]+dp[i], dp[i])
        
print(max(dp))