n = int(input())
nums = list(map(int, input().split()))
dp = nums

for i in range(1,n):
    best=0
    state = nums[i]
    for j in range(i):
        if nums[i]>nums[j]:
            dp[i] = max(dp[i], dp[j]+state)
print(max(dp))
