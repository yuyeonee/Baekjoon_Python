import sys
import heapq

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for i in range(M):
    s, e, c = map(int, sys.stdin.readline().split())
    graph[s].append((e, c))

A, B = map(int, input().split())

cost = [int(1e9)]*(N+1)

queue = []
heapq.heappush(queue, (A, 0))

while queue:
    st, co = heapq.heappop(queue)
    if cost[st]<co:
        continue
    for next in graph[st]:
        next_c = co+next[1]
        if cost[next[0]]>next_c:
            cost[next[0]] = next_c
            heapq.heappush(queue, (next[0], next_c))
    
print(cost[B])