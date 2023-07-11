import sys
from collections import deque

n = int(input())
graph = []
check = []

for i in range(n):
    graph.append(list(int(a) for a in list(map(str, sys.stdin.readline().strip()))))

for i in range(n):
    for j in range(len(graph[0])):
        if graph[i][j]==1:
            check.append([i, j])

def bfs(a, b):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append([a, b])
    home = 0

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]

            if -1<x<n and -1<y<len(graph[0]) and graph[x][y]==1:
                if visited[x][y]==False:
                    visited[x][y] = True
                    queue.append([x,y])
                    home+=1
    if home==0:
        count.append(1)
    else: count.append(home)

visited = [[False]*len(graph[0]) for _ in range(n)]
cnt = 0
count = []
for a, b in check:
    if visited[a][b]==False:
        bfs(a, b)
        cnt+=1

print(cnt)
count.sort()
for i in range(cnt):
    print(count[i])

if cnt==0:
    print(0)