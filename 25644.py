n = int(input())
nums = list(map(int, input().split()))

dp = [0]*n
min = nums[0]

for i in range(1, n):
    dp[i] = nums[i] - min
    if nums[i] < min:
        min = nums[i]

print(max(dp))