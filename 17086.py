from collections import deque

n, m = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))
sharks = []

def bfs(sharks):
    queue = deque()
    for shark in sharks:
        queue.append(shark)

    while queue:
        a, b = queue.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
            nx, ny = a+dx, b+dy
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[a][b] + 1
                queue.append((nx,ny))

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            sharks.append((i,j))

bfs(sharks)
ans = 0
for i in range(n):
    ans = max(ans, max(graph[i]))
print(ans-1)
