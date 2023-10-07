import sys

input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    n = int(input())
    sticker = list(list(map(int, input().split())) for _ in range(2))
    dp = [[0,0]]*n
    stick = [[0,0]]*n
    for i in range(n):
        stick[i] = [sticker[0][i], sticker[1][i]]
    
    #dp = [sticker[i] for i in range(2)]
    dp[0] = [sticker[0][0], sticker[1][0]]
    for i in range(1, n):
        if i>1:
            dp[i] = [max(dp[i-1][1]+stick[i][0], max(dp[i-2])+stick[i][0]), max(dp[i-1][0]+stick[i][1], max(dp[i-2])+stick[i][1])]
        else:
            dp[i] = [dp[i-1][1]+stick[i][0], dp[i-1][0]+stick[i][1]]
    print(max(dp[-1]))