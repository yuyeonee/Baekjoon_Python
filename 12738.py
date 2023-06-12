from bisect import bisect_left

n = int(input())
nums = list(map(int, input().split()))
dp = []

for num in nums:
    k = bisect_left(dp, num)
    if k==len(dp):
        dp += [num]
    else:
        dp[k] = num

print(len(dp))