import sys
from collections import deque

N, M, T = map(int, input().split())
graph = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
visited = [[-1]*M for _ in range(N)]
visited[0][0] = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()
queue.append([False,0,0])
flag1 = False

while queue:
    flag, a, b = queue.popleft()
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if flag:
            if 0<=x<N and 0<=y<M and (visited[x][y]==-1 or visited[x][y]==(visited[a][b]+1)):
                visited[x][y] = visited[a][b] + 1
                queue.append([True, x, y])

        else:
            if 0<=x<N and 0<=y<M and graph[x][y]!=1 and visited[x][y]==-1:
                visited[x][y] = visited[a][b] + 1
                if graph[x][y]==2:
                    queue.append([True, x, y])
                else:
                    queue.append([False, x, y])
        if x==N-1 and y==M-1:
            flag1 = True
            break
    if flag1:
        break
                

if visited[N-1][M-1]<=T and visited[N-1][M-1]!=-1:
    print(visited[N-1][M-1])
else:
    print('Fail')

