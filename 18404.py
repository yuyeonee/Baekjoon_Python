import sys
from collections import deque

def bfs(a, b):
    graph[a][b] = 0
    queue = deque()
    queue.append([a, b])

    while queue:
            a, b = queue.popleft()

            for i in range(8):
                n = a + dx[i]
                m = b + dy[i]

                if 0<n<N+1 and 0<m<N+1 and graph[n][m]==-1:
                    graph[n][m] = graph[a][b] + 1
                    queue.append([n, m])
                    

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

N, M = map(int, input().split())
a, b = map(int, input().split())
graph = [[-1]*(N+1) for _ in range(N+1)]

answer = []

bfs(a, b)

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    print(graph[x][y], end = ' ')
    
print(*answer)     