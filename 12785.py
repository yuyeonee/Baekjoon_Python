w, h = map(int, input().split())
x, y = map(int, input().split())

dp = list([1]*x for _ in range(y))

for i in range(1, y):
    for j in range(1, x):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
way1 = dp[y-1][x-1]

x, y = w-x+1, h-y+1
dp2 = list([1]*x for _ in range(y))

for i in range(1, y):
    for j in range(1, x):
        dp2[i][j] = dp2[i-1][j] + dp2[i][j-1]
way2 = dp2[y-1][x-1]

print((way1*way2)%1000007)