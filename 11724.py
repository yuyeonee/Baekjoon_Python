import sys
from collections import deque

def bfs(node):
    queue = deque()
    queue.append(node)
    
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if check[next] == 0:
                check[next] = check[now] + 1
                queue.append(next)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

check = [0]*(n+1)
count = 0

for i in range(1, n+1):
    if check[i]==0:
        if not graph[i]:
            count+=1
        else:
            bfs(i)
            count+=1
print(count)


