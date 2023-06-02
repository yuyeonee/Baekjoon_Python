n = int(input())

dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(3): # rgb 3개 j는 0,1,2 밖에 없음
        if j==0:
            dp[i][0] += min(dp[i-1][1], dp[i-1][2])
        elif j==1:
            dp[i][1] += min(dp[i-1][0], dp[i-1][2])
        else:
            dp[i][2] += min(dp[i-1][1], dp[i-1][0])

print(min(dp[n-1]))