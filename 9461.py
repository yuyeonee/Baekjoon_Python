
n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

dp = [0]*(max(nums)+1)
dp[1] = 1
dp[2] = 1

for i in range(3, max(nums)+1):
    dp[i] = dp[i-2]+dp[i-3]

for n in nums:
    print(dp[n])
'''1 1 1 2 2 3 4 5 7 9 12'''