import sys
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited_d = [True]*(n+1)


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for lst in graph:
    lst.sort()

ans_d = []
def dfs(node):
    visited_d[node] = False
    if node not in ans_d:
        ans_d.append(node)
    for next in graph[node]:
        if visited_d[next]:
            dfs(next)

ans_b = []
def bfs(node):
    queue = deque()
    queue.append(node)
    visited_b = [True]*(n+1)
    visited_b[node] = False
    while queue:
        node = queue.popleft()
        ans_b.append(node)
        for next in graph[node]:
            if visited_b[next]:
                queue.append(next)
                visited_b[next] = False

dfs(v)
print(*ans_d)
bfs(v)
print(*ans_b)
