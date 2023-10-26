from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
graph = [[0]*n for _ in range(n)]

queue = deque()
queue.append((r1, c1))
flag = False

while queue:
    a, b = queue.popleft()
    for dx, dy in [(-2,-1), (-2,1), (0,-2), (0,2), (2,-1), (2,1)]:
        nx, ny = a+dx, b+dy
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]==0:
            graph[nx][ny] = graph[a][b]+1
            queue.append((nx,ny))
            if nx==r2 and ny==c2:
                flag = True
                print(graph[nx][ny])
                break
    if flag:
        break

if not flag:
    print(-1)

