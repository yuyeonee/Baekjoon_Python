import sys

n, m = map(int, input().split())
nums = list(map(int, input().split()))
dp = nums

for i in range(1, n):
    dp[i] = dp[i]+dp[i-1]
dp.insert(0,0)

for i in range(m):
    left, right = map(int, sys.stdin.readline().split())
    print(dp[right]-dp[left-1])