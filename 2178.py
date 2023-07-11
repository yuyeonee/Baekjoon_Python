import sys
from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(int(a) for a in list(map(str, sys.stdin.readline().strip()))))

visited = [[-1]*m for _ in range(n)]

def bfs(a,b):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append([a, b])
    visited[a][b] = 1

    while queue:
        a, b = queue.popleft()
        
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if -1<x<n and -1<y<m and graph[x][y]==1:
                if visited[x][y]==-1:
                    visited[x][y] = visited[a][b] + 1
                    queue.append([x, y])

            if x==n-1 and y==m-1:
                return visited[x][y]

print(bfs(0, 0))

