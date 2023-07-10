from collections import deque

n = int(input())
jumps = [0] + list(map(int, input().split()))
a, b = map(int, input().split())

def bfs(a, b): 
    queue = deque([a]) 
    visited = [-1]*(n+1)
    visited[a] = 0

    while queue:
        now = queue.popleft()
        
        for i in range(now, n+1, jumps[now]):
            if visited[i]==-1:
                visited[i] = visited[now] + 1
                queue.append(i)
                if i==b:
                    return visited[i]
        for i in range(now, 0, -jumps[now]):
            if visited[i]==-1:
                visited[i] = visited[now] + 1
                queue.append(i)
                if i==b:
                    return visited[i]
    return -1

print(bfs(a,b))





