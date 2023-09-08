n = int(input())

dp = [1]*1000001
dp[0] = 0

for i in range(2, 1000001):
    dp[i] = (dp[i-1] + dp[i-2])%1000000000

if n>0:
    print(1)
elif n==0:
    print(0)
elif n<0:
    if abs(n)%2==0:
        print(-1)   
    else:
        print(1)
print(abs(dp[abs(n)]))
