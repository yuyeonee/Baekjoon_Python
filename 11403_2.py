import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = list(list(map(int, input().split())) for _ in range(n))
visited = [[0]*n for _ in range(n)]

def bfs(st):
    queue = deque()
    queue.append(st)
    check = [0 for _ in range(n)]

    while queue:
        a = queue.popleft()
        
        for i in range(n):
            if check[i]==0 and graph[a][i]==1:
                queue.append(i)
                check[i]=1
                visited[st][i]=1

for i in range(n):
    bfs(i)

for i in range(n):
    print(*visited[i])