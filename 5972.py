import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

queue = []
heapq.heappush(queue, (0, 1))
cost = [INF]*(N+1)

while queue:
    co, st = heapq.heappop(queue)

    if cost[st] < co:
        continue

    for next_n, c in graph[st]:
        next_c = co + c
        if cost[next_n] > next_c:
            cost[next_n] = next_c
            heapq.heappush(queue, (next_c, next_n))
            
print(cost[N])
