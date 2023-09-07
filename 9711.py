import sys

T = int(input())
dp = [1]*10000

for i in range(2, 10000):
    dp[i] = dp[i-1] + dp[i-2]

for i in range(T):
    p, q = map(int, sys.stdin.readline().split())
    m = dp[p-1]%q
    x = i+1
    print("Case #"+str(x)+": "+str(m))