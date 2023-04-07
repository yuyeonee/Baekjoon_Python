import sys

n = int(input())
dp = [0]*1000001
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3,1000001):
    dp[i] = dp[i-1]%1000000009 + dp[i-2]%1000000009 + dp[i-3]%1000000009

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    print(dp[num]%1000000009)


'''
1 1
2 2
3 4
4 7
5 13
6 24
7 44'''

