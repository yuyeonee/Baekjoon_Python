import sys
import heapq

N, D = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(D+1)]

for i in range(D):
    graph[i].append((i+1, 1))

for i in range(N):
    start, end, dist = map(int, sys.stdin.readline().split())
    if end > D: continue
    graph[start].append((end, dist))


INF = 987654321
distance = [INF]*(D+1)
distance[0] = 0
queue = []
heapq.heappush(queue, (0,0))
while queue:
    st, d = heapq.heappop(queue)
    for next in graph[st]:
        next_d = distance[st] + next[1]
        
        if next_d<distance[next[0]]:
            distance[next[0]] = next_d
            heapq.heappush(queue, (next[0], next_d))
print(distance[-1])
