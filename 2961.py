N = int(input())
food = list(list(map(int, input().split())) for _ in range(N))

def dfs(dep, S, B):
    global answer
    if dep==N:
        diff = abs(S-B)
        answer = min(answer, diff)
        return 

    else:
        if dep!=0:
            diff = abs(S-B)
            answer = min(answer, diff)
        for i in range(N):
            if visited[i]:
                visited[i] = False
                dfs(dep+1, S*food[i][0], B+food[i][1])
                visited[i] = True

visited = [True]*N
answer = 1000000000
dfs(0, 1, 0)
print(answer)


