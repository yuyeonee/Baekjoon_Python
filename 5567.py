import sys
from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

check = [-1]*(n+1)
check[1] = 0
queue = deque()
queue.append(1)
flag = False
count = 0

while queue:
    now = queue.popleft()

    for next in graph[now]:
        if check[next] == -1:
            check[next] = check[now]+1
            queue.append(next)
            if check[next] > 2:
                flag = True
                break
            count+=1
        
    if flag:
        break

print(count)