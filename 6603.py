def dfs(n, ind, answer):
    if n==6:
        print(*answer)

    else:
        for i in range(ind+1, N):
            if visited[i]:
                visited[i]=False
                dfs(n+1, i, answer+[nums[i]])
                visited[i] = True

while 1:
    tc = list(map(int, input().split()))
    if tc[0]==0:
        break
    N = tc[0]
    nums = tc[1:]
    visited = [True]*N
    answer = []

    dfs(0, -1, answer)
    print()