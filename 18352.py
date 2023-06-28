import sys
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

queue = deque()
queue.append(x)
distance = [-1]*(n+1)
distance[x] = 0

while queue:
    now = queue.popleft()

    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            queue.append(next_node)
    
if k in distance:
    for i in range(1, n+1):
        if distance[i]==k:
            print(i)
else:
    print(-1)