from collections import deque

R, C = map(int, input().split())
graph = list(list(input()) for _ in range(R))

queue = deque()
queue.append([0,0, graph[0][0], 1])
ans = 1

while queue:
    a, b, alpha, cnt = queue.popleft()
    if ans < cnt:
         ans = cnt

    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx = a + dx
        ny = b + dy
        if 0<=nx<R and 0<=ny<C and graph[nx][ny] not in alpha:
                
                queue.append([nx,ny, alpha+graph[nx][ny], cnt+1])
                print(queue)
            
print(cnt)

