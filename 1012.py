import sys

TC = int(input())


def dfs(bachu):
    a, b = bachu
    visited[a][b] = False

    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = a+dx, b+dy
        if 0<=nx<N and 0<=ny<M and graph[nx][ny]==1 and visited[nx][ny]:
            dfs([nx,ny])


for _ in range(TC):
    N, M, K = map(int, input().split())
    bachu = list(tuple(map(int, sys.stdin.readline().split())) for _ in range(K))
    graph = [[0]*M for _ in range(N)]
    visited = [[True]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if (i, j) in bachu:
                graph[i][j] =1
    
    cnt=0
    for i in range(K):
        if visited[bachu[i][0]][bachu[i][1]]:
            dfs(bachu[i])
            cnt+=1
    print(cnt)



