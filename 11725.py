import sys

sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n+1)]
parent = [None for _ in range(n+1)]

def dfs(graph, vertex, visited):
    for node in graph[vertex]: 
        if not visited[node]: # 방문한 적 없을 경우
            visited[node] = vertex
            dfs(graph, node, visited)

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(tree, 1, parent)

for i in range(2, n+1):
    print(parent[i])
    