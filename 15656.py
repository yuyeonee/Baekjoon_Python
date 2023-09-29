N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def dfs(m, ans):
    if M==m:
        print(*ans)
        return
    else:
        for i in range(N):
            dfs(m+1, ans+[nums[i]])

ans = []
dfs(0, ans)
    