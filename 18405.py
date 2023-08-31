import sys
from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
check1 = []
visited = [[-1]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j]!=0:
            check1.append([graph[i][j], [i,j]])
            visited[i][j] = 0
check1.sort(key = lambda x: x[0])
check = []

for list in check1:
    check.append(list[1])

s, X, Y = map(int, input().split())
queue = deque(check[:])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
flag = False

while queue:
    a, b = map(int, queue.popleft())
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]

        if 0<=x<n and 0<=y<n and graph[x][y]==0:
            visited[x][y] = visited[a][b]+1
            if visited[x][y] > s:
                flag = True
                break
            graph[x][y] = graph[a][b]
            queue.append([x, y])
    if flag:
        break

print(graph[X-1][Y-1])