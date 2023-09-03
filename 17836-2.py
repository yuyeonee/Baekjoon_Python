import sys
from collections import deque

N, M, T = map(int, input().split())
graph = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
visited = [[-1]*M for _ in range(N)]
visited[0][0] = 0
flag = False

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()
queue.append([0,0])
w = 0
windex = [0,0]

while queue:
    a, b = queue.popleft()
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        
        if 0<=x<N and 0<=y<M and graph[x][y]!=1 and visited[x][y]==-1:
            visited[x][y] = visited[a][b] + 1
            if graph[x][y]==2:
                w = visited[x][y]
                windex = [x,y]
            
            queue.append([x, y])
        if x==N-1 and y==M-1:
            flag = True
            break
    if flag:
        break

answer = w + (N-1-windex[0]) + (M-1-windex[1])


if w==0:
    if visited[N-1][M-1]==-1:
        print('Fail')
    else:
        print(visited[N-1][M-1])
else:
    if visited[N-1][M-1]==-1:
        if answer<=T:
            print(answer)
        else:
            print('Fail')
    else:
        if answer>visited[N-1][M-1]:
            answer = visited[N-1][M-1]
        if answer<=T:
            print(answer)
        else:
            print('Fail')