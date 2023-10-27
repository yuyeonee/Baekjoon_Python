from bisect import bisect_left

n = int(input())
nums = list(map(int, input().split()))

dp = []

for num in nums:
    ind = bisect_left(dp, num)

    if ind==len(dp):
        dp.append(num)
    else:
        dp[ind] = num

print(dp)