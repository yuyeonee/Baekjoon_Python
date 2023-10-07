import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

cost = [INF]*(V+1)
cost[K] = 0
queue = []
heapq.heappush(queue, (0, K))

while queue:
    co, st = heapq.heappop(queue)

    if cost[st]<co:
        continue

    for next_n , next_w in graph[st]:
        next_c = co + next_w
        if next_c < cost[next_n]:
            cost[next_n] = next_c
            heapq.heappush(queue, (next_c, next_n))
            

for i in range(1, V+1):
    print(cost[i] if not cost[i]==INF else 'INF')