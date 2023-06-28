from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

distance = [-1]*(n+1)
distance[a] = 0
queue = deque()
queue.append(a)

while queue:
    now = queue.popleft()

    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            queue.append(next_node)
    if now==b:
        break
        
print(distance[b])
