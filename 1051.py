n, m = map(int, input().split())
nums = list(list(input()) for _ in range(n))
r = min(n,m)

flag = False

for t in range(r, 0, -1):
    for i in range(n-t+1):
        for j in range(m-t+1):
            if nums[i][j] == nums[i+t-1][j] == nums[i][j+t-1] == nums[i+t-1][j+t-1]:
                flag = True
                print(t*t)
                break
        if flag:
            break
    if flag:
        break
