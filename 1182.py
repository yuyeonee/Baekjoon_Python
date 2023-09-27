N, k = map(int, input().split())
nums = list(map(int, input().split()))

def dfs(n, index, ans):
    global cnt
    if ans==k and n>0:
        cnt+=1

    for i in range(index+1, N):
        if visited[i]:
            visited[i] = False
            dfs(n+1, i, ans+nums[i])
            visited[i] = True

cnt = 0
visited = [True]*N
dfs(0, -1, 0)
print(cnt)
