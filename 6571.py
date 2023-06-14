dp = [1, 2]
ind = 2

while dp[-1] <= 10**100:
    dp.append(dp[ind-1] + dp[ind-2])
    ind += 1

while 1:
    a, b = map(int, input().split())
    if a==0 and b==0:
        break
    cnt = 0
    for num in dp:
        if num>=a and num<=b:
            cnt += 1
        if num>b:
            break
    print(cnt)
        

