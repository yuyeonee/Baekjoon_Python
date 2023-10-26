from collections import deque

r, c, k = map(int, input().split())
graph = list(list(input()) for _ in range(r))
queue = deque()
queue.append((r-1, 0, [(r-1,0)], 1))

ans = 0
while queue:
    a, b, visited, dist = queue.popleft()

    if dist > k:
        continue

    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = a+dx, b+dy
        if 0<=nx<r and 0<=ny<c and graph[nx][ny]!='T' and (nx,ny) not in visited:
            queue.append((nx,ny, visited+[(nx,ny)], dist+1))
            if nx==0 and ny==c-1 and dist+1==k:
                ans+=1

print(1 if r==c==k==1 else ans)



