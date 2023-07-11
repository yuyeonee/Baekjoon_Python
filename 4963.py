import sys
from collections import deque

def bfs(v):
    queue = deque()
    queue.append(v)

    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]

    while queue:
        a, b = queue.popleft()
        for i in range(8):
            x = b + dx[i]
            y = a + dy[i]
            if -1<x<w and -1<y<h and graph[y][x]==1:
                if visited[y][x]==False:
                    visited[y][x] = True
                    queue.append([y, x])

while 1:
    w, h = map(int, sys.stdin.readline().split())
    if w==0 and h==0:
        break
    graph = list(list(map(int, sys.stdin.readline().split())) for _ in range(h))
    visited = [[False]*w for _ in range(h)]
    check = []

    for i in range(h):
        for j in range(w):
            if graph[i][j]==1:
                check.append([i, j])
    
    cnt = 0
    for a, b in check:
        if visited[a][b] == False:
            bfs([a, b])
            cnt += 1
    print(cnt)

