n = int(input())
nums = list(map(int, input().split()))
dp = [n+1]*n
dp[0] = 0

for i in range(n):
    for j in range(1, nums[i]+1):
        if i+j<n:
            dp[i+j] = min(dp[i+j], dp[i]+1)
print(-1 if dp[n-1]==n+1 else dp[n-1])

'''
1 2 0 1 3 2 1 5 4 2
1 1 1 1 1 1 1 1 1 1
1 
'''