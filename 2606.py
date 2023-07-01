from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)
queue = deque()
queue.append(1)
check = [0]*(n+1)
while queue:
    now = queue.popleft()
    print(queue)
    for next in graph[now]:
        if check[next] == 0:
            check[next] == 1
            queue.append(next)
        
print(check)